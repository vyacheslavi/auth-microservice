from dependency_injector import providers
from dependency_injector.containers import (
    DeclarativeContainer,
    WiringConfiguration,
)

from ..common.settings import config
from ..infra.repositories.base import BaseDBRepository
from ..infra.repositories.db import DataBase
from ..infra.repositories.users import UserRepository
from .usecases.users import UserUseCase


class LogicContainer(DeclarativeContainer):

    wiring_config = WiringConfiguration(
        modules=[
            "..application.api.v1.handlers.auth",
        ],
    )

    db: DataBase = providers.Singleton(
        DataBase,
        url=config.settings.db.url,
        echo=config.settings.db.echo,
    )
    base_repository: BaseDBRepository = providers.Factory(
        BaseDBRepository,
        db=db,
    )
    user_repository: UserRepository = providers.Factory(
        UserRepository,
        db=db,
    )
    user_usecase: UserUseCase = providers.Factory(
        UserUseCase,
        user_repository=user_repository,
    )
