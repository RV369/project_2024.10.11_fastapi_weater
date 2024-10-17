from pydantic import BaseModel, ConfigDict


class ObjektAdd(BaseModel):
    """
    Схема объекта при создании объекта.
    """

    time: str
    temperature_2m: str
    wind_direction_10m: str
    wind_speed_10m: str
    surface_pressure: str
    precipitation: str
    weather_code: str


class Objs(ObjektAdd):
    """
    Схема вывода объектов.
    """

    id: int
    model_config = ConfigDict(from_attributes=True)
