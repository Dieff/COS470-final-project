import subprocess
from logging import info, warning
import pathlib

from PIL import Image

from layer import Layer

# TODO: make a UI for setting these constants or determine them automatically
TMP_FILE = "/tmp/sc.png"
OUTPUT = "DP-2"
SCALE = (160 * 2, 144 * 2)
GRIM_EXE = "/nix/store/lfw70hwlc9h65h2aa30c3rj9szfazdy2-grim-1.4.1/bin/grim"


def take_screenshot():
  """
    Returns a scaled and normalized Pillow Image of the current screen 
  """

  # delete the screenshot temp file
  # pathlib.Path.unlink(TMP_FILE)
  # capture a new screenshot
  capture_res = subprocess.run(
    f"{GRIM_EXE} -o {OUTPUT} {TMP_FILE}", shell=True)
  if (capture_res.returncode != 0):
    warning("Failed to capture screenshot")
    return False
  else:
    info("Successfully captured new image")
  new_sc = Image.open(TMP_FILE)

  # trim the margin off
  if new_sc.size[0] != new_sc.size[1]:
    x_margin = abs((new_sc.size[1] - new_sc.size[0]) / 2)
    top_margin = (new_sc.size[1] * 0.02)
    new_sc = new_sc.crop(
      (x_margin, top_margin, new_sc.size[0] - x_margin, new_sc.size[1]))

  # scale
  sc_scaled = new_sc.resize(SCALE, resample=Image.LANCZOS)
  return sc_scaled


class InputLayer:
  # this is the first layer, so any input is valid
  def validate_input(self, any):
    return True

  def run_layer(self):
    return take_screenshot()
