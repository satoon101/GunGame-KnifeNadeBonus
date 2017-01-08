# ../gungame/plugins/custom/gg_knife_nade_bonus/rules.py

"""Creates the gg_knife_nade_bonus rules."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame
from gungame.core.rules.instance import GunGameRules
from gungame.core.rules.strings import rules_translations

# Plugin
from .info import info


# =============================================================================
# >> RULES
# =============================================================================
knife_nade_bonus_rules = GunGameRules(info.name)
