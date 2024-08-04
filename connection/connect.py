from mongoengine import connect

from config import config


def get_connection():

    uri = config.uri
    db_name = config.POSTGRES_NAME

    return connect(db=db_name, host=uri)

