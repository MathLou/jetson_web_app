import base64
import requests

server_link = 'http://172.31.46.12:5000/'
with open("pudim.jpg", "rb") as img:
    b64_string = base64.b64encode(img.read()).decode("utf-8")

payload = {"image_base64": b64_string}
r = requests.post(server_link + "image", json=payload)
print(r.status_code)