from typing import Optional

from pydantic import conint
from fastapi import APIRouter

from api.models import (
    FullRoom,
    BaseRoom,
    RoomsRoomIdAutoconfirmGetResponse,
    RoomsRoomIdAutoconfirmPutRequest
    )



rooms_router = APIRouter(
    prefix='/rooms',
    tags=['Rooms']
)



@rooms_router.get(
    '/{room_id}',
    response_model=None,
    responses={'200': {'model': FullRoom}}
)
async def get_rooms_room_id(room_id: int) -> Optional[FullRoom]:
    """
    Получить данные о помещении
    """
    pass


@rooms_router.put('/{room_id}', response_model=None)
async def put_rooms_room_id(room_id: int, body: BaseRoom = None) -> None:
    """
    Изменить даные о аудитории
    """
    pass


@rooms_router.get(
    '/{room_id}/autoconfirm',
    response_model=None,
    responses={'200': {'model': RoomsRoomIdAutoconfirmGetResponse}}
)
async def get_rooms_room_id_autoconfirm(
    room_id: int,
) -> Optional[RoomsRoomIdAutoconfirmGetResponse]:
    """
    Получить список пользователей, для которых настроенно автоподтверждение мероприятий
    """
    pass


@rooms_router.put('/{room_id}/autoconfirm', response_model=None)
async def put_rooms_room_id_autoconfirm(
    room_id: int, body: RoomsRoomIdAutoconfirmPutRequest = None
) -> None:
    """
    Изменить настройки автоподтверждения для помещения
    """
    pass
