import subprocess
from logging import warning

# libinput keycodes
ARROW_UP = "103"
ARROW_DOWN = "108"
ARROW_LEFT = "105"
ARROW_RIGHT = "106"
# Z
A_BUTTON = ""
# X
B_BUTTON = ""
# ENTER
SELECT_BUTTON = ""

YDT_EXE = "/home/dieff/.nix-profile/bin/ydotool"

class GameInputController:
  def _do_press(self, code):
    t_ret = subprocess.run([YDT_EXE, "key", f"{code}:1", f"{code}:0"])
    if (t_ret.returncode != 0):
      warning(f"failed to type {code}. Return status {t_ret.returncode}")

  def press_up(self):
    self._do_press(ARROW_UP)
