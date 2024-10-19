# project_2024.10.11_fastapi_weater

Стек технологий: 
- FastAPI
- Python 3.11.9
- Docker / Docker compose
- PostgreSQL 16 / asyncpg
- Uvicorn

Для развертывания необходимо склонировать репозиторий:
- git clone git@github.com:RV369/project_2024.10.11_fastapi_weater.git

- установить виртуальное окружение:
- python -m venv venv
- source venv/Scripts/activate

- установить в развернутое виртуальное окружение необходимые библиотеки
- pip install pandas openpyxl httpx aioconsole

- Запустить Docker
- docker-compose up -d

- Далее следует подождать 30 минут чтобы наполнилась база данных
- Запустьть выполнение файла output_excel.py

- прописать в консоли команду 'start'
- файл excel.xlsx будет создан в папке с проектом

# Документация доступна по адресам:
- http://127.0.0.1:8000/docs

- http://127.0.0.1:8000/redoc
