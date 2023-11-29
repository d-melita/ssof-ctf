# Challenge `I challenge you for a race` Writeup

- Vulnerability:
    - Time-of-check / Time-of - Race Condition

- Where:
    - `access` and `fopen` functions

- Impact:
    - Allows access to protected files

## Steps to reproduce

By analizing the `/challenge/` folder we can see that we have a file called `flag`, that we want to access, a c program `read_flag.c`, a `Makefile`, and a binary `challenge`, the `read_flag.c` compiled.
This `challenge` binary has the S bit set, which means that it will run with the effective UID of file the owner of the file, which is root. This means that we can use the binary to read the flag file. 

    
### Step 1: Create a new file temporarily file a symbolic link to it

In directory `/tmp/<dummy_name>`

```bash
$ touch temp_file
$ ln -s temp_file link
```

### Step 2: Call the binary, fork and create a symbolic link to the flag

Then, we must call the binary `challenge` with the link above using echo and pipes. At the same time, using fork, we must create a symbolic link to the flag file using the previous link.

```bash
$ echo "/tmp/99202/link" | /challenge/challenge &
$ ln -sf /challenge/flag link
```
If we find the right timing, the `access` function will return true when using the `temp_file` as argument. Then we change the link to the flag file and `fopen` will read it and reveal the flag . This works because `fopen` uses the effective UID (which is root because of the S bit in the binary) to check the permissions of the file, while `access` uses the real UID.

## Implementation

The full implementation can be found [here](i_challenge_you_for_a_race.sh).
