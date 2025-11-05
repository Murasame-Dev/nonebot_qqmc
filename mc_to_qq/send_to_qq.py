import re

from nonebot import get_bot, get_plugin_config
from nonebot.adapters.onebot.v11 import Bot

from ..config import Config

config = get_plugin_config(Config)
Group = config.QQMC_Group
QQ = config.QQMC_QQ

async def send_msg_to_qq(bot: Bot, msg: str):
    msg = re.sub(r"[&§]", "", msg)

    try:
        bot = get_bot(QQ)
        await bot.send_group_msg(
            group_id=Group,
            message=msg
        )
    except Exception as e:
        print(f"Error sending message to QQ: {e}")
