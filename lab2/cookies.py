import requests
import re

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23054"

# Create a session to persist the cookies between requests
s = requests.Session()

# get cookie, target value, and current value from link + /hello
r = s.get(link + "/hello")
cookies = r.cookies.get_dict()

target = re.search(r"target (\d+)", r.text, re.IGNORECASE)[1]
curr = re.search(r"Your current value is: (\d+)", r.text, re.IGNORECASE)[1]

while curr != target:
    r = requests.get(link + "/more", cookies=cookies)
    curr = re.search(r"Your current value is: (\d+)", r.text, re.IGNORECASE)[1]

print("Target: " + target)
print("Current: " + curr)

r = s.get(link + "/finish")
print(r.text)