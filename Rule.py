from nonebot import get_plugin_config
from nonebot.adapters.minecraft import (
    Event as MinecraftEvent,
)
from nonebot.adapters.onebot.v11 import (
    GroupMessageEvent,
)

from .config import Config

config = get_plugin_config(Config)
Group = config.QQMC_Group

# Minecraft
def is_minecraft_rule(event) -> bool:
    return isinstance(event, (MinecraftEvent))

# OneBot V11
def is_target_group_message_rule(event: GroupMessageEvent) -> bool:
    if event.group_id == Group:
        return isinstance(event, GroupMessageEvent)
    else:
        return isinstance(event, GroupMessageEvent) and False