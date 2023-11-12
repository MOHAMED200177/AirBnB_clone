#!/usr/bin/python3
"""this is the unittest for base model."""
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    test class
    """
    base = BaseModel()  # Create a new instance for each test
    base.name = "My First Model"
    base.my_number = 89

    def test_init(self):
        """
        create an instance of class without kwargs
        """
        self.assertIsInstance(self.base, BaseModel)
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)
        self.assertEqual(self.base.name, "My First Model")
        self.assertEqual(self.base.my_number, 89)

    def test_create_instance_with_kwargs(self):
        """
        create an instance of class using kwargs
        """
        my_base_json = self.base.to_dict()
        new_base = BaseModel(**my_base_json)
        self.assertIsInstance(new_base, BaseModel)
        self.assertIsInstance(new_base.id, str)
        self.assertIsInstance(new_base.created_at, datetime)
        self.assertIsInstance(new_base.updated_at, datetime)
        self.assertEqual(new_base.name, "My First Model")
        self.assertEqual(new_base.my_number, 89)
        self.assertNotEqual(new_base, self.base)
        self.assertDictEqual(new_base.__dict__, self.base.__dict__)

    def test_save(self):
        """"
        test save class method
        """
        initail_updated_at = self.base.updated_at
        self.base.save()
        current_updated_at = self.base.updated_at
        self.assertNotEqual(initail_updated_at, current_updated_at)

    def test_to_dict(self):
        """
            test to_dict class method
        """
        to_dict_cp = self.base.to_dict()
        test_dic = self.base.__dict__.copy()
        test_dic["__class__"] = self.base.__class__.__name__
        test_dic["updated_at"] = self.base.updated_at.isoformat()
        test_dic["created_at"] = self.base.created_at.isoformat()
        self.assertDictEqual(test_dic, to_dict_cp)

    def test_str(self):
        """
            test str method

            check for string representaion
        """
        class_name = self.base.__class__.__name__
        test_str = f"[{class_name}] ({self.base.id}) <{self.base.__dict__}>"
        self.assertEqual(self.base.__str__(), test_str)
