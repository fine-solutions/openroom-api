from datetime import datetime, timedelta, timezone
from typing import Literal, Optional

import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError

from core.dependencies import IJWTManager



class JWTManager(IJWTManager):
    def __init__(self, key: str, access_ttl: Optional[int] = 300, refersh_ttl: Optional[int] = 3000) -> None:
        self.__secret_key = key
        self.__access_ttl = timedelta(seconds=access_ttl)
        self.__refresh_ttl = timedelta(seconds=refersh_ttl)

    
    def __create_token(self, subj: str, exp_time: datetime, type: Literal['access', 'refresh']) -> bytes:
        token = jwt.encode(
            payload = {
                'sub': subj,
                'exp': exp_time,
                'type': type
                },
            key = self.__secret_key,
            algorithm="HS256"
        )

        return token


    def __decode_token(self, token: bytes) -> dict:
        # try:
        decode = jwt.decode(
            jwt = token,
            key = self.__secret_key,
            algorithms=["HS256"]
        )
        # except ExpiredSignatureError:
        #     raise AuthError(msg='Signature has expired')
        # except InvalidSignatureError:
        #     raise AuthError(msg='Invalid signature')

        return decode
    

    def create_access_token(self, sub: str) -> bytes:
        token = self.__create_token(
            subj = str(sub), 
            exp_time = datetime.now(tz=timezone.utc) + self.__access_ttl,
            type = 'access'
            )
    
        return token
    
    
    def create_refresh_token(self, sub: str) -> bytes:
        token = self.__create_token(
            subj = str(sub), 
            exp_time = datetime.now(tz=timezone.utc) + self.__refresh_ttl,
            type = 'refresh'
            )
    
        return token


    def get_jwt_subject(self, token: bytes) -> str:
        payload = self.__decode_token(token=token)
        
        return payload['sub']
    

    def is_refresh_token(self, token: str) -> bool:
        payload = self.__decode_token(token=token)
        return payload['type'] == 'refresh'
    

    def is_access_token(self, token: str) -> bool:
        payload = self.__decode_token(token=token)
        return payload['type'] == 'access'
