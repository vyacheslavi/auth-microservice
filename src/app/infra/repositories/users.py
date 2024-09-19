from sqlalchemy import select

from ...domain.users.schemas import (
    UserCreateSchema,
    UserResponseSchema,
    UserUpdateSchema,
)
from ..models import UserORM
from .base import BaseDBRepository
from .exceptions.users import UserAlreadyExist


class UserRepository(
    BaseDBRepository[UserCreateSchema, UserUpdateSchema, UserResponseSchema, UserORM],
):
    @property
    def _table(self) -> UserORM:
        return UserORM

    @property
    def _encode(self, entry: UserORM) -> UserResponseSchema:
        return UserResponseSchema.model_validate(entry)

    async def get_by_email(
        self,
        email: str,
    ) -> UserORM | None:
        async with self.db_session as session:
            stmt = select(UserORM).where(UserORM.email == email)
            return await session.scalar(stmt)

    async def create(
        self,
        user_data: UserCreateSchema,
    ):
        if await self.get_by_email(user_data.email) is None:
            await super().create(user_data)
        else:
            raise UserAlreadyExist(user_data.email)
