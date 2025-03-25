from typing import Optional

from pydantic import conint
from fastapi import APIRouter

from api.models import (
    Organization
    )



organization_router = APIRouter(
    prefix='/organization',
    tags=['Organization']
)



@organization_router.get(
    '/',
    response_model=None,
    responses={'200': {'model': Organization}}
)
async def get_organization() -> Optional[Organization]:
    """
    Получить информацию об организации
    """
    pass
