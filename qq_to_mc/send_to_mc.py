from nonebot import get_plugin_config, get_bot, logger
from nonebot.adapters.minecraft import Bot
from nonebot.adapters.minecraft.exception import ActionFailed

from ..config import Config

config = get_plugin_config(Config)

MCServer = config.QQMC_MCServer
Rcon_Message = config.QQMC_Rcon_Message

async def send_msg_to_mc(MCServer: str, msg: str, bot: Bot):
    bot = get_bot(MCServer)
    if Rcon_Message:
        await bot.send_rcon_command(command=f'tellraw @a "{msg}"')
        logger.info(f"Sent rcon message to Minecraft server: {msg}")

    else:
        await bot.send_chat_message(message=f"{msg}")
        logger.info(f"Sent chat message to Minecraft server: {msg}")