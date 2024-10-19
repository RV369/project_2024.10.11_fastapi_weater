from sqlalchemy import select

from src.db import new_session
from src.models import WeatherData
from src.schemas import Objs


class ObjektRepository:
    @classmethod
    async def add_object(cls, data: dict) -> int:
        """
        Создание объекта в базе данных.
        Args:
            data: WeatherData
        Return:
            id: int
        """
        async with new_session() as session:
            new_obj = WeatherData(**data)
            session.add(new_obj)
            await session.flush()
            await session.commit()
            return new_obj.id

    @classmethod
    async def get_objects(cls, limit: int | None = 10) -> list[Objs]:
        """
        Выводит список обектов из бвзы данных.
        Args:
            limit: int
        Return:
            dict_objcts: list[objs]
        """
        async with new_session() as session:
            query = (
                select(WeatherData)
                .order_by(WeatherData.id.desc())
                .limit(limit)
            )
            result = await session.execute(query)
            obj_models = result.scalars().all()
            dict_objcts = [
                Objs.model_validate(obj_model) for obj_model in obj_models
            ]
            return dict_objcts
