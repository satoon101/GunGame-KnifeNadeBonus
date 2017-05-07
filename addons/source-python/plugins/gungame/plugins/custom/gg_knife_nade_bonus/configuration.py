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
    'weapon_convars',
)


# =============================================================================
# >> CONFIGURATION
# =============================================================================
weapon_convars = {
    'knife': {},
    'nade': {},
}
with GunGameConfigManager(info.name) as _config:

    with _config.cvar('nade_smoke') as nade_smoke:
        nade_smoke.add_text()
        weapon_convars['nade']['smoke'] = nade_smoke

    with _config.cvar('nade_flash') as nade_flash:
        nade_flash.add_text()
        weapon_convars['nade']['flash'] = nade_flash

    with _config.cvar('nade_health') as nade_health:
        nade_health.add_text()
        weapon_convars['nade']['health'] = nade_health

    with _config.cvar('nade_gravity') as nade_gravity:
        nade_gravity.add_text()
        weapon_convars['nade']['gravity'] = nade_gravity

    with _config.cvar('nade_speed') as nade_speed:
        nade_speed.add_text()
        weapon_convars['nade']['speed'] = nade_speed

    with _config.cvar('nade_color') as nade_color:
        nade_color.add_text()
        weapon_convars['nade']['color'] = nade_color

    with _config.cvar('nade_emit_sparks') as nade_emit_sparks:
        nade_emit_sparks.add_text()
        weapon_convars['nade']['emit_sparks'] = nade_emit_sparks

    with _config.cvar('nade_emit_smoke') as nade_emit_smoke:
        nade_emit_smoke.add_text()
        weapon_convars['nade']['emit_smoke'] = nade_emit_smoke

    with _config.cvar('knife_smoke') as knife_smoke:
        knife_smoke.add_text()
        weapon_convars['knife']['smoke'] = knife_smoke

    with _config.cvar('knife_flash') as knife_flash:
        knife_flash.add_text()
        weapon_convars['knife']['flash'] = knife_flash

    with _config.cvar('knife_health') as knife_health:
        knife_health.add_text()
        weapon_convars['knife']['health'] = knife_health

    with _config.cvar('knife_gravity') as knife_gravity:
        knife_gravity.add_text()
        weapon_convars['knife']['gravite'] = knife_gravity

    with _config.cvar('knife_speed') as knife_speed:
        knife_speed.add_text()
        weapon_convars['knife']['speed'] = knife_speed

    with _config.cvar('knife_color') as knife_color:
        knife_color.add_text()
        weapon_convars['knife']['color'] = knife_color

    with _config.cvar('knife_emit_sparks') as knife_emit_sparks:
        knife_emit_sparks.add_text()
        weapon_convars['knife']['emit_sparks'] = knife_emit_sparks

    with _config.cvar('knife_emit_smoke') as knife_emit_smoke:
        knife_emit_smoke.add_text()
        weapon_convars['knife']['emit_smoke'] = knife_emit_smoke


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
