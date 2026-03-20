import os


def slugify(title):
    return title.lower().replace(" ", "_")


def create_folder(idd, title):
    folder = f"{idd}_{slugify(title)}"
    os.makedirs(folder, exist_ok=True)
    return folder


def write_file(folder, filename, content):
    path = os.path.join(folder, filename)
    with open(path, "w") as f:
        f.write(content)
