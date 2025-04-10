from core.usecases import (
    RegUser,
    UserLoginBasic,
    UserLoginRefresh,
    GetJWTSubject,
    GetUser
)

from adapters import get_DBAuth_CRUD, get_DBUser_CRUD, JWTManager

from database import DBManager
from config import conf



jwt_manager = JWTManager(
    key = conf.JWT_SECRET_KEY,
    access_ttl=conf.JWT_ACCESS_TTL,
    refersh_ttl=conf.JWT_REFRESH_TTL
)

db_manager = DBManager(conf.get_db_url())

auth_crud = get_DBAuth_CRUD(db_manager)
user_crud = get_DBUser_CRUD(db_manager)


RegUser.set_dependencies(user_crud=user_crud, auth_crud=auth_crud)
GetUser.set_dependencies(user_crud=user_crud)

UserLoginBasic.set_dependencies(auth_crud=auth_crud, jwt_manager=jwt_manager)
UserLoginRefresh.set_dependencies(auth_crud=auth_crud, jwt_manager=jwt_manager)
GetJWTSubject.set_dependencies(auth_crud=auth_crud, jwt_manager=jwt_manager)

