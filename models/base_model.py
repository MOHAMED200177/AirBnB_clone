#!/usr/bin/python3
"""this is the base model."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """__init__.
        id :  unique ID
        created_at : Record the creation timestamp
        updated_at : Updated timestamp
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "updated_at":
                        self.updated_at = datetime.fromisoformat(value)
                    elif key == "created_at":
                        self.created_at = datetime.fromisoformat(value)
                    else:
                        setattr(self, key, value)

    def save(self):
        """save.

        update atr updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """__str__.

        return string Representation.
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def to_dict(self):
        """To_dict.

        Returns:
            dict: dictionary representation.
        """
        classDict = self.__dict__.copy()
        classDict["__class__"] = self.__class__.__name__
        classDict["created_at"] = self.created_at.isoformat()
        classDict["updated_at"] = self.updated_at.isoformat()
        return classDict
