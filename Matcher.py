from nonebot import on_message, on_notice

from nonebot.rule import Rule
from .Rule import is_minecraft_rule, is_target_group_message_rule

# Minecraft
# 聊天消息和死亡事件
mc_message_matcher = on_message(Rule(is_minecraft_rule), priority=5, block=True)
# 加入/退出事件
mc_notice_matcher = on_notice(Rule(is_minecraft_rule), priority=5, block=True)

# Onebot V11
# 群聊天事件
group_message_matcher = on_message(Rule(is_target_group_message_rule), priority=5, block=True)