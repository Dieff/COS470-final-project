from dataclasses import dataclass

@dataclass
class PokemonStatus:

  # health is a floating point number from 0 to 10
  # note that this is not exactly how it works in the game, where it
  # is a floating point number based on the pokemon's level
  health = 10.0

  # there are some other stats that can be modified, such as speed
  # but they are less interesting
  attack_mod = 1.0
  defense_mod = 1.0

  # status conditions
  # see https://gamefaqs.gamespot.com/gameboy/367023-pokemon-red-version/faqs/64175/status-conditions

  # reduces movement ability
  sleeping = False
  paralyzed = False

  # may hurt
  confused = False

  # hurts each turn
  poisoned = False
  burned = False

  # is the pokemon in the middle of a mutli-turn move?
  cur_move = None

  # are there potions remaining?
  has_healing_items = True

  pkmn_type = "normal"

@dataclass
class BattleStateModel:
  player = PokemonStatus()
  enemy = PokemonStatus()

  cur_turn = "player"
  # a goal can be to defeat the enemy or to catch the enemy
  goal = "defeat"

class EntityAction:
  name = "Base Action"

  def next_state(self, prev_state):
    raise NotImplementedError()
  
class Attack(EntityAction):
  "Describes a single move that could be used by a pokemon"
  pass
