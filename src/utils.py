class CreatePropertisObject:
    @classmethod
    async def weather_code(self, current_weather_code: int) -> str:
        """
        Преобразует 'wmo code' в понятное описание погоды.
        Args:
            current_weather_code: int
        Return:
            str
        """
        dictionary_weather_cod = {
            0: 'Чистое небо',
            1: 'Преимущественно ясно',
            2: 'Переменная облачность',
            3: 'Пасмурно',
            45: 'Туман',
            48: 'Отложение инея',
            51: 'Лёгкая морозь',
            53: 'Умеренная морозь',
            55: 'Интенсивная морозь',
            56: 'Легкий моросящий дождь',
            57: 'Интенсивный моросящий дождь',
            61: 'Небольшой дождь',
            63: 'Умеренный дождь',
            65: 'Сильный дождь',
            66: 'Ледяной дождь небольшой интенсивности',
            67: 'Ледяной дождь сильной интенсивности',
            71: 'Снегопад слабой интенсивности',
            73: 'Снегопад умеренной интенсивности',
            75: 'Снегопад сильной интенсивности',
            77: 'Снежные зёрна',
            80: 'Ливень слабой интенсивности',
            81: 'Ливень умеренной интенсивности',
            82: 'Ливень сильной интенсивности',
            85: 'Небольшой снегопад',
            86: 'Сильный снегопад',
            95: 'Гроза умеренная',
            96: 'Гроза с небольшим градом',
            99: 'Гроза и сильный град',
        }
        return dictionary_weather_cod[current_weather_code]

    @classmethod
    async def wind_direction(self, current_wind_direction_10m: float) -> str:
        """
        Преобразует направление в градусах в обозначение направления ветра.
        Args:
            current_wind_direction_10m: float
        Return:
            str
        """
        list_directions = ['С', 'СВ', 'В', 'ЮВ', 'Ю', 'ЮЗ', 'З', 'СЗ']
        index = int((current_wind_direction_10m + 22.5) / 45) % 8
        return list_directions[index]

    @classmethod
    async def get_weather_data(self, data: dict) -> dict:
        """
        Создание полей объекта базы данных.
        Args:
            data: dict
        Return:
            data_dict: dict
        """
        time = data['current']['time']
        wind_direction_10m = await self.wind_direction(
            data['current']['wind_direction_10m'],
        )
        weather_code = await self.weather_code(data['current']['weather_code'])
        temperature_2m = data['current']['temperature_2m']
        wind_speed_10m = data['current']['wind_speed_10m']
        pressure = data['current']['surface_pressure']
        precipitation = data['current']['precipitation']
        data_dict = {
            'time': f'{time}'.replace('T', ' | '),
            'temperature_2m': f'Температура: {temperature_2m} °C',
            'wind_direction_10m': f'Направление ветра: {wind_direction_10m}',
            'wind_speed_10m': f'Скорость ветра: {wind_speed_10m} m/s',
            'surface_pressure': f'Атмосферное давление: {pressure} hPa',
            'precipitation': f'Уровень осадков: {precipitation} mm',
            'weather_code': f'Текущая погода: {weather_code}',
        }
        return data_dict
