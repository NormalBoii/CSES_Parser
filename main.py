import requests
from bs4 import BeautifulSoup
import os

idd = input("Enter id : ")
url = f"https://cses.fi/problemset/task/{idd}"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

content = soup.find("div", class_="content")
title = soup.find("h1")

if title is None:
    print("Not Found")
    exit()

title2 = title.get_text()
folder = f"{idd}_{title2}"
os.makedirs(folder, exist_ok=True)
if content:
    text = content.get_text()
    with open(f"{folder}/problem.txt", "w") as f:
        f.write(text)

print("Done")
