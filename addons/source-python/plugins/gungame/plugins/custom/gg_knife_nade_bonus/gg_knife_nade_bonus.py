# ../gungame/plugins/custom/gg_knife_nade_bonus/gg_knife_nade_bonus.py

"""Plugin that gives players bonuses when on knife/nade levels."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from contextlib import suppress

# Source.Python
import colors
from events import Event
from listeners import on_tick_listener_manager
from players.entity import Player

# GunGame
from gungame.core.players.dictionary import player_dictionary
from gungame.core.weapons.groups import all_grenade_weapons, melee_weapons

# Plugin
from .configuration import level_down, weapon_convars


# =============================================================================
# >> CLASSES
# =============================================================================
class _KnifeNadeBonusPlayer(Player):
    """Class used to give/remove bonuses for a player."""

    spark_entity = None

    def __init__(self, index, weapon_type_convars):
        """Give the player multi-level."""
        super(_KnifeNadeBonusPlayer, self).__init__(index)
        self.start_gravity = self.gravity
        self.start_speed = self.speed
        self.gravity = gravity.get_int() / 100
        self.speed = speed.get_int() / 100
        self.give_spark_entity()

    def give_spark_entity(self):
        """Give the player an env_spark effect."""
        entity = self.spark_entity = Entity.create('env_spark')
        entity.spawn_flags = 896
        entity.angles = Vector(-90, 0, 0)
        entity.magnitude = 8
        entity.trail_length = 3
        entity.set_parent(self, -1)
        entity.origin = self.origin
        entity.start_spark()

    def remove_bonuses(self):
        """Remove all bonuses from the player."""
        self.gravity = self.start_gravity
        self.speed = self.start_speed
        self.spark_entity.stop_spark()
        self.spark_entity.remove()


class _MultiLevelManager(dict):
    """Dictionary to store players with multi-level effects."""

    def __delitem__(self, userid, reset_levels=True):
        """Remove the player from the dictionary and remove the effects."""
        if reset_levels:
            player_dictionary[userid].multi_levels = 0
        if userid not in self:
            return
        self[userid].remove_multi_level()
        super(_MultiLevelManager, self).__delitem__(userid)
        if not len(self):
            on_tick_listener_manager.unregister_listener(self._tick)

    def clear(self, silent=False):
        """Remove each player individually instead of just clearing."""
        if silent:
            super().clear()
            return
        for userid in list(self):
            del self[userid]

    def delete_disconnecting_player(self, userid):
        """Remove the disconnecting player from the dictionary."""
        self.__delitem__(userid, reset_levels=False)

    def give_bonuses(self, userid):
        """Give the player multi-level effects."""
        if not len(self):
            on_tick_listener_manager.register_listener(self._tick)
        if userid in self:
            self.__delitem__(userid, reset_levels=False)
        self[userid] = _KnifeNadeBonusPlayer.from_userid(userid)

    def _tick(self):
        """Reset multi-level players' gravity each tick."""
        for player in self.values():
            player.reset_gravity()

multi_level_manager = _MultiLevelManager()


# =============================================================================
# >> HELPER FUNCTIONS
# =============================================================================
@Event('gg_level_up', 'gg_level_down')
def remove_and_give_bonuses(game_event):
    """"""
    if game_event.name == 'gg_level_down' and not level_down.get_bool():
        return

    player = player_dictionary[game_event['leveler']]
    level_weapon = player.level_weapon
    if level_weapon not in all_grenade_weapons | melee_weapons:
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
