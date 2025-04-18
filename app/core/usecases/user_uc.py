from typing import Optional, Dict
from datetime import datetime

from core.usecases import BaseUC
from core.entities import AuthData, User
from core.dependencies import IUserCRUD, IAuthCRUD



class RegUser(BaseUC):
    """
    Зарегистрировать пользователя в системе
    """
    userName: str
    email: str
    password: str
    userDescription: Optional[str] = None
    _user_crud: IUserCRUD
    _auth_crud: IAuthCRUD


    @classmethod
    def set_dependencies(cls, user_crud: IUserCRUD, auth_crud: IAuthCRUD) -> 'RegUser':
        cls._user_crud = user_crud
        cls._auth_crud = auth_crud
        return cls
    
    
    async def execute(self) -> User:
        user = await self._user_crud.create_user(
            userName=self.userName,
            registerAt=datetime.now(),
            userDescription=self.userDescription
        )

        await self._auth_crud.create_auth_data(
            userID=user.userID,
            email=self.email,
            password=self.password
        )

        return user



class GetUser(BaseUC):
    """
    Получить профиль пользователя
    """
    userID: int
    _user_crud: IUserCRUD


    @classmethod
    def set_dependencies(cls, user_crud: IUserCRUD) -> 'GetUser':
        cls._user_crud = user_crud
        return cls
    
    
    async def execute(self) -> User:
        user = await self._user_crud.get_user_by_id(
            user_id=self.userID
        )

        if user: 
            return user
        else: 
            raise



class EditUser(BaseUC):
    """
    Редактировать профиль пользователя
    """
    userID: int 
    userName: Optional[str]
    userDescription: Optional[str]
    email: Optional[str]
    password: Optional[str]

    _user_crud: IUserCRUD
    _auth_crud: IAuthCRUD

    @classmethod
    def set_dependencies(cls, user_crud: IUserCRUD, auth_crud: IAuthCRUD) -> 'EditUser':
        cls._user_crud = user_crud
        cls._auth_crud = auth_crud
        return cls
    
    
    async def execute(self) -> User:
        user = await self._user_crud.get_user_by_id(user_id=self.userID)
        auth_data = await self._auth_crud.get_auth_data_by_user_id(user_id=self.userID)

        if not user or not auth_data:
            raise

        user.userName = self.userName
        user.userDescription = self.userDescription
        auth_data.email = self.email
        auth_data.password = self.password

        await self._auth_crud.update_auth_data(auth_data=auth_data)
        return await self._user_crud.update_user(user=user)
