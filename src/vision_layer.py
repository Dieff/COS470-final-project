from dataclasses import dataclass

from layer import Layer

@dataclass
class VisionLayerOutput:
  max_health = 10
  min_health = 10
  cur_menu = "MaxMove"


class VisionLayer(Layer):

  def validate_input(self, input):
    return True
  
  def run_layer(self):
    return VisionLayerOutput()
