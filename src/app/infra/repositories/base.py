from abc import ABC
from contextlib import asynccontextmanager
from typing import (
    Generic,
    TypeVar,
)

from pydantic import BaseModel

from ..models import BaseModel as Base
from .db import DataBase


CREATE_SCHEMA = TypeVar("CREATE_SCHEMA", bound=BaseModel)
UPDATE_SCHEMA = TypeVar("UPDATE_SCHEMA", bound=BaseModel)
RESPONSE_SCHEMA = TypeVar("RESPONSE_SCHEMA", bound=BaseModel)
TABLE = TypeVar("TABLE", bound=Base)


class BaseDBRepository(
    ABC,
    Generic[CREATE_SCHEMA, UPDATE_SCHEMA, RESPONSE_SCHEMA, TABLE],
):

    def __init__(self, db: DataBase) -> None:
        self.db: DataBase = db

    @property
    def db_session(self):
        return self._get_session()

    @asynccontextmanager
    async def _get_session(self):
        async with self.db.session() as session:
            yield session

    @property
    def _table(self) -> TABLE: ...

    def _encode(self, entry: TABLE) -> RESPONSE_SCHEMA: ...

    async def get_by_id(self, id: int) -> RESPONSE_SCHEMA: # noqa
        if not (entry := await self.db_session.get(self._table, id=id)):
            raise ValueError(f"{self._table().__name__}<id:{id}> does not exist")
        return self._encode(entry)

    async def create(self, data: CREATE_SCHEMA) -> RESPONSE_SCHEMA:
        async with self.db_session as session:
            odject_to_db = self._table(**data.model_dump())
            session.add(odject_to_db)
            await session.commit()

    async def update(self, id: int, data: UPDATE_SCHEMA) -> RESPONSE_SCHEMA: # noqa
        pass

    async def delete(self, id: int) -> None: # noqa
        pass
