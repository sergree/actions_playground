import aiohttp
from loguru import logger


async def get(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        logger.debug(f"GET {url} ...")
        async with session.get(url) as resp:
            result = await resp.text()
            logger.debug(f"DONE {url}")
            return result
