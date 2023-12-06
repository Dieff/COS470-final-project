from dataclasses import dataclass

from vision_layer import VisionLayerOutput
from layer import Layer

class RuleLayer(Layer):
  cur_input = None
  cur_goal = "MOVE"

  def validate_input(self, input):
    if not(isinstance(input, VisionLayerOutput)):
      return False
    self.cur_input = input
    return True

  