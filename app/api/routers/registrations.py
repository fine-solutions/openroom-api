from typing import Optional

from pydantic import conint
from fastapi import APIRouter

from api.models import (
    RegistrationsGetResponse,
    EventRegistrationStatus,
    Decision
    )



registrations_router = APIRouter(
    prefix='/registrations',
    tags=['Registrations']
)



@registrations_router.get(
    '/',
    response_model=None,
    responses={'200': {'model': RegistrationsGetResponse}}
)
def get_registrations(
    status: Optional[EventRegistrationStatus] = None,
) -> Optional[RegistrationsGetResponse]:
    """
    Получить список исходящих запросов на посещение мероприятий
    """
    pass


@registrations_router.put(
    '/{event_id}/{user_id}', response_model=None
)
def put_registrations_event_id_user_id(
    event_id: int, user_id: int = ..., decision: Decision = ...
) -> None:
    """
    Обработать заявку на посещение мероприятия
    """
    pass
