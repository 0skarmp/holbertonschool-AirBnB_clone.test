#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def testState(self):
      obj_state = State.name
      self.assertIsNotNone(obj_state, "name is None")
