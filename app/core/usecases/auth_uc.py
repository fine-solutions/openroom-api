from typing import Optional, Dict
from datetime import datetime

from core.usecases import BaseUC
from core.dependencies import IAuthCRUD, IJWTManager



class UserLoginBasic(BaseUC):
    """
    Получить access и refresh токены по учётным данным пользователя
    """
    email: str
    password: str


    @classmethod
    def set_dependencies(cls, auth_crud: IAuthCRUD, jwt_manager: IJWTManager) -> 'UserLoginBasic':
        cls._auth_crud = auth_crud
        cls.jwt = jwt_manager
        return cls
    
    
    async def execute(self) -> Dict[str, bytes]:
        auth_data = await self._auth_crud.get_auth_data_by_email(email=self.email)

        if auth_data is None:
            raise

        if auth_data.password != self.password:
            raise

        access = self.jwt.create_access_token(auth_data.userID)
        refresh = self.jwt.create_refresh_token(auth_data.userID)

        return {
            'access_token': access,
            'refresh_token': refresh
        }



class UserLoginRefresh(BaseUC):
    """
    Обновить токены по refresh токену пользователя
    """
    refresh_token: str


    @classmethod
    def set_dependencies(cls, auth_crud: IAuthCRUD, jwt_manager: IJWTManager) -> 'UserLoginRefresh':
        cls._auth_crud = auth_crud
        cls.jwt = jwt_manager
        return cls
    
    
    async def execute(self) -> Dict[str, bytes]:
        if not self.jwt.is_refresh_token(self.refresh_token):
            raise

        user_id = int(self.jwt.get_jwt_subject(self.refresh_token))

        auth_data = await self._auth_crud.get_auth_data_by_user_id(user_id=user_id)

        if auth_data is None:
            raise

        access = self.jwt.create_access_token(auth_data.userID)
        refresh = self.jwt.create_refresh_token(auth_data.userID)

        return {
            'access_token': access,
            'refresh_token': refresh
        }



class GetJWTSubject(BaseUC):
    """
    Получить user_id по access токену пользователя
    """
    access_token: bytes


    @classmethod
    def set_dependencies(cls, auth_crud: IAuthCRUD, jwt_manager: IJWTManager) -> 'GetJWTSubject':
        cls._auth_crud = auth_crud
        cls.jwt = jwt_manager
        return cls
    
    
    async def execute(self) -> Dict[str, bytes]:
        if not self.jwt.is_access_token(self.access_token):
            raise

        user_id = int(self.jwt.get_jwt_subject(self.access_token))
        auth_data = await self._auth_crud.get_auth_data_by_user_id(user_id=user_id)

        if auth_data is None:
            raise

        return user_id
