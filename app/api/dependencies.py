from core.usecases import (
    RegUser,
    UserLoginBasic,
    UserLoginRefresh,
    GetJWTSubject,
    GetUser,
    EditUser,
    InitBuilding
)

from adapters import (
    get_DBAuth_CRUD, 
    get_DBUser_CRUD, 
    get_DBBuilding_CRUD,
    get_DBUnit_CRUD,
    get_DBFloor_CRUD,
    get_DBRoom_CRUD,
    JWTManager,
    OsFileStorage
)

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
building_crud = get_DBBuilding_CRUD(db_manager)
unit_crud = get_DBUnit_CRUD(db_manager)
floor_crud = get_DBFloor_CRUD(db_manager)
room_crud = get_DBRoom_CRUD(db_manager)

file_torage = OsFileStorage('D:\VSU\Diplom\openroom-api\store')


RegUser.set_dependencies(user_crud=user_crud, auth_crud=auth_crud)
GetUser.set_dependencies(user_crud=user_crud)
EditUser.set_dependencies(user_crud=user_crud, auth_crud=auth_crud)

UserLoginBasic.set_dependencies(auth_crud=auth_crud, jwt_manager=jwt_manager)
UserLoginRefresh.set_dependencies(auth_crud=auth_crud, jwt_manager=jwt_manager)
GetJWTSubject.set_dependencies(auth_crud=auth_crud, jwt_manager=jwt_manager)

InitBuilding.set_dependencies(building_crud=building_crud, unit_crud=unit_crud, floor_crud=floor_crud, room_crud=room_crud, file_storage=file_torage)
