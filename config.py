from pydantic import BaseModel
from typing import List, Dict


class Config(BaseModel):
    """Plugin Config Here"""

    QQMC_MCServer: str = ""
    QQMC_QQ: str = ""
    QQMC_Group: int = 0
    QQMC_Rcon_Message: bool = False