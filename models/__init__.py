from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
"""
Here we are ensureing any saved instances are being reloaded
When the program starts.
"""


storage = FileStorage()
storage.reload()

"""This is dictionary maps class names to their class objects"""
classes = {
        "BaseModel": BaseModel,
        }
