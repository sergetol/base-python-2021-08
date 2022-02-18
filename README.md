# base-python-2021-08 [![Run tests for homework](https://github.com/sergetol/base-python-2021-08/actions/workflows/run_tests.yml/badge.svg)](https://github.com/sergetol/base-python-2021-08/actions/workflows/run_tests.yml)

## [OTUS - Python Developer. Basic](https://otus.ru/lessons/python-basic/)
### Homework repository
Sergey Tolstinskiy

## homework_07

- портировано ранее созданное `Flask`-приложение на `Django`
- создан `Django`-проект, добавлены приложения, в debug режиме подключен `debug_toolbar`
- созданы модели, добавлены миграции
- написан `Dockerfile.dev` для сборки debug образа приложения
- написан `docker-compose.yaml` файл, запускающий отдельно БД `Postgres`, а также приложение в debug режиме

## homework_06

- доработано базовое приложение на `Flask`
- добавлены модели
- есть возможность добавлять/редактировать записи
- добавлена страница со списком добавленных записей
- написаны `Dockerfile.dev` и `Dockerfile` для сборки debug и prod образов приложения
- написан `docker-compose.yaml` файл, запускающий отдельно БД `Postgres`, а также приложения в debug и prod режимах

## homework_05

- создано базовое приложение на `Flask`
- добавлены вьюшки `/` и `/about/`, а также errorhandler на 404
- подключены Bootstrap стили и добавлена навигационная панель

## homework_04

- доработаны модули `jsonplaceholder_requests`, `models`, `main`
- асинхронно выполняются запросы внешних данных пользователей и постов
- полученные данные асинхронно добавляются в БД

## homework_03

- создано веб-приложение на `FastAPI`
- написан `Dockerfile` для сборки образа приложения

## homework_02

- объявлены необходимые исключения
- доработан базовый класс `Vehicle`
- создан датакласс `Engine`
- создан класс `Car`
- создан класс `Plane`

## homework_01

- написана функция возведения N чисел в указанную степень (по умоланию во вторую)
- написана функция, возвращающая из списка целых чисел только нечётные/чётные/простые числа (по умолчанию нечётные)
- (*)создан декоратор для замера времени выполнения функции и показа вложенных вызовов функции (на примере вычисления чисел Фибоначчи)
