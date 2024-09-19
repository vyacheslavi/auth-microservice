from sqlalchemy import MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)
from sqlalchemy.sql import func


class BaseModel(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        },
    )

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa
    updated_at: Mapped[str] = mapped_column(
        server_default=func.now(),
        nullable=False,
        onupdate=func.now(),
    )
    created_at: Mapped[str] = mapped_column(
        server_default=func.now(),
        nullable=False,
    )
