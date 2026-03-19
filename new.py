import requests
from bs4 import BeautifulSoup

url = "https://cses.fi/problemset/"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

# Check 1: Did the request succeed?
print(response.status_code)

# Check 2: Print all h2 tags to see what's actually there
for tag in soup.find_all("h2"):
    print(repr(tag.get_text()))
