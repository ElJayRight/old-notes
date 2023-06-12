# Overview
I'm going to start to build out a few shell code injectors and encoders cause it sounds fun and I will finally force myself to learn C.

Going to use this [crow's gitbook](https://crows-nest.gitbook.io/crows-nest/malware-development/getting-started-with-malware-development) and a few other things to get started.

# To do

|Topic|Status|Overview / Idea|
|-|-|----------|
|[Bad USB Part 1](./Bad%20USB%20part%201.md)|Done|Using a Pico to run a reverse shell when it is plugged in.|
|Bad USB Part 2|Not Started|Get it to reach back to an AWS instance and run commands remotely.|
|[Intro to MalDev](./Intro%20to%20MalDev.md)|Done|An intro to C, Windows API and Processes.|
|[Shellcode Injection](./Shellcode%20Injection.md)|Done|Create a remote process and thread and inject meterpreter shellcode to get a rev shell (No AV bypass)|
|[DLL Injection](./DLL%20Injection.md)|Done|The same thing as shellcode injection but using a DLL instead|
|[MACAddr Encoder / Injector](./Encoding%20Shellcode%20as%20MACAddrs.md)|In progress|I overheard something about decoding MACAddrs into shell code and running in memory being a valid AV bypass (As of June 2023).|
|[Shellcode runner in Nim](./Nim%20101.md)|Done|If this turns out well I might use Nim instead of C/C++ as it sounds easier. (Tiny bit of AV evasion too.) |

# Ideas
A list of any idea that jumps into my head that could be cool:
1. sharpkatz.exe -(donut)-> process injection -> <win?>
2. Have a pico W be an interface for the RPi deauther.
3. Build out an AWS instance with teraform for stagers and quick deployment.
4. pico w to run stager that calls back to rpi then rev shells to aws. This is very dumb but idc.
5. Do that syscalls trick to list processes but in win api and not syscalls.
6. Do syscalls with syswhispers then cry over my own implementation.