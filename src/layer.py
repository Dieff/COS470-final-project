class Layer:
  """
    A base class for all layers
    besides the i/o ones.
    Each layer takes a previous state layer's
    output and emits a new one. 
  """

  name = "Generic Layer"

  def validate_input(self, input):
    raise NotImplementedError()
  
  def run_layer(self):
    raise NotImplementedError()
  
  def __repr__(self) -> str:
    return f"{self.name}"
