# Challenge `Simple Overflow` Writeup

- Vulnerability: 
  - Buffer overflow
- Where:
  - test and buffer variables
- Impact:
  - allows to bypass if test

## Steps to reproduce

By analyzing the program, we can see that the main function creates two variables: 
`test`and `buffer`. The `test` variable is initialized to zero and the `buffer` 
variable is initialized to the user input which is read using the `gets` function.

Since `gets` doesn't check the length of the input, we can overflow the `buffer`
variable and overwrite the `test` variable. It is important to note that this only works
because the `buffer` variable is located "on top" of the `test` variable in stack, 
once the `test` variable is initialized first.

To overflow, we must compute the offset of the `test` variable from the `buffer` 
variable and then write any value "offset+1" times. We can do so using GBD by 
placing a breakpoint at `*main+71` (before the gets function) and reading the
address of `test` and `buffer` variables by using the `p &variable` command. 
This will output `0x80` meaning that we need to write a string with the length
of `0x81` characters to pass the `test != 0` condition and therefore to overflow.
Doing so, the flag is revealed.

## Implementation

Implementation [here](simple-overflow.py).