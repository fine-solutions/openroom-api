from typing import Optional

from fastapi import APIRouter

from api.models import User, TokenSet, LoginPostRequest



account_router = APIRouter(
    tags=['Account']
)



@account_router.get(
    '/account',
    response_model=None,
    responses={'200': {'model': User}}
)
def get_account() -> Optional[User]:
    """
    Получить данные своего аккаунта
    """
    pass


@account_router.put('/account', response_model=None)
def put_account(body: User = None) -> None:
    """
    Изменить данные своего аккаунта
    """
    pass


@account_router.post(
    '/login',
    response_model=None,
    responses={'200': {'model': TokenSet}}
)
def post_login(body: LoginPostRequest = None) -> Optional[TokenSet]:
    """
    Войти в систему по логину и паролю (получить JWT токены)
    """
    pass


@account_router.post(
    '/login/refresh',
    response_model=None,
    responses={'200': {'model': str}}
)
def post_login_refresh(body: str = None) -> Optional[str]:
    """
    Обновить access token
    """
    pass


@account_router.post('/register', response_model=None)
def post_register(body: User = None) -> None:
    """
    Создать аккаунт в системе
    """
    pass
