from typing import Optional

from pydantic import conint
from fastapi import APIRouter, Query, Request

from api.models import (
    Unit,
    UnitsGetResponse,
    UnitsUnitIdFloorsGetRequest
    )



units_router = APIRouter(
    prefix='/units',
    tags=['Units']
)



@units_router.post('/', response_model=None)
def post_units(
    unit_name: str = Query(..., alias='unitName'),
    unit_description: Optional[str] = Query(None, alias='unitDescription'),
    request: Request = ...,
) -> None:
    """
    Добавить в систему корпус организации
    """
    pass


@units_router.get(
    '/',
    response_model=None,
    responses={'200': {'model': UnitsGetResponse}}
)
def get_units() -> Optional[UnitsGetResponse]:
    """
    Получить список корпусов организации
    """
    pass


@units_router.get(
    '/{unit_id}',
    response_model=None,
    responses={'200': {'model': Unit}}
)
def get_units_unit_id(unit_id: int) -> Optional[Unit]:
    """
    Получить информацию о корпусе
    """
    pass


@units_router.put('/{unit_id}', response_model=None)
def put_units_unit_id(unit_id: int, body: Unit = None) -> None:
    """
    Изменить информацию о корпусе
    """
    pass


@units_router.get('/{unit_id}/floors', response_model=None)
def get_units_unit_id_floors(
    unit_id: int, body: UnitsUnitIdFloorsGetRequest = None
) -> None:
    """
    Получить список этажей корпуса
    """
    pass
