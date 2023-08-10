<<<<<<< HEAD
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
=======
#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
>>>>>>> 9bd7c0c77cb1feeac064e2bc88b8994c0e77a935
