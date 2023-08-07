#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
  def testPlace(self):
    obj_place = Place()
    self.assertIsNotNone(obj_Place.city_id, "city_id is None")
    self.assertIsNotNone(obj_place.user_id, "user_id is None")
    self.assertIsNotNone(obj_place.name, "name is None")
    self.assertIsNotNone(obj_place.description, "description is None")
    self.assertIsNotNone(obj_place.number_rooms, "number_rooms is None")
    self.assertIsNotNone(obj_place.numbers_bathrooms, "number_bathrooms is None")
    self.assertIsNotNone(obj_place.max_guest, "max_guest is None")
    self.assertIsNotNone(obj_place.price_by_night, "price_by_night is None")
    self.assertIsNotNone(obj_place.latitude, "latitude is None")
    self.assertIsNotNone(objplace.longitude, "longitude is None")
    self.assertIsInstance(obj_place.amenity_ids, list)
    self.assertEqual(len(obj_place.amenity_ids, 0) 
