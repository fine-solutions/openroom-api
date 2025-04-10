from datetime import datetime
from typing import Optional
from abc import ABC, abstractmethod

from core.entities import User, AuthData



class IUserCRUD(ABC):
    def __init__(self):
        pass

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    async def create_user(
            self,
            userName: str, 
            registerAt: datetime,
            userDescription: Optional[str] = None) -> User:
        pass 

    @abstractmethod
    async def delete_user_by_id(self, user_id: int) -> None:
        pass 

    @abstractmethod
    async def update_user(self, user: User) -> User:
        pass



class IAuthCRUD(ABC):
    def __init__(self):
        pass

    @abstractmethod
    async def get_auth_data_by_user_id(self, user_id: int) -> AuthData:
        pass

    @abstractmethod
    async def get_auth_data_by_email(self, email: str) -> AuthData:
        pass

    @abstractmethod
    async def create_auth_data(
            self,
            userID: str, 
            email: datetime,
            password: Optional[str] = None) -> AuthData:
        pass 

    @abstractmethod
    async def delete_auth_data_by_user_id(self, user_id: int) -> None:
        pass 

    @abstractmethod
    async def update_auth_data_by_user_id(self, auth_data: AuthData) -> AuthData:
        pass
