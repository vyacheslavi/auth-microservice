from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncSession,
    create_async_engine,
)


class DataBase:

    def __init__(self, url, echo) -> None:
        self._engine = create_async_engine(
            url=url,
            echo=echo,
        )

        self._session_factory = async_sessionmaker(
            bind=self._engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    @asynccontextmanager
    async def session(self):
        session: AsyncSession = self._session_factory()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
