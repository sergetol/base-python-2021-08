"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

from typing import Optional, List
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> Optional[List[dict]]:
    async with ClientSession() as client_session:
        response = await client_session.get(url)
        return await response.json()


async def fetch_users_data() -> Optional[List[dict]]:
    return await fetch_json(USERS_DATA_URL)


async def fetch_posts_data() -> Optional[List[dict]]:
    return await fetch_json(POSTS_DATA_URL)
