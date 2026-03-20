from bs4 import BeautifulSoup


def parse_problem(html):
    soup = BeautifulSoup(html, "html.parser")

    title_id = soup.find("h1")
    if title_id is None:
        return None

    content = soup.find("div", class_="content")
    if content is None:
        return None

    return {
        "title": title_id.get_text().strip(),
        "text": content.get_text("\n").strip(),
    }
