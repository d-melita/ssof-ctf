# Challenge `Return Address` Writeup

- Vulnerability: 
  - Buffer overflow
- Where:
  - challenge function return address
- Impact:
  - allows to return to other address

## Steps to reproduce

Analyzing the source code, we can note that the challenge function creates one variable 
`buffer`and initializes it to the user input which is read using the `gets` function. 
The main function calls the `challenge` function but not the `win` function.

Once the `gets` function doesn't check the length of the input, we can use this to our 
advantage and overflow the `buffer` variable and change the return address of the `challenge` 
function. Additionally, we know that the stack keeps the `saved eip` in order to know where 
to return after the function finishes.

Using GDB, to see the address of the `eip` we can use the `info f` command but first we must 
place a breakpoint somewhere in the `challenge` function and run the program. Then, we should 
compute the offset between the `eip` address and the `buffer` address which is `0x16`.

Since we want to jump to the `win` function we must fill the buffer first with `0x16` characters 
and then write the `win` function address value (`0x080486f1`). Now when the programs returns 
from the `challenge` function it will return to the `win` function, revealing the flag.

## Implementation

Implementation [here](return-address.py).
