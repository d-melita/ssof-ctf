import requests

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23052"

# Create a session to persist the cookies between requests
s = requests.Session()

# Access the first link to set the user cookie
s.get(link)

# use binary seacrh to get the number

low = 0
high = 1000000

while True:
    mid = (low + high) // 2
    r = s.get(link + "/number/" + str(mid))
    if "Higher!" in r.text:
        low = mid + 1
    elif "Lower!" in r.text:
        high = mid - 1
    elif "SSof" in r.text:
        print(r.text)
        break
    
