from typing import Any
from abc import ABC, abstractmethod

from pydantic import BaseModel



class BaseUC(ABC, BaseModel):

    @classmethod
    @abstractmethod
    def set_dependencies(cls, **kwargs) -> 'BaseUC':
        """
        Установка зависимостей, которыми будут пользоваться все экземпляры класса
        """
        pass


    @abstractmethod
    async def execute(self) -> Any:
        """
        Выполнить сценарий
        """
        pass 
