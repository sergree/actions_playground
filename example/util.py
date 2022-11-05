from typing import List

from pyquery import PyQuery as pq


def get_title(text: str) -> str:
    return pq(text)("title").text()


def get_genre_ulrs(text: str, main_url: str) -> List[str]:
    return list(
        map(
            lambda x: f"{main_url}{x.attrib['href']}",
            pq(text).find("a.genre-drop-list__genre"),
        )
    )
