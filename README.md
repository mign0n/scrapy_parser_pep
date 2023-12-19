# Scrapy PEP parser

## Описание

CLI утилита для парсинга Python PEP.

## Технологии

- [Python v3.9](https://docs.python.org/3.9/)
- [Scrapy v2.5](https://docs.scrapy.org/en/2.5/index.html)

## Использование

Запуск парсера осуществляется командой:

```shell
scrapy crawl pep
```

Файлы с результатами парсинга сохраняются в директории `results/`.

## Установка

- Склонируйте репозиторий и перейдите в директорию проекта

```shell
git clone https://github.com/mign0n/scrapy_parser_pep.git && cd scrapy_parser_pep
```

- Установите и активируйте виртуальное окружение

```shell
python -m venv venv && source venv/bin/activate
```

- Установите зависимости из файла requirements.txt

```shell
pip install -r requirements.txt
```

## Авторы

- [mign0n](https://github.com/mign0n)
- [yandex-praktikum](https://github.com/yandex-praktikum)
