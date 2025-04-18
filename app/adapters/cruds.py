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

        @classmethod
        def _db_to_app_model(cls, db_model: DBUser) -> User:
            return User(
                userID=db_model.id,
                userName=db_model.name,
                userDescription=db_model.description,
                registerAt=db_model.create_at,
                extraPermissionIDs=[p.permission_id for p in db_model.permission_ids],
                adminedRoomIDs=[r.room_id for r in db_model.admined_room_ids],
                availableRoomIDs=[r.room_id for r in db_model.available_room_ids]
            )
        
        @classmethod
        @dbmanager.connection
        async def create_user(cls, session: AsyncSession, userName: str, registerAt: datetime, userDescription: str = None) -> User:
            dbuser = DBUser(name = userName, 
                            description = userDescription, 
                            create_at = registerAt)
            
            session.add(dbuser)
            await session.commit()
            dbuser = (await session.execute(select(DBUser).where(DBUser.id == dbuser.id))).scalars().first()

            user = cls._db_to_app_model(dbuser)
            return user


        @classmethod
        @dbmanager.connection
        async def get_user_by_id(cls, session: AsyncSession, user_id: int) -> User:
            query = select(DBUser).where(DBUser.id == user_id)

            result = await session.execute(query)

            record = result.scalars().first()

            return cls._db_to_app_model(record) if record else None


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

            return cls._db_to_app_model(new_user)


    return DBUserCrud



def get_DBAuth_CRUD(dbmanager: DBManager) -> IAuthCRUD:
    '''
    Фабрика для класса DBAuthCRUD
    '''
    class DBAuthCRUD(IAuthCRUD):

        @classmethod
        def _db_to_app_model(cls, db_model: DBAuthData) -> AuthData:
            return AuthData(
                userID=db_model.user_id,
                email=db_model.email,
                password=db_model.password
            )

        @classmethod
        @dbmanager.connection
        async def create_auth_data(cls, session: AsyncSession, userID: int, email: str, password: str) -> AuthData:
            dbauth = DBAuthData(
                user_id = userID,
                email = email,
                password = password
            )

            session.add(dbauth)

            await session.commit()

            return cls._db_to_app_model(dbauth)
        

        @classmethod
        @dbmanager.connection
        async def get_auth_data_by_user_id(cls, session: AsyncSession, user_id: int) -> AuthData:
            query = select(DBAuthData).where(DBAuthData.user_id == user_id)

            result = await session.execute(query)

            record = result.scalars().first()

            return cls._db_to_app_model(record)


        @classmethod
        @dbmanager.connection
        async def get_auth_data_by_email(cls, session: AsyncSession, email: str) -> AuthData:
            query = select(DBAuthData).where(DBAuthData.email == email)

            result = await session.execute(query)

            record = result.scalars().first()

            return cls._db_to_app_model(record)


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

            return cls._db_to_app_model(result)

    return DBAuthCRUD



def get_DBBuilding_CRUD(dbmanager: DBManager) -> IBuildingCRUD:
    '''
    Фабрика для класса DBAuthCRUD
    '''
    class DBBuildingCRUD(IBuildingCRUD):

        @classmethod
        def _db_to_app_model(cls, db_model: DBBuilding) -> Building:
            return Building(
                buildingID=db_model.id,
                buildingName=db_model.name,
                buildingDescription=db_model.description,
                unitIDs=[u.id for u in db_model.units],
                svg_schema=db_model.schema_uri,
                geopointRB=db_model.geopoint_rb,
                geopointLT=db_model.geopoint_lt
            )


        @classmethod
        @dbmanager.connection
        async def create_building(cls, session: AsyncSession,
                name: str,
                schema_uri: str,
                geopoint_lt: str,
                geopoint_rb: str,
                description: Optional[str] = None) -> Building:
            
            building = DBBuilding(
                name = name,
                description = description,
                schema_uri = schema_uri,
                geopoint_lt = geopoint_lt,
                geopoint_rb = geopoint_rb
            )

            session.add(building)
            await session.commit()

            dbbuilding = (await session.execute(select(DBBuilding).where(DBBuilding.id == building.id))).scalars().first()

            return cls._db_to_app_model(dbbuilding)
        
    return DBBuildingCRUD



def get_DBUnit_CRUD(dbmanager: DBManager) -> IUnitCRUD:
    '''
    Фабрика для класса DBAuthCRUD
    '''
    class DBUnitCRUD(IUnitCRUD):

        @classmethod
        def _db_to_app_model(cls, db_model: DBUnit) -> Unit:
            return Unit(
                unitID=db_model.id,
                unitName=db_model.name,
                unitDescription=db_model.description,
                floorIDs=[f.id for f in db_model.floors]
            )
        

        @classmethod
        @dbmanager.connection
        async def create_unit(cls, session: AsyncSession,
                name: str,
                building_id: int,
                description: Optional[str] = None) -> Unit:
            
            unit = DBUnit(
                name = name,
                description = description,
                building_id = building_id
            )

            session.add(unit)
            await session.commit()

            dbunit = (await session.execute(select(DBUnit).where(DBUnit.id == unit.id))).scalars().first()

            return cls._db_to_app_model(dbunit)
        
    return DBUnitCRUD



def get_DBFloor_CRUD(dbmanager: DBManager) -> IFloorCRUD:
    '''
    Фабрика для класса DBAuthCRUD
    '''
    class DBFloorCRUD(IFloorCRUD):

        @classmethod
        def _db_to_app_model(cls, db_model: DBFloor) -> Floor:
            return Floor(
                floorID=db_model.id,
                floorName=db_model.name,
                floorSequence=db_model.sequence,
                roomIDs=[r.id for r in db_model.rooms]
            )
        

        @classmethod
        @dbmanager.connection
        async def create_floor(cls, session: AsyncSession,
                name: str,
                sequence: int,
                unit_id: int) -> Floor:
            
            floor = DBFloor(
                name = name,
                sequence = sequence,
                unit_id = unit_id
            )

            session.add(floor)
            await session.commit()

            dbfloor = (await session.execute(select(DBFloor).where(DBFloor.id == floor.id))).scalars().first()

            return cls._db_to_app_model(dbfloor)
        
    return DBFloorCRUD



def get_DBRoom_CRUD(dbmanager: DBManager) -> IRoomCRUD:
    '''
    Фабрика для класса DBAuthCRUD
    '''
    class DBRoomCRUD(IRoomCRUD):

        @classmethod
        def _db_to_app_model(cls, db_model: DBRoom) -> Room:
            return Room(
                roomID=db_model.id,
                romName=db_model.name,
                roomDescription=db_model.description,
                floorID=db_model.floor_id
            )
        

        @classmethod
        @dbmanager.connection
        async def create_room(cls, session: AsyncSession,
                name: str,
                floor_id: int,
                description: Optional[str] = None) -> Room:
            
            room = DBRoom(
                name = name,
                description = description,
                floor_id = floor_id
            )
            
            session.add(room)
            await session.commit()

            dbroom = (await session.execute(select(DBRoom).where(DBRoom.id == room.id))).scalars().first()

            return cls._db_to_app_model(dbroom)
        
    return DBRoomCRUD
