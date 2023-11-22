from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23055

### run a remote process
s = remote(SERVER, PORT, timeout=9999)

# read the welcome message and get target

s.recvuntil(b'get to ')
target = s.recvuntil(b'.')[:-1].decode()

s.recvuntil(b'CURRENT = ')
curr = s.recvuntil(b'.')[:-1].decode()

while curr != target:
    # send MORE
    s.sendline('MORE'.encode('utf-8'))
    s.recvuntil(b'CURRENT = ')
    curr = s.recvuntil(b'.')[:-1].decode()

log.info("Target: " + target)
log.info("Current: " + curr)

# send FINISH
s.sendline('FINISH'.encode('utf-8'))
s.recvuntil(b'GREAT JOB: ')
flag = s.recvuntil(b'\n')[:-1].decode()
log.info("Flag: " + flag)
s.close()
