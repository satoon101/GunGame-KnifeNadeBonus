# ../gungame/plugins/custom/gg_knife_nade_bonus/rules.py

"""Creates the gg_knife_nade_bonus rules."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame
from gungame.core.rules.instance import GunGameRules

# Plugin
from .info import info


# =============================================================================
# >> RULES
# =============================================================================
knife_nade_bonus_rules = GunGameRules(info.name)
knife_nade_bonus_rules.register_all_rules()
