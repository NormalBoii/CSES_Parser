import requests
from bs4 import BeautifulSoup

url = "https://cses.fi/problemset/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

header = soup.find(
    lambda tag: tag.name == "h2" and tag.get_text() == "Introductory Problems"
)
if header:
    task_list = header.find_next("ul", class_="task-list")

    if task_list:
        problems = task_list.find_all("li")
        for question in problems:
            link = question.find("a")
            if link:
                name = link.text
                print(name)
