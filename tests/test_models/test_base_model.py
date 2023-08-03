#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_models import BaseModel


class TestBaseModel(unittest.TestCase):
    """ TestCase test_init method """
    def test__init__(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test__str__(self):
        obj = BaseModel()
        result_obj = str(obj)
        string_text = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(result_obj, string_text)

    def test_save(self):
        obj = BaseModel()
        obj_updated1 = obj.updated_at

        obj.save()
        obj_updated2 = obj.updated_at

        self.assertNotEqual(obj_updated1, obj_updated2)

    def test_to_dict(self):
        obj = BaseModel()
        expected_dict = {
                'id': obj.id,
                'created_at': obj.created_at.isoformat(),
                'updated_at': obj.updated_at.isoformat(),
                '__class__': "BaseModel"
                }

        obj_dict = obj.to_dict()
        self.assertDictEqual(obj_dict, expected_dict) 

if __name__ == '__main__':
    unittest.main()
