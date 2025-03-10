import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine, AsyncSession

from database.tables import Base



class DBManager():
    def __init__(self, url: str):
        self.engine = create_async_engine(url)
        self.session_maker = async_sessionmaker(self.engine, expire_on_commit=False)
        self.base = Base


    async def db_init(self) -> None:
        """
        Метод для инициализации структуры БД
        """
        async with self.engine.begin() as conn:
            await conn.run_sync(self.base.metadata.create_all)


    def connection(self, method):
        """
        Декоратор для управления сессиями
        """
        async def wrapper(*args, **kwargs):
            async with self.session_maker() as session:
                try:
                    # Явно не открываем транзакции, так как они уже есть в контексте
                    return await method(*args, session=session, **kwargs)
                except Exception as e:
                    await session.rollback()  # Откатываем сессию при ошибке
                    raise e  # Поднимаем исключение дальше
                finally:
                    await session.close()  # Закрываем сессию

        return wrapper
