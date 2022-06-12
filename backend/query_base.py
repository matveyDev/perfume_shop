from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from database.local_db import SQLALCHEMY_DATABASE_URL


class BaseQueries:
    def __init__(self):
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        self.session = Session(engine)
