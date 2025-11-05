from nonebot import get_plugin_config, get_bot
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent

from ..config import Config

from .send_to_mc import send_msg_to_mc
from ..Matcher import group_message_matcher

config = get_plugin_config(Config)

MCServer = config.QQMC_MCServer
QQ = config.QQMC_QQ
Group = config.QQMC_Group

@group_message_matcher.handle()
async def qq_message(event: GroupMessageEvent, bot: Bot):
    bot = get_bot(QQ)
    QQ_ID = event.sender.user_id
    Group_ID = event.group_id
    QQ_MSG = event.message

    msg = f"§6[{Group_ID}] §a<{QQ_ID}>: §f{QQ_MSG}"

    await send_msg_to_mc(MCServer, msg, bot)