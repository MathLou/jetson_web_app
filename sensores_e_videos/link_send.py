import requests
import main

url_server = main.server_link

def send_link():
    url = url_server+"link"
    data = {"link": "https://www.pudim.com.br/"}
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Link sent successfully:", response.json())
        else:
            print(f"Failed to send link. Status code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    send_link()