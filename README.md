# project_2024.10.11_fastapi_weater

- Стек технологий: 
- FastAPI
- Python 3.11.9
- Docker / Docker compose
- PostgreSQL 16 / asyncpg
- Uvicorn

- Для развертывания необходимо склонировать репозиторий:
```sh
git clone git@github.com:RV369/project_2024.10.11_fastapi_weater.git
```
- установить и активировать виртуальное окружение:

```sh
python -m venv venv
```
```sh
source venv/Scripts/activate
```

- создать файл .env 
- установить в развернутое виртуальное окружение необходимые библиотеки
```sh
pip install pandas openpyxl httpx aioconsole
```
- Запустить Docker
```sh
docker-compose up -d
```

- Далее следует подождать 30 минут чтобы наполнилась база данных
- Запустьть выполнение файла output_excel.py

- прописать в консоли команду 'start'
- файл excel.xlsx будет создан в папке с проектом

> Документация доступна по адресам:
> http://127.0.0.1:8000/docs
> http://127.0.0.1:8000/redoc

> API с данными о погоде доступны по адресу:
> http://127.0.0.1:8000/weather