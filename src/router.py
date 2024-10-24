from fastapi import APIRouter

from src.repository import get_objects
from src.schemas import Objs

router = APIRouter(
    prefix='/weather',
    tags=['Weather'],
)


@router.get('')
async def get_weather() -> list[Objs]:
    objs_dict = await get_objects()
    return objs_dict
