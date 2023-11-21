import requests
import re

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23053"

# Create a session to persist the cookies between requests
s = requests.Session()

# Access the first link to set the user cookie
s.get(link)

# get target value from link + /hello
r = s.get(link + "/hello")
print(r.text)

target = re.search(r"target (\d+)", r.text, re.IGNORECASE)[1]
curr = re.search(r"Your current value is: (\d+)", r.text, re.IGNORECASE)[1]

while curr != target:
    r = s.get(link + "/more")
    curr = re.search(r"Your current value is: (\d+)", r.text, re.IGNORECASE)[1]

print("Target: " + target)
print("Current: " + curr)

r = s.get(link + "/finish")
print(r.text)