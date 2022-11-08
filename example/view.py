import html
from datetime import datetime
from distutils.dir_util import copy_tree
from pathlib import Path
from typing import List


def render(items: List[str]):
    with open("templates/template_index.html") as f:
        template = f.read()

    document = template.format(
        now=datetime.utcnow(),
        content="".join([f"<p>{html.escape(x)}</p>" for x in items]),
    )

    Path("build").mkdir(parents=True, exist_ok=True)
    with open("build/index.html", "w") as f:
        f.write(document)

    copy_tree("static", "build/static")

    with open("build/example_file_002.html", "w") as f:
        f.write("002")
