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
    async def save_user(
            self,
            user: User) -> User:
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
    async def save_auth_data(
            self,
            auth_data: AuthData) -> AuthData:
        pass 

    @abstractmethod
    async def delete_auth_data_by_user_id(self, user_id: int) -> None:
        pass 

    @abstractmethod
    async def update_auth_data(self, auth_data: AuthData) -> AuthData:
        pass



class IBuildingCRUD():

    @abstractmethod
    async def save_building(self, building: Building) -> Building:
        pass
        
    @abstractmethod
    async def get_building_by_id(building_id: int) -> Building:
        pass



class IUnitCRUD():

    @abstractmethod
    async def save_unit(self, unit: Unit) -> Unit:
        pass



class IFloorCRUD():

    @abstractmethod
    async def save_floor(self, floor: Floor) -> Floor:
        pass



class IRoomCRUD():

    @abstractmethod
    async def save_room(self, room: Room) -> Room:
        pass
