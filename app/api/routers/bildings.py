from typing import Optional

from pydantic import conint
from fastapi import APIRouter, Query, Request, UploadFile

from api.security import auth_scheme, refresh_scheme, get_user_id
from api.models import (
    BaseBuilding,
    FullBuilding
    )
from api.dependencies import (
    InitBuilding
)



buildings_router = APIRouter(
    prefix='/buiidings',
    tags=['Buildings']
)



@buildings_router.post('/', response_model=None)
async def post_units(building_schema: UploadFile) -> FullBuilding:
    """
    Добавить в систему строение
    """
    uc = InitBuilding(svg_schema=building_schema)
    building = await uc.execute()
    return FullBuilding(
        buildingID=building.buildingID,
        buildingName=building.buildingName,
        buildingDescription=building.buildingDescription,
        geopointLT=building.geopointLT,
        geopointRB=building.geopointRB,
        schema=building.svg_schema,
        unitIDs=building.unitIDs
    )


@buildings_router.get('/{building_id}', response_model=FullBuilding)
async def post_units(building_id: int) -> FullBuilding:
    """
    Получить строение по ID
    """
    pass


@buildings_router.put('/{building_id}', response_model=FullBuilding)
async def post_units(building_id: int, body: BaseBuilding) -> FullBuilding:
    """
    Изменить строение по ID
    """
    pass
