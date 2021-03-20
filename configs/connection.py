import databases
import sqlalchemy
from functools import lru_cache
from configs import dbinfo
from db.table import metadata

@lru_cache()
def db_config():
    return dbinfo.Setting()

def DATABASE_URL(
    connection: str = db_config().db_connection,
    username: str   = db_config().db_username,
    password: str   = db_config().db_password,
    host: str       = db_config().db_host,
    port: str       = db_config().db_port,
    database: str   = db_config().db_database
):
    return str(connection+"://"+username+":"+password+"@"+host+":"+port+"/"+database)

database = databases.Database(DATABASE_URL())

engine = sqlalchemy.create_engine(
    DATABASE_URL()
)

metadata.create_all(engine)