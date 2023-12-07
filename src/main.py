import logging
from logging import info, warning, error

from layer import LayerSet
from sc_wayland import InputLayer
from vision_layer import VisionLayer
from decision_layer import DecisionLayer


if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  info("Starting main program")

  layers = LayerSet([
    InputLayer(),
    VisionLayer(),
    DecisionLayer()
  ])

  layers.run()

