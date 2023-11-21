import requests

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:22051"

# Create a session to persist the cookies between requests
s = requests.Session()

# Access the first link to set the user cookie
s.get(link)

for i in range(1000):
    response = s.get(link + "/number/" + str(i))

    if ("SSof" in response.text):
        print(response.text)
        break

