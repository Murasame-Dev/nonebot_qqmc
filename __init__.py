from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

# MC消息 发送到 QQ
from .mc_to_qq import mc_to_qq as mc_to_qq
# QQ消息 发送到 MC
from .qq_to_mc import qq_to_mc as qq_to_mc

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="qqmc",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

