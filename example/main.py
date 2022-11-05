import asyncio
import view
import web
from util import get_title, get_genre_ulrs

MAIN_URL = "https://www.beatport.com"
GENERAL_TOP_100_URL = f"{MAIN_URL}/top-100"
STRESS_TEST_COEF = 2


async def main():
    main_page_task = asyncio.create_task(web.get(MAIN_URL))
    general_top_100_task = asyncio.create_task(web.get(GENERAL_TOP_100_URL))

    main_page = await main_page_task
    genre_urls = get_genre_ulrs(main_page, MAIN_URL)

    page_titles = [get_title(main_page), get_title(await general_top_100_task)]

    genre_page_tasks = []
    for genre_url in genre_urls:
        genre_page_tasks.append(asyncio.create_task(web.get(genre_url)))

    for genre_page_task in genre_page_tasks:
        page_titles.append(get_title(await genre_page_task))

    view.render(page_titles)


if __name__ == "__main__":
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
