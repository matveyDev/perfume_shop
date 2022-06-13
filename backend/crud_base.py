from typing import Generic, Optional, TypeVar

from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine, update
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

    def __init__(self, Model: ModelType) -> None:
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
        self.session.refresh(db_object)
        return db_object

    def update(self, jsonalbe_data: ModelType, update_data: UpdateSchemaType) -> ModelType:
        db_object = jsonable_encoder(jsonalbe_data)
        update_data = update_data.dict(skip_defaults=True)

        for field in update_data:
            setattr(db_object, field, update_data[field])

        self.session.execute(
            update(self.Model).
            where(self.Model.id == db_object.id).
            values(**db_object)
        )
        self.session.commit()
        self.session.refresh(db_object)
        return db_object

    def delete(self, id: int) -> ModelType:
        delete_object = self.session.query(self.Model).get(id)

        self.session.delete(delete_object)
        self.session.commit()
        return delete_object

    def __del__(self) -> None:
        self.session.close()
