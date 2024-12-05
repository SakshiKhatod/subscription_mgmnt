from services import Subscription
from  subscription_mgmnt.constants.constant import MUSIC_FREE_PLAN_PRICE,MUSIC_FREE_PLAN_VALIDITY,MUSIC_PERSONAL_PLAN_PRICE,MUSIC_PERSONAL_PLAN_VALIDITY,MUSIC_PREMIUM_PLAN_PRICE,MUSIC_PREMIUM_PLAN_VALIDITY



class Music(Subscription):
    def __init__(self,subscription_date,subscription_category,subscription_plan) -> None:
        plans_dict={
            "FREE":{"subscription_price":MUSIC_FREE_PLAN_PRICE,"subscription_validity":MUSIC_FREE_PLAN_VALIDITY},
            "PERSONAL":{"subscription_price":MUSIC_PERSONAL_PLAN_PRICE,"subscription_validity":MUSIC_PERSONAL_PLAN_VALIDITY},
              "PREMIUM":{"subscription_price":MUSIC_PREMIUM_PLAN_PRICE,"subscription_validity":MUSIC_PREMIUM_PLAN_VALIDITY},
        }
        super().__init__(subscription_date,subscription_category,subscription_plan,plans_dict)

    def __str__(self):
        return "Music"
        

