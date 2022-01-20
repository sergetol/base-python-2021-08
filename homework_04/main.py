"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from models import engine, Base, Session, User, Post
from typing import List
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data


async def recreate_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


USER_ATTRIBUTES_MAP = dict(
    name="name",
    username="username",
    email="email",
    phone="phone",
    website="website",
)

POST_ATTRIBUTES_MAP = dict(
    user_id="userId",
    title="title",
    body="body",
)


async def create_db_objects(Model, objects: List[dict], attr_map: dict):
    async with Session() as session:
        async with session.begin():
            session.add_all(
                [Model(**{k: obj[v] for k, v in attr_map.items()}) for obj in objects]
            )


async def async_main():
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    print(len(users_data), "users gathered")
    print(len(posts_data), "posts gathered")

    await recreate_tables()
    print("All tables recreated")

    await create_db_objects(User, users_data, USER_ATTRIBUTES_MAP)
    print("All users created")
    await create_db_objects(Post, posts_data, POST_ATTRIBUTES_MAP)
    print("All posts created")


def main():
    print("START main")
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()  # on Windows only
    )
    asyncio.run(async_main())
    print("END main")


if __name__ == "__main__":
    main()
