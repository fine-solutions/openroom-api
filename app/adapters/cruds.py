from datetime import datetime

from sqlalchemy import select

from core.dependencies import IAuthCRUD, IUserCRUD
from core.entities import User, AuthData

from database import DBManager, AsyncSession
from database.tables import User as DBUser, AuthData as DBAuthData

from dependencies import db_manager



class DBUserCrud(IUserCRUD):
    
    @classmethod
    @db_manager.connection
    async def create_user(cls, session: AsyncSession, userName: str, registerAt: datetime, userDescription: str = None):
        dbuser = DBUser(name = userName, 
                        description = userDescription, 
                        create_at = registerAt)
        
        session.add(dbuser)
        await session.commit()

        return User(
            userID=dbuser.id,
            userName=dbuser.name,
            userDescription=dbuser.description,
            registerAt=dbuser.create_at,
            extraPermissionIDs=[],
            adminedRoomIDs=[],
            availableRoomIDs=[]
        )


    @classmethod
    @db_manager.connection
    async def get_user_by_id(self, session: AsyncSession, user_id: int) -> User:
        query = select(DBUser).where(DBUser.id == user_id)

        result = await session.execute(query)

        record = result.scalar_one_or_none()

        return User(
            userID=record.id,
            userName=record.name,
            userDescription=record.description,
            registerAt=record.create_at,
            extraPermissionIDs=[],
            adminedRoomIDs=[],
            availableRoomIDs=[]
        ) if record else None


    async def delete_user_by_id(self, user_id):
        pass 


    async def update_user(self, user):
        pass



class DBAuthCRUD(IAuthCRUD):

    @classmethod
    @db_manager.connection
    async def create_auth_data(cls, session: AsyncSession, userID: int, email: str, password: str) -> AuthData:
        dbauth = DBAuthData(
            user_id = userID,
            email = email,
            password = password
        )

        session.add(dbauth)

        await session.commit()

        return AuthData(
            userID=dbauth.user_id,
            email=dbauth.email,
            password=dbauth.password
        )
    

    async def get_auth_data_by_user_id(self, user_id: int):
        pass


    async def delete_auth_data_by_user_id(self, user_id):
        pass 


    async def update_auth_data_by_user_id(self, auth_data):
        pass
