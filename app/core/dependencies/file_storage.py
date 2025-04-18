from abc import ABC, abstractmethod
from typing import BinaryIO, AsyncGenerator



class IFileStorage(ABC):

    @abstractmethod
    async def save_file(file: BinaryIO) -> str:
        pass 

    @abstractmethod
    async def get_file_by_id(id: str) -> AsyncGenerator[BinaryIO, None]:
        pass
