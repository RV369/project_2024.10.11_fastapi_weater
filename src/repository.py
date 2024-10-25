from sqlalchemy import select

from src.db import connection
from src.models import WeatherData
from src.schemas import Objs


@connection
async def add_object(data: dict, session) -> int:
    """
    Создание объекта в базе данных.

    """
    new_obj = WeatherData(**data)
    session.add(new_obj)
    await session.flush()
    await session.commit()
    return new_obj.id


@connection
async def get_objects(session) -> list[Objs]:
    """
    Выводит список обектов из бвзы данных.

    """
    query = select(WeatherData).order_by(WeatherData.id.desc()).limit(limit=10)
    result = await session.execute(query)
    obj_models = result.scalars().all()
    dict_objcts = [Objs.model_validate(obj_model) for obj_model in obj_models]
    return dict_objcts
