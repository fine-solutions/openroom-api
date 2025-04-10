from typing import Annotated, Any, Union
from uuid import UUID

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, APIKeyCookie
from fastapi import Depends

from api.dependencies import jwt_manager, GetJWTSubject

from config import conf



# auth_scheme = HTTPBearer(scheme_name='JWT')
auth_scheme = APIKeyCookie(scheme_name='JWT', name='access_token')
refresh_scheme = APIKeyCookie(scheme_name='JWT refresh', name='refresh_token')



# def get_user_id(token: Annotated[HTTPAuthorizationCredentials, Depends(auth_scheme)]) -> UUID:
#     token_string = token.credentials
#     return UUID(jwt_manager.get_jwt_subject(token_string))

async def get_user_id(cookie: str = Depends(auth_scheme)) -> UUID:
    uc = GetJWTSubject(access_token=cookie)
    return await uc.execute()
