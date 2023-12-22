# Challenge `Super Secure Lottery` Writeup

- Vulnerability: 
  - Buffer overflow
- Where:
  - run_lottery function in read call
- Impact:
  - allows to change variable value

## Steps to reproduce

Analyzing the server, we can see that it creates a `lottery` string and fills it with random values.
Then it reads user input to `guess` and if the `guess` is equal to `lottery` the user wins.

The read is done using the `read` function but the length of the input is `GUESS_SIZE` 
while the `guess` string has a `LOTTERY_LEN` length which is smaller, so we can overflow the string.

Even though the program uses canaries, we can still exploit it. The canaries will prevent 
some stack overflows but they are only checked when the function returns and the `run_lottery` 
function never returns so we can change the value of a canary and the program won't "notice".

Computing the offset between the `guess` variable and the `lottery` variable we can input 
a string big enough to overflow the `guess` variable and overwrite the `lottery` variable 
in order to make them have the same value. 

To achieve this, first input 8 characters for the `guess` value followed by 40 random characters 
and finally the same 8 initial characters for the `lottery`. This will reveal the flag.

## Implementation

Implementation [here](super-secure-lottery.sh).
