from typing import Optional

from pydantic import conint
from fastapi import APIRouter

from api.models import (
    Event, 
    EventsGetResponse, 
    EventsRequestsGetResponse,
    Status,
    EventsEventIdRegistrationsGetResponse,
    EventsEventIdInvitesGetResponse,
    Decision
    )



events_router = APIRouter(
    prefix='/events',
    tags=['Events']
)



@events_router.get(
    '/',
    response_model=None,
    responses={'200': {'model': EventsGetResponse}}
)
def get_events(
    count: Optional[conint(le=100)] = 50,
    offset: Optional[int] = 0,
    free_entry: Optional[bool] = True,
    organizer_id: Optional[int] = None,
    room_id: Optional[int] = None,
    status: Optional[Status] = True,
) -> Optional[EventsGetResponse]:
    """
    Получить список мероприятий
    """
    pass


@events_router.post('/', response_model=None)
def post_events(body: Event = None) -> None:
    """
    Запланировать мероприятие
    """
    pass


@events_router.get(
    '/requests',
    response_model=None,
    responses={'200': {'model': EventsRequestsGetResponse}}
)
def get_events_requests(
    count: Optional[conint(le=100)] = 50, offset: Optional[int] = 0
) -> Optional[EventsRequestsGetResponse]:
    """
    Получить список запросов на бронирование
    """
    pass


@events_router.get(
    '/{event_id}',
    response_model=None,
    responses={'200': {'model': Event}}
)
def get_events_event_id(event_id: int) -> Optional[Event]:
    """
    Получить информацию о мероприятии
    """
    pass


@events_router.delete('/{event_id}', response_model=None)
def delete_events_event_id(event_id: int) -> None:
    """
    Отменить мероприятие
    """
    pass


@events_router.put('/{event_id}/decision', response_model=None)
def put_events_event_id_decision(event_id: int, decision: Decision = ...) -> None:
    """
    Ответить на запрос
    """
    pass


@events_router.get(
    '/{event_id}/invites',
    response_model=None,
    responses={'200': {'model': EventsEventIdInvitesGetResponse}},
    tags=['Invites'],
)
def get_events_event_id_invites(
    event_id: int,
) -> Optional[EventsEventIdInvitesGetResponse]:
    """
    Получить список приглашений на мероприятие
    """
    pass


@events_router.post('/{event_id}/invites', response_model=None, tags=['Invites'])
def post_events_event_id_invites(event_id: int, user_id: int = ...) -> None:
    """
    Пригласить пользователя на мероприятие
    """
    pass


@events_router.get(
    '/{event_id}/registrations',
    response_model=None,
    responses={'200': {'model': EventsEventIdRegistrationsGetResponse}},
    tags=['Registrations'],
)
def get_events_event_id_registrations(
    event_id: int,
) -> Optional[EventsEventIdRegistrationsGetResponse]:
    """
    Получить список заявок на посещение мероприятия
    """
    pass


@events_router.post(
    '/{event_id}/registrations',
    response_model=None,
    tags=['Registrations'],
)
def post_events_event_id_registrations(event_id: int) -> None:
    """
    Подать заявку на посещение мероприятия
    """
    pass
