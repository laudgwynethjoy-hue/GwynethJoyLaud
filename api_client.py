
import requests

url = "https://gwynethjoylaud-1.onrender.com/skills"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("My Skills:")

    for skill in data["skills"]:
        print("-", skill)

else:
    print("Request failed.")
    print("Status Code:", response.status_code)
