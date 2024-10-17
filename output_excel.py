import asyncio

import aioconsole
import httpx
import pandas as pd

url = 'http://127.0.0.1:8000/weather-date'


async def fetch_url(url):
    """
    Отправляет GET запрос на эндпоинт микросервиса.
    args:
        url: str
    return:
        response
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response


async def import_to_excel(json_file):
    """
    Преобразует файл в формате json в файл excel.
    args:
        json_file: json
    return
        excel.xlsx
    """
    pd.DataFrame(json_file).to_excel('excel.xlsx')


async def main():
    """
    Обработчик команды экспорта данных в Excel
    """
    while True:
        command = await aioconsole.ainput(
            'Введите "start" для экспорта данных в Excel: ',
        )
        if command.strip().lower() == 'start':
            response = await fetch_url(url)
            await import_to_excel(response.json())
            print(f'Response status: {response.status_code}')
        else:
            print('Неверная команда. Попробуйте снова.')


asyncio.run(main())
