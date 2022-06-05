from . import schemas
from fastapi import UploadFile
import shutil
import uuid

def generate_image_file_name():
    return str(uuid.uuid4())

def form_dict_create_post_file_name(request: schemas.CreatePost):
    photo_file_name = generate_image_file_name()
    fields = request.dict()
    fields['photo_url'] = photo_file_name
    return fields, photo_file_name
    

def create_photo_file(photo_file_name: str, photo: UploadFile):
    with open(f'app/staticfile/{photo_file_name}', 'wb') as buffer:
        shutil.copyfileobj(photo.file, buffer)
