from typing import Generic, Optional, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from database.db import Base
from database.local_db import SQLALCHEMY_DATABASE_URL

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=Base)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=Base)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    You should inherit from this class to your current CRUDClass

    Attributes:
        model: Model from models.py
    """

    def __init__(self, Model: Type(ModelType)) -> None:
        self.Model = Model
        self.session = Session(
            create_engine(SQLALCHEMY_DATABASE_URL)
        )

    def get(self, id: int) -> Optional[ModelType]:
        self.session.query(self.Model).get(id)

    def create(self, jsonalbe_data: CreateSchemaType) -> ModelType:
        data = jsonable_encoder(jsonalbe_data)
        db_object = self.Model(**data)

        self.session.add(db_object)
        self.session.commit()
        self.session.refresh()
        return db_object

    def update(self):
        pass

    def delete(self):
        pass

    def __del__(self) -> None:
        self.session.close()
