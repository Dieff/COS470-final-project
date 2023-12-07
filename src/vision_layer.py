from dataclasses import dataclass
from uuid import uuid4
from logging import info, warning, error
import pathlib

from layer import Layer
from sc_wayland import SCALE

import PIL


@dataclass
class VisionLayerOutput:
  max_health = 10
  min_health = 10
  cur_menu = "MaxMove"

  def __repr__(self) -> str:
    return f"State(max_health={self.max_health} min_health={self.min_health})"

# where will data files be saved?
OUTPUT_DIR = "data"
# as found by opening a screen capture data file in "Pinta"
ENEMY_HEALTH_BAR_PIX_LOC = ((56, 34), (156, 34))
PLAYER_HEALTH_BAR_PIX_LOC = ((197, 149), (300, 149))

GREEN_HEALTH_COLOR = (74, 166, 90)
YELLOW_HEALTH_COLOR = (215, 166, 0)
RED_HEALTH_COLOR = (213, 74, 39)
WHITE_HEALTH_COLOR = (255, 240, 255)

PIXEL_DIFF_TOLERANCE = 10


def write_file(img_buffer: PIL.Image.Image):
  """
  saves an image file
  """
  name = f"{str(uuid4())[:8]}.png"
  path = pathlib.Path(OUTPUT_DIR)
  path = path.joinpath(name)
  info(f"Saved image ({img_buffer.size}) to file {path}")
  img_buffer.save(path)


def get_color_distance(color1, color2):
  """returns a very simplistic measurement of the
  likeness of two rgb pixels
  """
  return (abs(color1[0] - color2[0])
          + abs(color1[1] - color2[1])
          + abs(color1[2] - color2[2]))


class VisionLayer(Layer):
  last_input = None
  save_input = False

  def validate_input(self, input: PIL.Image.Image):
    self.last_input = input
    # need to establish that input is an Image first
    # so we have to write this in a clunky way
    if isinstance(input, PIL.Image.Image):
      if input.size == SCALE:
        return True
    return False

  def test_health(self, start, end):
    x_diff = end[0] - start[0]
    step = int(x_diff / 20)
    final_step = 0
    for i in range(20):
      final_step += 1
      cur_pixel_loc = (start[0] + (step * i), start[1])
      cur_pixel = self.last_input.getpixel(cur_pixel_loc)
      if (
        get_color_distance(cur_pixel, GREEN_HEALTH_COLOR) < PIXEL_DIFF_TOLERANCE or
        get_color_distance(cur_pixel, RED_HEALTH_COLOR) < PIXEL_DIFF_TOLERANCE or
        get_color_distance(
          cur_pixel, YELLOW_HEALTH_COLOR) < PIXEL_DIFF_TOLERANCE
      ):
        continue
      if (get_color_distance(cur_pixel, WHITE_HEALTH_COLOR) < PIXEL_DIFF_TOLERANCE):
        break

    return final_step / 20

  def run_layer(self):
    if self.save_input:
      write_file(self.last_input)

    cur_state = VisionLayerOutput()
    cur_state.max_health = self.test_health(
      PLAYER_HEALTH_BAR_PIX_LOC[0], PLAYER_HEALTH_BAR_PIX_LOC[1])
    cur_state.min_health = self.test_health(
      ENEMY_HEALTH_BAR_PIX_LOC[0], ENEMY_HEALTH_BAR_PIX_LOC[1])

    self.last_input = None
    return cur_state
