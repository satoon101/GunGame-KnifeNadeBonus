# ../gungame/plugins/custom/gg_knife_nade_bonus/gg_knife_nade_bonus.py

"""Plugin that gives players bonuses when on knife/nade levels."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from events import Event
from filters.players import PlayerIter

# GunGame
from gungame.core.players.dictionary import player_dictionary
from gungame.core.weapons.groups import all_grenade_weapons, melee_weapons

# Plugin
from .configuration import level_down, weapon_convars

# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
EVENT_VARIABLES = {
    "player_spawn": "userid",
    "gg_level_up": "leveler",
    "gg_level_down": "leveler",
}


# =============================================================================
# >> HELPER FUNCTIONS
# =============================================================================
@Event(*EVENT_VARIABLES.keys())
def remove_and_give_bonuses(game_event):
    """Remove and give out bonuses."""
    if game_event.name == "gg_level_down" and not level_down.get_bool():
        return

    player = player_dictionary[game_event[EVENT_VARIABLES[game_event.name]]]
    level_weapon = player.level_weapon
    if level_weapon not in all_grenade_weapons | melee_weapons:
        return

    weapon_type = "nade" if level_weapon in all_grenade_weapons else "knife"
    convars = weapon_convars[weapon_type]

    # Give smoke grenade
    if convars["smoke"].get_bool() and level_weapon != "smokegrenade":
        player.give_named_item("weapon_smokegrenade")

    # Give flashbang
    if convars["flash"].get_bool() and level_weapon != "flashbang":
        player.give_named_item("weapon_flashbang")

    # Give extra health
    health = convars["health"].get_int()
    if health:
        player.health += health

    # Give extra speed
    speed = convars["speed"].get_float()
    if speed:
        player.speed *= speed


@Event("round_freeze_end")
def _give_speed_bonus(game_event):
    """Give speed bonus to players on knife/nade level."""
    speed_convars = {
        weapon_type: weapon_convars[weapon_type]["speed"].get_float()
        for weapon_type in ("nade", "knife")
    }
    for userid in [player.userid for player in PlayerIter()]:
        player = player_dictionary[userid]
        level_weapon = player.level_weapon
        if level_weapon not in all_grenade_weapons | melee_weapons:
            return

        speed = speed_convars[
            "nade" if level_weapon in all_grenade_weapons else "knife"
        ]
        if speed:
            player.speed *= speed
