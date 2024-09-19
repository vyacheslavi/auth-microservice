from fastapi import (
    Depends,
    status,
)
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from dependency_injector.wiring import (
    inject,
    Provide,
)

from .....domain.users.schemas import UserCreateSchema
from .....infra.repositories.exceptions.users import UserAlreadyExist
from .....logic.containers import LogicContainer
from .....logic.usecases.users import UserUseCase


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register")
@inject
async def register(
    user_data: UserCreateSchema,
    uc: UserUseCase = Depends(Provide[LogicContainer.user_usecase]),
):
    try:
        await uc.register_user(user_data)
    except UserAlreadyExist as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error
