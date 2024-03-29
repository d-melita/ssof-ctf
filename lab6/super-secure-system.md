# Challenge `Super Secure System` Writeup

- Vulnerability: 
  - Buffer overflow
- Where:
  - check_password function return address
- Impact:
  - allows to return to other address

## Steps to reproduce

By analyzing the source code, we can note that the `challenge` function creates 
one variable `pass` and initializes it to the user input which is read using the `read` function.

The `read` function checks the length of the input, so we can't overflow the `pass` variable.
However, the `check_password` function calls the `strcpy` function which copies the
`pass` variable to the `buffer` variable which is 32 bytes long. The `strcpy` function 
does not check the length of the input, so we can overflow the `buffer` variable and change 
the return address of `check_password` function.

This time, our job is not so easy. If we simply compute the offset between the `eip` address 
and the `buffer` address and fill the stack with random input plus the address we want to jump to we 
will get a faulty execution. When looking at the disassembly of the `main` function we can see that
after the `check_password` function returns the program uses the `ebx` value but since we 
overflown the stack the `ebx` value is now corrupted.

This is due to the fact that the function is called with the `call` instruction which pushes the 
`eip` value to the stack and then at the beginning of the function the `ebp` value and 
`ebx` value are pushed to the stack, only then is the `buffer` variable initialized. 

In order to correctly overflow the stack, first we must compute the offset between `buffer` and `ebx`
then read the content of the `ebx` and `ebp` values. Finally, we must find the address of the 
next instruction after the `check_password` function is called to bypass the if condition.

The payload that reveals the flag is then:
```python
payload = b'x'*0x24 + p32(0x804a001) + p32(0xffffd158) + p32(0x080487d9)
```

## Implementation

Implementation [here](super-secure-system.py).
