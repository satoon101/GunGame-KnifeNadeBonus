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
    'knife_color',
    'knife_emit_smoke',
    'knife_emit_sparks',
    'knife_flash',
    'knife_gravity',
    'knife_health',
    'knife_smoke',
    'knife_speed',
    'nade_color',
    'nade_emit_smoke',
    'nade_emit_sparks',
    'nade_flash',
    'nade_gravity',
    'nade_health',
    'nade_smoke',
    'nade_speed',
)


# =============================================================================
# >> CONFIGURATION
# =============================================================================
with GunGameConfigManager(info.name) as _config:

    with _config.cvar('nade_smoke') as nade_smoke:
        nade_smoke.add_text()

    with _config.cvar('nade_flash') as nade_flash:
        nade_flash.add_text()

    with _config.cvar('nade_health') as nade_health:
        nade_health.add_text()

    with _config.cvar('nade_gravity') as nade_gravity:
        nade_gravity.add_text()

    with _config.cvar('nade_speed') as nade_speed:
        nade_speed.add_text()

    with _config.cvar('nade_color') as nade_color:
        nade_color.add_text()

    with _config.cvar('nade_emit_sparks') as nade_emit_sparks:
        nade_emit_sparks.add_text()

    with _config.cvar('nade_emit_smoke') as nade_emit_smoke:
        nade_emit_smoke.add_text()

    with _config.cvar('knife_smoke') as knife_smoke:
        knife_smoke.add_text()

    with _config.cvar('knife_flash') as knife_flash:
        knife_flash.add_text()

    with _config.cvar('knife_health') as knife_health:
        knife_health.add_text()

    with _config.cvar('knife_gravity') as knife_gravity:
        knife_gravity.add_text()

    with _config.cvar('knife_speed') as knife_speed:
        knife_speed.add_text()

    with _config.cvar('knife_color') as knife_color:
        knife_color.add_text()

    with _config.cvar('knife_emit_sparks') as knife_emit_sparks:
        knife_emit_sparks.add_text()

    with _config.cvar('knife_emit_smoke') as knife_emit_smoke:
        knife_emit_smoke.add_text()


'''
smoke
flash
health
gravity
speed
color (just enable/disable, auto set using team color and 128 alpha)
emit_sparks
emit_smoke
'''