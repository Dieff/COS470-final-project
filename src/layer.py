from logging import info, warning

class Layer:
  """
    A base class for all layers
    besides the i/o ones.
    Each layer takes a previous state layer's
    output and emits a new one. 
  """

  def validate_input(self, input):
    raise NotImplementedError()
  
  def run_layer(self):
    raise NotImplementedError()
  
  def __repr__(self) -> str:
    return f"{self.__class__.__name__}"


class LayerSet:
  def __init__(self, layers: list[Layer]):
    self.layers = layers

  def run(self):
    cur_output = None

    for layer in self.layers:
      # skip layer?

      # check that last output is valid
      if not(layer.validate_input(cur_output)):
        warning(f"Layer {layer} failed to validate input")
        return

      cur_output = layer.run_layer()
      info(f"Layer {layer} finished with output {cur_output}")

      