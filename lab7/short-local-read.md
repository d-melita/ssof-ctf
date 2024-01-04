# Challenge `Short Local Read` Writeup

- Vulnerability: 
  - Format strings
- Where:
  - printf function
- Impact:
  - allows to read arbitrary memory

## Steps to reproduce

By analyzing the server, we see that the main function reads the user input to a buffer, reads the flag to a variable, and finally calls the `printf` function with the user input as argument.

By running `gdb` and placing a breakpoint before the `printf` function is called, we can see that the flag is stored on the 7th register. We can use this information to read the flag by sending a format string that will print the value of the 7th register. However the buffer only has 5 characters so it's necessary to use the `%n$s` specifier to print the value of the nth register:
```
%7$s
```
