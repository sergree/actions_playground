import html
from typing import List


def render(items: List[str]):
    with open("template_index.html") as f:
        template = f.read()

    document = template.format(
        content="".join([f"<p>{html.escape(x)}</p>" for x in items])
    )

    with open("../index.html", "w") as f:
        f.write(document)
