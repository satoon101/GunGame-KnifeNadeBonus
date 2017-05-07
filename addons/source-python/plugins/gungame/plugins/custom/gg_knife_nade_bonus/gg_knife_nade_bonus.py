# ../gungame/plugins/custom/gg_knife_nade_bonus/gg_knife_nade_bonus.py

"""Plugin that gives players bonuses when on knife/nade levels."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from contextlib import suppress

# Source.Python
import colors

# GunGame
from gungame.core.weapons.groups import all_grenade_weapons, melee_weapons

# Plugin
from .configuration import weapon_convars


# =============================================================================
# >> HELPER FUNCTIONS
# =============================================================================
def give_bonuses(player):
    level_weapon = player.level_weapon
    if level_weapon not in all_grenade_weapons + melee_weapons:
        return

    weapon_type = 'nade' if level_weapon in all_grenade_weapons else 'knife'
    convars = weapon_convars[weapon_type]

    # Give smoke grenade
    if convars['smoke'].get_bool() and level_weapon != 'smokegrenade':
        player.give_named_item('weapon_smokegrenade')

    # Give flashbang
    if convars['flash'].get_bool() and level_weapon != 'flashbang':
        player.give_named_item('weapon_flashbang')

    # Give extra health
    health = convars['health'].get_int()
    if health:
        player.health += health

    # TODO: gravity

    # Give extra speed
    speed = convars['speed'].get_float()
    if speed:
        player.speed *= speed

    # Set color
    color = _get_color(convars['color'].get_string())
    if color is not None:
        player.color = color

    # TODO: emit_sparks

    # TODO: emit_smoke


def _get_color(value):
    test_value = getattr(colors, value, None)
    if test_value is not None:
        return test_value

    with suppress(ValueError):
        test_value = list(
            map(
                int,
                value.split(',')
            )
        )
        if len(test_value) in (3, 4):
            return colors.Color(*test_value)

    return None
