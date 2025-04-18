from typing import Optional

from fastapi import APIRouter, Depends, Response

from api.models import FullUser, RegUserData, TokenSet, LoginPostRequest
from api.security import auth_scheme, refresh_scheme, get_user_id
from api.dependencies import (
    GetUser, 
    RegUser, 
    UserLoginBasic,
    UserLoginRefresh,
    EditUser
)



account_router = APIRouter(
    tags=['Account']
)



@account_router.get(
    '/account',
    response_model=None,
    responses={'200': {'model': FullUser}},
    dependencies=[Depends(auth_scheme)]
)
async def get_account(user_id: str = Depends(get_user_id)) -> FullUser:
    """
    Получить данные своего аккаунта
    """
    uc = GetUser(userID=user_id)

    user = await uc.execute()

    return FullUser(**user.model_dump())


@account_router.put(
    '/account', 
    response_model=None,
    dependencies=[Depends(auth_scheme)]
)
async def put_account(body: RegUserData = None, user_id: str = Depends(get_user_id)) -> FullUser:
    """
    Изменить данные своего аккаунта
    """
    uc = EditUser(
        userID=user_id,
        userName=body.userName,
        userDescription=body.userDescription,
        email=body.email,
        password=body.password
    )

    result = await uc.execute()
    return FullUser(**result.model_dump())


@account_router.post(
    '/login',
    response_model=None,
    responses={'200': {'model': TokenSet}}
)
async def post_login(res: Response, body: LoginPostRequest = None) -> TokenSet:
    """
    Войти в систему по логину и паролю (получить JWT токены)
    """
    uc = UserLoginBasic(email=body.email, password=body.password)
    jwt_set = await uc.execute()

    res.set_cookie(
        key='access_token',
        value=jwt_set['access_token'],
        secure=False,
        httponly=True,
        path='/'
    )
    res.set_cookie(
        key='refresh_token',
        value=jwt_set['refresh_token'],
        secure=False,
        httponly=True,
        path='/login/refresh'
    )

    return TokenSet(accessToken=jwt_set['access_token'], refreshToken=jwt_set['refresh_token'])


@account_router.post(
    '/login/refresh',
    response_model=None,
    responses={'200': {'model': TokenSet}}
)
async def post_login_refresh(res: Response, user_refresh: str = Depends(refresh_scheme)) -> TokenSet:
    """
    Обновить access token
    """
    uc = UserLoginRefresh(refresh_token=user_refresh)
    jwt_set = await uc.execute()

    res.set_cookie(
        key='access_token',
        value=jwt_set['access_token'],
        secure=False,
        httponly=True,
        path='/'
    )
    res.set_cookie(
        key='refresh_token',
        value=jwt_set['refresh_token'],
        secure=False,
        httponly=True,
        path='/login/refresh'
    )

    return TokenSet(accessToken=jwt_set['access_token'], refreshToken=jwt_set['refresh_token'])


@account_router.post('/register', response_model=None)
async def post_register(body: RegUserData = None) -> FullUser:
    """
    Создать аккаунт в системе
    """
    uc = RegUser(
        userName=body.userName,
        email=body.email,
        password=body.password,
        userDescription=body.userDescription
    )

    user = await uc.execute()

    return FullUser(**user.model_dump())
