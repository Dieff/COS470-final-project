import unittest

from rule_layer import RuleLayer
from vision_layer import VisionLayerOutput

class TestDecisionLayer(unittest.TestCase):
  def test_basic_validation(self):
    rlayer = RuleLayer()

    test = VisionLayerOutput()
    self.assertTrue(rlayer.validate_input(test))