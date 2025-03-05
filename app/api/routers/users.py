from typing import Optional

from pydantic import conint
from fastapi import APIRouter

from api.models import (
    User,
    UsersUserIdAdminedRoomsPutRequest,
    UsersUserIdAvailableRoomsPutRequest,
    UsersUserIdPermissionsPutRequest
    )



users_router = APIRouter(
    prefix='/users',
    tags=['Users']
)



@users_router.get(
    '/{user_id}',
    response_model=None,
    responses={'200': {'model': User}})
def get_users_user_id(user_id: int) -> Optional[User]:
    """
    Получить информацию о пользователе
    """
    pass


@users_router.delete('/{user_id}', response_model=None)
def delete_users_user_id(user_id: int) -> None:
    """
    Удалить пользователя
    """
    pass


@users_router.put('/{user_id}/admined_rooms', response_model=None)
def put_users_user_id_admined_rooms(
    user_id: int, body: UsersUserIdAdminedRoomsPutRequest = None
) -> None:
    """
    Изменить список помещений, управляемых пользователем
    """
    pass


@users_router.put('/{user_id}/available_rooms', response_model=None)
def put_users_user_id_available_rooms(
    user_id: int, body: UsersUserIdAvailableRoomsPutRequest = None
) -> None:
    """
    Изменить список доступных пользователю помещений
    """
    pass


@users_router.put('/{user_id}/permissions', response_model=None)
def put_users_user_id_permissions(
    user_id: int, body: UsersUserIdPermissionsPutRequest = None
) -> None:
    """
    Изменить права пользователя
    """
    pass
