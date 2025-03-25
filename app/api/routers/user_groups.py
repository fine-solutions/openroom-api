from typing import Optional

from pydantic import conint
from fastapi import APIRouter

from api.models import (
    BaseUserGroup,
    FullUserGroup,
    UserGroupsGetResponse
    )



user_groups_router = APIRouter(
    prefix='/user-groups',
    tags=['User groups']
)



@user_groups_router.post('/', response_model=None)
async def post_user_groups(body: BaseUserGroup = None) -> None:
    """
    Создать группу пользователей
    """
    pass


@user_groups_router.get(
    '/',
    response_model=None,
    responses={'200': {'model': UserGroupsGetResponse}}
)
async def get_user_groups(
    creator_id: Optional[int] = None,
) -> Optional[UserGroupsGetResponse]:
    """
    Получить список групп пользователей
    """
    pass


@user_groups_router.get(
    '/{group_id}',
    response_model=None,
    responses={'200': {'model': FullUserGroup}}
)
async def get_user_groups_group_id(group_id: int) -> Optional[FullUserGroup]:
    """
    Получить информацию о группе пользователей
    """
    pass


@user_groups_router.put('/{group_id}', response_model=None)
async def put_user_groups_group_id(group_id: int, body: BaseUserGroup = None) -> None:
    """
    Изменить группу пользователей
    """
    pass


@user_groups_router.delete('/{group_id}', response_model=None)
async def delete_user_groups_group_id(group_id: int) -> None:
    """
    Удалить группу пользователей
    """
    pass
