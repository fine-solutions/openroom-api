from database import DBManager
from config import conf

db_manager = DBManager(conf.get_db_url())
