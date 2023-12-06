from random import randint
from dataclasses import dataclass

from layer import Layer
from vision_layer import VisionLayerOutput
from game_state import BattleStateModel

@dataclass
class TreeNode:
  """
  Represents a node in the minmax tree.
  Contains the current game state, and
  calculates the utility function.
  """
  game_state = None
  parent = None
  next_actions = []

  def get_utility(self):
    pass

@dataclass
class TreeEdge:
  parent = None
  child = None
  action = None


class DecisionLayer(Layer):
  last_input = None

  def build_tree(self):
    pass

  def validate_input(self, input):
    if (isinstance(input, VisionLayerOutput)):
      self.last_input = input
      return True
    return False
  
