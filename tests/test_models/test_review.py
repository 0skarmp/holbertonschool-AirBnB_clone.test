#!/usr/bin/python3
import unittest
from models.review import Review
  
  
class TestReview(unittest.TestCase):
  def testPlaceId(self):
    obj_placeId = Review.place_id
    self.assertIsNotNone(obj_placeId, "place_id is None")

  def testUserId(self):
    obj_UserId = Review.user_id
    self.assertIsNotNone(obj_UserId, "user_id is None")

  def testText(self):
    obj_Text = Review.text
    self.assertIsNotNone(obj_Text, "text is None")
