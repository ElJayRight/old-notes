import osproc

proc command(): string = 
    var output: string
    output = exec_cmd_ex("powershell.exe gci").output
    return output

echo command()