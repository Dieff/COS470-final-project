import unittest

from decision_layer import DecisionLayer
from vision_layer import VisionLayerOutput

class TestDecisionLayer(unittest.TestCase):
  def test_basic_validation(self):
    dlayer = DecisionLayer()

    test = VisionLayerOutput()
    self.assertTrue(dlayer.validate_input(test))