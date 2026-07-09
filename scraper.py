import requests

URL = "https://cuantoestaeldolar.pe/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/138 Safari/537.36"
    )
}

response = requests.get(URL, headers=headers, timeout=30)
response.raise_for_status()

print(f"Status: {response.status_code}")

with open("pagina.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("HTML guardado correctamente.")
