import requests

url = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("=== Chuck Norris Joke ===")
    print(data["value"])

except requests.exceptions.RequestException as e:
    print(f"Erreur : {e}")