from typing import AsyncGenerator, BinaryIO
from contextlib import asynccontextmanager
from uuid import uuid4
import os

import aiofiles 

from core.dependencies import IFileStorage



class OsFileStorage(IFileStorage):
    def __init__(self, os_storage_path: str):
        self.spath: str = os_storage_path
        
        if not os.path.exists(os_storage_path):
            os.mkdir(os_storage_path)


    async def save_file(self, file: BinaryIO, filename: str) -> str:
        '''
        Сохраняет файл в файловом хранилище, возвращает имя файла
        '''
        file_id = uuid4()
        file_ext = filename.split('.')[-1]

        async with aiofiles.open(f'{self.spath}/{file_id}.{file_ext}', 'wb') as f:
            await f.write(await file.read())
            await f.seek(0)
        
        return f'{file_id}.{file_ext}'
    

    @asynccontextmanager
    async def get_file_by_id(self, file_name: str) -> AsyncGenerator[BinaryIO, None]:
        try:
            async with aiofiles.open(f'{self.spath}/{file_name}', 'rb') as f:
                yield f 
        finally:
            pass
