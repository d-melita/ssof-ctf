# Challenge `Calling Functions` Writeup

- Vulnerability: 
  - Buffer overflow
- Where:
  - fp and buffer variables
- Impact:
  - allows to change function pointer

## Steps to reproduce

By analyzing the source code, we can note that the main function creates 
two variables: `fp` and `buffer`. The `fp` variable is initialized to zero 
and the `buffer` variable is initialized to the user input which is read 
using the `gets` function.

Like the previous challenges, we already know that the `gets` function does 
not check the length of the input, so we can use this to our advantage and 
overflow the `buffer` variable and overwrite the `fp` variable which only 
works because the `fp` variable is initialized first which means that the
`buffer` variable is located "on top" of the `fp` variable in stack.
Again, to overflow, we must compute the offset of the `fp` variable from 
the `buffer` variable and then write any value "offset+1" times. We can do 
so using GBD by placing a breakpoint, run the program and read the address 
of `fp` and `buffer` variables by using the `p &variable` command. This will
output `0x20` as the offset and the function address is `0x080486f1`.

This time, we want to write a specific value, so we must fill the buffer first 
with `0x20` characters and then write the function address value. When the program 
runs and calls the `fp` function it will call the `win` function, revealing the flag.

## Implementation

Implementation [here](calling-functions.py).
