from typing import Optional

from pydantic import conint
from fastapi import APIRouter, Query, Request, UploadFile

from api.security import auth_scheme, refresh_scheme, get_user_id
from api.models import (
    BaseBuilding,
    FullBuilding,
    FullUnit,
    Floor,
    FullRoom
    )
from api.dependencies import (
    InitBuilding,
    GetBuilding
)



buildings_router = APIRouter(
    prefix='/buiidings',
    tags=['Buildings']
)



@buildings_router.post('/', response_model=None)
async def post_building(building_schema: UploadFile) -> FullBuilding:
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
        units=[FullUnit(
            unitID=u.unitID,
            unitName=u.unitName,
            unitDescription=u.unitDescription,
            floors=[Floor(
                floorID=f.floorID,
                floorName=f.floorName,
                floorSequence=f.floorSequence,
                rooms=[FullRoom(
                    roomID=r.roomID,
                    roomName=r.romName,
                    roomDescription=r.roomDescription,
                    floorID=f.floorID,
                    unitID=u.unitID
                ) for r in f.rooms]
            ) for f in u.floors]
        ) for u in building.units]
    )


@buildings_router.get('/', response_model=FullBuilding)
async def get_buildings() -> FullBuilding:
    """
    Получить список строений
    """
    pass


@buildings_router.get('/{building_id}', response_model=FullBuilding)
async def get_building(building_id: int) -> FullBuilding:
    """
    Получить строение по ID
    """
    uc = GetBuilding(building_id=building_id)
    building = await uc.execute()
    return FullBuilding(
        buildingID=building.buildingID,
        buildingName=building.buildingName,
        buildingDescription=building.buildingDescription,
        geopointLT=building.geopointLT,
        geopointRB=building.geopointRB,
        schema=building.svg_schema,
        units=[FullUnit(
            unitID=u.unitID,
            unitName=u.unitName,
            unitDescription=u.unitDescription,
            floors=[Floor(
                floorID=f.floorID,
                floorName=f.floorName,
                floorSequence=f.floorSequence,
                rooms=[FullRoom(
                    roomID=r.roomID,
                    roomName=r.romName,
                    roomDescription=r.roomDescription,
                    floorID=f.floorID,
                    unitID=u.unitID
                ) for r in f.rooms]
            ) for f in u.floors]
        ) for u in building.units]
    )


@buildings_router.put('/{building_id}', response_model=FullBuilding)
async def put_building(building_id: int, body: BaseBuilding) -> FullBuilding:
    """
    Изменить строение по ID
    """
    pass
