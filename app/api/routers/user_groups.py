from typing import Optional

from pydantic import conint
from fastapi import APIRouter

from api.models import (
    UserGroup,
    UserGroupsGetResponse
    )



user_groups_router = APIRouter(
    prefix='/user-groups',
    tags=['User groups']
)



@user_groups_router.post('/', response_model=None)
def post_user_groups(body: UserGroup = None) -> None:
    """
    Создать группу пользователей
    """
    pass


@user_groups_router.get(
    '/',
    response_model=None,
    responses={'200': {'model': UserGroupsGetResponse}}
)
def get_user_groups(
    creator_id: Optional[int] = None,
) -> Optional[UserGroupsGetResponse]:
    """
    Получить список групп пользователей
    """
    pass


@user_groups_router.get(
    '/{group_id}',
    response_model=None,
    responses={'200': {'model': UserGroup}}
)
def get_user_groups_group_id(group_id: int) -> Optional[UserGroup]:
    """
    Получить информацию о группе пользователей
    """
    pass


@user_groups_router.put('/{group_id}', response_model=None)
def put_user_groups_group_id(group_id: int, body: UserGroup = None) -> None:
    """
    Изменить группу пользователей
    """
    pass


@user_groups_router.delete('/{group_id}', response_model=None)
def delete_user_groups_group_id(group_id: int) -> None:
    """
    Удалить группу пользователей
    """
    pass
