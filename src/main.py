import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.db import init_db
from src.models import WeatherData
from src.repository import ObjektRepository
from src.router import router as weacher_router
from src.utils import CreatePropertisObject
from src.weather_api import fetch_url


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(weacher_router)


url = 'https://api.open-meteo.com/v1/forecast'
params = {
    'latitude': 55.697877,
    'longitude': 37.358603,
    'current': [
        'temperature_2m',
        'precipitation',
        'weather_code',
        'surface_pressure',
        'wind_speed_10m',
        'wind_direction_10m',
    ],
    'wind_speed_unit': 'ms',
    'timezone': 'Europe/Moscow',
}


async def main() -> WeatherData:
    """
    Получает данные о погоде и добавляет их в базу.
    """
    try:
        while True:
            obj = await fetch_url(url, params)
            data = await CreatePropertisObject.get_weather_data(obj)
            await ObjektRepository.add_object(data)
            await asyncio.sleep(180)
    except* AttributeError as errors:
        print([str(e) for e in errors.exceptions])


asyncio.create_task(main())
