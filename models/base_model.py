#!/usr/bin/python3
"""
This is the base class where all other classes will inherite from
Its the blue print of all classes
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """This are the attributes and methods of this class"""
    def __init__(self, *args, **kwargs):
        """THis is the contractor method of the base class."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(
                            self,
                            key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                                )
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        models.storage.new(self)

    def __str__(self):
        """This method returns the string representation of the object"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        """This method updates the last updated_at atrribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        This method returns objects of the objects attributes after seriazation
        """
        obj_dict = self.__dict__.copy()

        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict
