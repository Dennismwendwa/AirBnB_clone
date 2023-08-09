from models.engine.file_storage import FileStorage
"""
Here we are ensureing any saved instances are being reloaded
When the program starts.
"""


storage = FileStorage()
storage.reload()
