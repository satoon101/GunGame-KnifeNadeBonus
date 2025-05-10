# ../gungame/plugins/custom/gg_knife_nade_bonus/configuration.py

"""Creates the gg_knife_nade_bonus configuration."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame
from gungame.core.config.manager import GunGameConfigManager

# Plugin
from .info import info

# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
    "level_down",
    "weapon_convars",
)


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
weapon_convars = {
    "knife": {},
    "nade": {},
}


# =============================================================================
# >> CONFIGURATION
# =============================================================================
with (
    GunGameConfigManager(info.name) as _config,
    _config.cvar(name="give_on_level_down") as level_down,
):
    level_down.add_text()

    for weapon_name in ("nade", "knife"):
        _config.section(name=weapon_name.title())

        for cvar in (
            "smoke",
            "flash",
            "health",
            "speed",
        ):
            with _config.cvar(name=f"{weapon_name}_{cvar}") as _cvar:
                _cvar.add_text()
                weapon_convars[weapon_name][cvar] = _cvar
