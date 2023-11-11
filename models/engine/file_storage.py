#!usr/bin/python3

""" File storage model """
import json
from models.base_model import BaseModel


class FileStorage:
    """File Storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """"
        serializes __objects to the JSON file (path: __file_path)
        """
        json_objs = {}
        for key, val in self.__objects.items():
            json_objs[key] = val.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(json_objs, f, indent=4)

    def reload(self):
        """
        Deserializes the JSON objects in file.json
        """
        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                json_objs = json.load(f)

            for key, val in json_objs.items():
                constractor = val["__class__"]
                if val["__class__"] in self.__models.keys():
                    self.__objects[key] = self.__models[val["__class__"]](
                        **val)
        except FileNotFoundError:
            pass
        except Exception as e:
            pass
