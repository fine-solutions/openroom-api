from typing import Optional

from fastapi import APIRouter


from core.usecases import RegUser
from adapters import DBAuthCRUD, DBUserCrud
from api.models import FullUser, RegUserData, TokenSet, LoginPostRequest
from database import DBManager

from config import conf


RegUser.set_dependencies(user_crud=DBUserCrud, auth_crud=DBAuthCRUD)



account_router = APIRouter(
    tags=['Account']
)



@account_router.get(
    '/account',
    response_model=None,
    responses={'200': {'model': FullUser}}
)
async def get_account() -> Optional[FullUser]:
    """
    Получить данные своего аккаунта
    """
    pass


@account_router.put('/account', response_model=None)
async def put_account(body: RegUserData = None) -> None:
    """
    Изменить данные своего аккаунта
    """
    pass


@account_router.post(
    '/login',
    response_model=None,
    responses={'200': {'model': TokenSet}}
)
async def post_login(body: LoginPostRequest = None) -> Optional[TokenSet]:
    """
    Войти в систему по логину и паролю (получить JWT токены)
    """
    pass


@account_router.post(
    '/login/refresh',
    response_model=None,
    responses={'200': {'model': str}}
)
async def post_login_refresh(body: str = None) -> Optional[str]:
    """
    Обновить access token
    """
    pass


@account_router.post('/register', response_model=None)
async def post_register(body: RegUserData = None) -> None:
    """
    Создать аккаунт в системе
    """
    uc = RegUser(
        userName=body.userName,
        email=body.email,
        password=body.password,
        userDescription=body.userDescription
    )

    print(await uc.execute())

    return 
