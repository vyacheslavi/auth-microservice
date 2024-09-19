from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
)


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserCreateSchema(UserBase):
    pass


class UserUpdateSchema(UserBase):
    pass


class UserResponseSchema(UserBase):

    model_config = ConfigDict(from_attributes=True)

    id: int  # noqa
    is_active: bool
    is_superuser: bool
    is_verified: bool
