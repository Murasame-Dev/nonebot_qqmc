from nonebot import get_plugin_config, logger
from nonebot.adapters.minecraft import (
    BaseChatEvent,
    BaseDeathEvent,
    BaseJoinEvent,
    BaseQuitEvent,
)

from ..Matcher import mc_message_matcher, mc_notice_matcher

from .send_to_qq import send_msg_to_qq

# 导入配置/变量赋值
from ..config import Config

config = get_plugin_config(Config)

MCServer = config.QQMC_MCServer
Group = config.QQMC_Group

# 监听 Minecraft 聊天消息/死亡事件
@mc_message_matcher.handle()
async def mc_message(event: BaseChatEvent | BaseDeathEvent):
    MC_ID = event.player.nickname
    Server = event.server_name
    MC_MSG = event.message

    # chat event
    if isinstance(event, BaseChatEvent):
        msg = f"[{Server}] {MC_ID}: {MC_MSG}"
        logger.info(msg)
    # death event
    elif isinstance(event, BaseDeathEvent):
        msg = f"[{Server}] {MC_ID} 死亡了"
        logger.info(msg)
        logger.info(f"事件详情: {event}")

    await send_msg_to_qq(Server, msg)


# 监听 Minecraft 玩家加入/离开事件
@mc_notice_matcher.handle()
async def mc_notice(event: BaseJoinEvent | BaseQuitEvent):
    MC_ID = event.player.nickname
    Server = event.server_name
    if isinstance(event, BaseJoinEvent):
        action = "加入了"
    else:
        action = "离开了"
    msg = f"[{Server}] {MC_ID} {action}服务器"
    logger.info(msg)
    await send_msg_to_qq(Server, msg)