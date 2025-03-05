from typing import Optional

from pydantic import conint
from fastapi import APIRouter, Query

from api.models import (
    RoomGroup,
    RoomGroupsGetResponse
    )



room_groups_router = APIRouter(
    prefix='/room-groups',
    tags=['Room groups']
)



@room_groups_router.post('/room-groups', response_model=None)
def post_room_groups(body: RoomGroup = None) -> None:
    """
    Создать группу помещений
    """
    pass


@room_groups_router.get(
    '/',
    response_model=None,
    responses={'200': {'model': RoomGroupsGetResponse}}
)
def get_room_groups(
    creator_id: Optional[int] = Query(None, alias='creatorId')
) -> Optional[RoomGroupsGetResponse]:
    """
    Получить список групп помещений
    """
    pass


@room_groups_router.get(
    '/{group_id}',
    response_model=None,
    responses={'200': {'model': RoomGroup}}
)
def get_room_groups_group_id(group_id: int) -> Optional[RoomGroup]:
    """
    Получить информацию о группе помещений
    """
    pass


@room_groups_router.put('/{group_id}', response_model=None)
def put_room_groups_group_id(group_id: int, body: RoomGroup = None) -> None:
    """
    Изменить группу помещений
    """
    pass


@room_groups_router.delete('/{group_id}', response_model=None)
def delete_room_groups_group_id(group_id: int) -> None:
    """
    Удалить группу помещений
    """
    pass
