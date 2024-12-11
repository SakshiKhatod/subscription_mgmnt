# from subscription_mgmnt.models import music,video,podcast
from constants.constant import TOPUP_COSTS

class Topup:

    def __init__(self,topup_type:str) -> None:
        self.topup_type = topup_type
    
    def caculate_topup_total_price(self,months:int)->float:
        return TOPUP_COSTS.get(self.topup_type,0)*months

