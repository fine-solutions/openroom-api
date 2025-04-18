from datetime import datetime
from typing import Optional
from abc import ABC, abstractmethod

from core.entities import Floor, User, AuthData, Building, Unit, Floor, Room



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
    async def update_auth_data(self, auth_data: AuthData) -> AuthData:
        pass



class IBuildingCRUD():

    @abstractmethod
    async def create_building(
            name: str,
            schema_uri: str,
            geopoint_lt: str,
            geopoint_rb: str,
            description: Optional[str] = None) -> Building:
        pass



class IUnitCRUD():

    @abstractmethod
    async def create_unit(
            name: str,
            building_id: int,
            description: Optional[str] = None) -> Unit:
        pass



class IFloorCRUD():

    @abstractmethod
    async def create_floor(
            name: str,
            sequence: int,
            unit_id: int) -> Floor:
        pass



class IRoomCRUD():

    @abstractmethod
    async def create_room(
            name: str,
            floor_id: int,
            description: Optional[str] = None) -> Room:
        pass
