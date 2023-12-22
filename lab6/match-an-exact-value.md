# Challenge `Match an exact value` Writeup

- Vulnerability: 
  - Buffer overflow
- Where:
  - test and buffer variables
- Impact:
  - allows to bypass if test

## Steps to reproduce

Like the previous challenge, the main function creates two variables: 
`test`and `buffer`. The `test` variable is initialized to zero and the `buffer` 
variable is initialized to the user input which is read using the `gets` function.

Like mentioned in the previous challenge, the `gets` function does not check the 
length of the input, so we can use this to our advantage and overflow the `buffer` 
variable and overwrite the `test` variable. It is important to note that this only 
works once the `test` variable is initialized first which means that the `buffer` 
variable is located "on top" of the `test` variable in stack.

To overflow, we must compute the offset of the `test` variable from the `buffer` 
variable and then write any value "offset+1" times. We can do so using GBD by
placing a breakpoint, run the program and read the address of `test` and `buffer` 
variables by using the `p &variable` command. This will output `0x40` as the offset.

This time, we want to write a specific value, so we must fill the buffer first 
with `0x40` characters and then write the `dcba` value to the `test` variable to 
pass the `test == 0x61626364` condition, revealing the flag. The value `dcba` 
is written in reverse order because of the little endian architecture.

## Implementation

Implementation [here](match-an-exact-value.py).