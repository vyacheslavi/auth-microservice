from ...domain.users.schemas import UserCreateSchema
from ...infra.repositories.users import UserRepository


class UserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def register_user(self, user_data: UserCreateSchema):
        await self.user_repository.create(user_data)
