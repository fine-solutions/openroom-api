from typing import Optional

from pydantic import conint
from fastapi import APIRouter

from api.models import (
    InvitesGetResponse,
    EventInviteStatus,
    Decision
    )



invites_router = APIRouter(
    prefix='/invites',
    tags=['Invites']
)



@invites_router.get(
    '/',
    response_model=None,
    responses={'200': {'model': InvitesGetResponse}}
)
def get_invites(status: EventInviteStatus) -> Optional[InvitesGetResponse]:
    """
    Получить список приглашений на мероприятия
    """
    pass


@invites_router.put('/{event_id}/answer', response_model=None)
def put_invites_event_id_answer(event_id: int, decision: Decision = ...) -> None:
    """
    Ответить на приглашение
    """
    pass
