from datetime import datetime
from typing import Optional

from sqlalchemy import select, update

from core.dependencies import IAuthCRUD, IUserCRUD, IBuildingCRUD, IUnitCRUD, IFloorCRUD, IRoomCRUD
from core.entities import User, AuthData, Building, Unit, Floor, Room

from database import DBManager, AsyncSession
from database.tables import (
    User as DBUser, 
    AuthData as DBAuthData,
    Building as DBBuilding,
    Unit as DBUnit,
    Floor as DBFloor,
    Room as DBRoom)



def get_DBUser_CRUD(dbmanager: DBManager) -> IUserCRUD:
    '''
    Фабрика для класса DBUserCRUD
    '''

    class DBUserCrud(IUserCRUD):
        
        # @classmethod
        # @dbmanager.connection
        # async def create_user(cls, session: AsyncSession, userName: str, registerAt: datetime, userDescription: str = None) -> User:
        #     dbuser = DBUser(name = userName, 
        #                     description = userDescription, 
        #                     create_at = registerAt)
            
        #     session.add(dbuser)
        #     await session.commit()
        #     dbuser = (await session.execute(select(DBUser).where(DBUser.id == dbuser.id))).scalars().first()

        #     return dbuser.db_to_app_model()

        @classmethod
        @dbmanager.connection
        async def save_user(cls, session: AsyncSession, user: User) -> User:
            dbuser = DBUser.from_app_model(user)
            
            session.add(dbuser)
            await session.commit()
            dbuser = (await session.execute(select(DBUser).where(DBUser.id == dbuser.id))).scalars().first()

            return dbuser.db_to_app_model()


        @classmethod
        @dbmanager.connection
        async def get_user_by_id(cls, session: AsyncSession, user_id: int) -> User:
            query = select(DBUser).where(DBUser.id == user_id)

            result = await session.execute(query)

            record = result.scalars().first()

            return record.db_to_app_model()


        async def delete_user_by_id(self, user_id) -> None:
            pass 


        @classmethod
        @dbmanager.connection
        async def update_user(cls, session: AsyncSession, user: User) -> User:
            if not user.userID:
                raise 

            query = update(DBUser).where(DBUser.id == user.userID).values(
                name = user.userName,
                description = user.userDescription
            )

            await session.execute(query)
            await session.commit()

            new_user = await session.get(DBUser, user.userID)

            return new_user.db_to_app_model()


    return DBUserCrud



def get_DBAuth_CRUD(dbmanager: DBManager) -> IAuthCRUD:
    '''
    Фабрика для класса DBAuthCRUD
    '''
    class DBAuthCRUD(IAuthCRUD):

        @classmethod
        @dbmanager.connection
        async def save_auth_data(cls, session: AsyncSession, auth_data: AuthData) -> AuthData:
            dbauth = DBAuthData.from_app_model(auth_data)

            session.add(dbauth)

            await session.commit()

            return dbauth.db_to_app_model()
        

        @classmethod
        @dbmanager.connection
        async def get_auth_data_by_user_id(cls, session: AsyncSession, user_id: int) -> AuthData:
            query = select(DBAuthData).where(DBAuthData.user_id == user_id)

            result = await session.execute(query)

            record = result.scalars().first()

            return record.db_to_app_model()


        @classmethod
        @dbmanager.connection
        async def get_auth_data_by_email(cls, session: AsyncSession, email: str) -> AuthData:
            query = select(DBAuthData).where(DBAuthData.email == email)

            result = await session.execute(query)

            record = result.scalars().first()

            return record.db_to_app_model()


        async def delete_auth_data_by_user_id(self, user_id):
            pass 


        @classmethod
        @dbmanager.connection
        async def update_auth_data(cls, session: AsyncSession, auth_data: AuthData) -> AuthData:
            if not auth_data.userID:
                raise 

            query = update(DBAuthData).where(DBAuthData.user_id == auth_data.userID).values(
                email = auth_data.email,
                password = auth_data.password
            ).returning(DBAuthData)

            result = (await session.scalars(query)).first()

            return result.db_to_app_model()

    return DBAuthCRUD



def get_DBBuilding_CRUD(dbmanager: DBManager) -> IBuildingCRUD:
    '''
    Фабрика для класса DBAuthCRUD
    '''
    class DBBuildingCRUD(IBuildingCRUD):

        @classmethod
        @dbmanager.connection
        async def save_building(cls, session: AsyncSession, building: Building) -> Building:
            
            dbbuilding = DBBuilding.from_app_model(building)

            session.add(dbbuilding)
            await session.commit()

            dbbuilding = (await session.execute(select(DBBuilding).where(DBBuilding.id == dbbuilding.id))).scalars().first()

            return dbbuilding.db_to_app_model()
        

        @classmethod
        @dbmanager.connection
        async def get_building_by_id(cls, session: AsyncSession, building_id: int) -> Building:
            query = select(DBBuilding).where(DBBuilding.id == building_id)

            result = await session.execute(query)

            record = result.scalars().first()

            return record.db_to_app_model()
        
    return DBBuildingCRUD



def get_DBUnit_CRUD(dbmanager: DBManager) -> IUnitCRUD:
    '''
    Фабрика для класса DBAuthCRUD
    '''
    class DBUnitCRUD(IUnitCRUD):

        @classmethod
        @dbmanager.connection
        async def save_unit(cls, session: AsyncSession, unit: Unit) -> Unit:
            
            dbunit = DBUnit.from_app_model(unit)

            session.add(dbunit)
            await session.commit()

            dbunit = (await session.execute(select(DBUnit).where(DBUnit.id == dbunit.id))).scalars().first()

            return dbunit.db_to_app_model()
        
    return DBUnitCRUD



def get_DBFloor_CRUD(dbmanager: DBManager) -> IFloorCRUD:
    '''
    Фабрика для класса DBAuthCRUD
    '''
    class DBFloorCRUD(IFloorCRUD):

        @classmethod
        @dbmanager.connection
        async def save_floor(cls, session: AsyncSession, floor: Floor) -> Floor:
            
            dbfloor = DBFloor.from_app_model(floor)

            session.add(dbfloor)
            await session.commit()

            dbfloor = (await session.execute(select(DBFloor).where(DBFloor.id == dbfloor.id))).scalars().first()

            return dbfloor.db_to_app_model()
        
    return DBFloorCRUD



def get_DBRoom_CRUD(dbmanager: DBManager) -> IRoomCRUD:
    '''
    Фабрика для класса DBAuthCRUD
    '''
    class DBRoomCRUD(IRoomCRUD):
        
        @classmethod
        @dbmanager.connection
        async def save_room(cls, session: AsyncSession, room: Room) -> Room:
            
            dbroom = DBRoom.from_app_model(room)
            
            session.add(dbroom)
            await session.commit()

            dbroom = (await session.execute(select(DBRoom).where(DBRoom.id == dbroom.id))).scalars().first()

            return dbroom.db_to_app_model()
        
    return DBRoomCRUD
