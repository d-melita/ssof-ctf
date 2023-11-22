# Challenge `Secure By Design` Writeup

- Vulnerability:
    - Cookie poisoning

- Where:
    - `/user` cookie

- Impact:
    - Allows to get access to the admin account

## Thinking process
Upon entering a nickname, the server responds with "Unfortunately our page is still under construction for non-admin users." It also adds a cookie with a user key and a base64 encoded value (evident by the == at the end). Decoding this value reveals that it's the nickname entered by the user. To check the cookie value in the browser we should do the following steps:
1. Open the developer tools (right click -> inspect element)
2. Go to the Application tab
3. Under Storage, click on Cookies
4. Click on the link that appears below
5. Then we can see the cookie value

A logical step was to try to enter with the `admin` nickname. However, the server prevents this by changing it to fake-admin. It's possible to verify this by decoding the value of cookie user key and checking that it's the same whether the nickname is admin or fake-admin. To bypass this we should send a request with the cookie value poisoned equal to the base64 encoded value of admin.

## Steps to reproduce
We can do the above using a python script

### Step 1: Encode admin nickname
```python
import requests
import base64

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23056"
adminEncoded = base64.b64encode(b"admin").decode("utf-8")
```

### Step 2: Send request with poisoned cookie and get the flag
```python
r = requests.get(link, cookies={'user': adminEncoded})
print(r.text)
```
Then the flag should be display in the console.

## Implementation

The full implementation can be found [here](secure-by-design.py).