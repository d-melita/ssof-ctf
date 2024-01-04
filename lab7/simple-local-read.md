# Challenge `Simple Local Read` Writeup

- Vulnerability: 
  - Format strings
- Where:
  - printf function
- Impact:
  - allows to read arbitrary memory

## Steps to reproduce
By analyzing the main function, we can see that it reads the user input to a buffer, reads the flag to a variable and finally calls the `printf` function with the user input as argument.

If we run `gdb` and place a breakpoint before `printf` is called, we can see that the flag is stored on the 7th register. Using this information to our advantage, we can read the flag by sending a format string that will print the value of the 7th register:
```
%08x.%08x.%08x.%08x.%08x.%08x.%s
```
