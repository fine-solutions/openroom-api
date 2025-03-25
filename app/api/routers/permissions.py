from typing import Optional

from pydantic import conint
from fastapi import APIRouter

from api.models import (
    ExtraPermission,
    PermissionsGetResponse
    )



permissions_router = APIRouter(
    prefix='/permissions',
    tags=['Permissions']
)



@permissions_router.get(
    '/',
    response_model=None,
    responses={'200': {'model': PermissionsGetResponse}}
)
async def get_permissions() -> Optional[PermissionsGetResponse]:
    """
    Получить список существующих разрешений пользователей
    """
    pass


@permissions_router.get(
    '/{permission_id}',
    response_model=None,
    responses={'200': {'model': ExtraPermission}}
)
async def get_permissions_permission_id(permission_id: int) -> Optional[ExtraPermission]:
    """
    Получить информацию о указанном разрешении
    """
    pass
