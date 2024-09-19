from sqlalchemy import (
    Boolean,
    LargeBinary,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from .base import BaseModel


class UserORM(BaseModel):

    __tablename__ = "user"

    email: Mapped[str] = mapped_column(
        unique=True,
        index=True,
        nullable=False,
    )
    hashed_password: Mapped[str] = mapped_column(
        LargeBinary,
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
