from fastapi import HTTPException, status
from fastapi import UploadFile
import shutil
import uuid
import os.path


class Photo:
    STATIC_FILE_URL = 'app/staticfile'

    @classmethod
    def create(cls, photo: UploadFile):
        def generate_file_name():
            return str(uuid.uuid4())

        file_name = generate_file_name()
        if cls._file_exist(file_name):
            raise HTTPException(status_code=status.HTTP_510_NOT_EXTENDED,
                                detail='file with generated name already exist')
        with open(f'{cls.STATIC_FILE_URL}/{photo.file.name}', 'wb') as buffer:
            shutil.copyfileobj(photo.file, buffer)
        return file_name

    @classmethod
    def get_full_path(cls, url: str):
        if cls._file_exist(url):
            return f'{cls.STATIC_FILE_URL}/{url}'
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid photo url')

    @classmethod
    def _file_exist(cls, url: str):
        return os.path.isfile(f'{cls.STATIC_FILE_URL}/{url}')
