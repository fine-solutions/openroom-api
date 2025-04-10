from typing import Optional

from pydantic import conint
from fastapi import APIRouter, Depends

from api.models import (
    FullUser,
    UsersUserIdAdminedRoomsPutRequest,
    UsersUserIdAvailableRoomsPutRequest,
    UsersUserIdPermissionsPutRequest
    )
from api.security import auth_scheme, get_user_id
from api.dependencies import (
    GetUser
)

from config import conf



users_router = APIRouter(
    prefix='/users',
    tags=['Users'],
    dependencies=[Depends(auth_scheme)]
)



@users_router.get(
    '/{user_id}',
    response_model=None,
    responses={'200': {'model': FullUser}})
async def get_users_user_id(user_id: int) -> Optional[FullUser]:
    """
    Получить информацию о пользователе
    """
    uc = GetUser(userID=user_id)

    return await uc.execute()


@users_router.delete('/{user_id}', response_model=None)
async def delete_users_user_id(user_id: int, requester_id: str = Depends(get_user_id)) -> None:
    """
    Удалить пользователя
    """
    pass


@users_router.put('/{user_id}/admined_rooms', response_model=None)
async def put_users_user_id_admined_rooms(
    user_id: int, body: UsersUserIdAdminedRoomsPutRequest = None, requester_id: str = Depends(get_user_id)
) -> None:
    """
    Изменить список помещений, управляемых пользователем
    """
    pass


@users_router.put('/{user_id}/available_rooms', response_model=None)
async def put_users_user_id_available_rooms(
    user_id: int, body: UsersUserIdAvailableRoomsPutRequest = None, requester_id: str = Depends(get_user_id)
) -> None:
    """
    Изменить список доступных пользователю помещений
    """
    pass


@users_router.put('/{user_id}/permissions', response_model=None)
async def put_users_user_id_permissions(
    user_id: int, body: UsersUserIdPermissionsPutRequest = None, requester_id: str = Depends(get_user_id)
) -> None:
    """
    Изменить права пользователя
    """
    pass
