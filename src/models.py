from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class WeatherData(Base):
    __tablename__ = 'weather_data'
    id: Mapped[int] = mapped_column(primary_key=True)
    time: Mapped[str]
    temperature_2m: Mapped[str]
    wind_direction_10m: Mapped[str]
    wind_speed_10m: Mapped[str]
    surface_pressure: Mapped[str]
    precipitation: Mapped[str]
    weather_code: Mapped[str]
