#!/usr/bin/python3
"""defines the basemodel class"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Rep. the basemodel of the airbnb project
    """

    def __init__(self, *args, **kwargs):
        """
        initialize a new basemodel

        Args:
        *args
        **kwargs-key/value pairs of attributes
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

        def save(self):
            """
            update updated_at with the current datetime and save the instance
            """
            self.updated_at = datetime.today()
            models.storage.save()

        def to_dict(self):
            """
            return the dict of the basemodel instance
            """

            rdict = self.__dict__.copy()
            rdict["created_at"] = self.created_at.isoformat()
            rdict["updated_at"] = self.updated_at.isoformat()
            rdict["__class__"] = self.__class__.__name__
            return rdict

        def __str__(self):
            """
            return the print/str rep of the basemodel instance
            """
            clname = self.__class__.__name__
            return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
