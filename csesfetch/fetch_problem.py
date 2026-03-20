import requests

from csesfetch.parser import parse_problem
from csesfetch.utils import create_folder, write_file


def fetch_problem(idd):
    url = f"https://cses.fi/problemset/task/{idd}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch")
        return

    data = parse_problem(response.text)

    if data is None:
        print("Failed to parse problem")
        return

    folder = create_folder(idd, data["title"])

    write_file(folder, "problem.txt", data["text"])

    print(f"Fetched {idd}: {data['title']}")
