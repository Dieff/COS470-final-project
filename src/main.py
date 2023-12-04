import logging
from logging import info, warning, error
from sc_wayland import take_screenshot

if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  info("Starting main program")
  take_screenshot()

