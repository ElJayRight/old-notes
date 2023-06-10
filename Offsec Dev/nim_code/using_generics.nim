import osproc

proc command[I,T](payload: var array[I,T]): string =
    var output: string
    echo payload
    output = exec_cmd_ex("powershell.exe gci").output
    return output

var num = ["1","2"]
echo command(num)