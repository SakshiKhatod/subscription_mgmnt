from services import Subscription
from  subscription_mgmnt.constants.constant import VIDEO_FREE_PLAN_PRICE,VIDEO_FREE_PLAN_VALIDITY,VIDEO_PERSONAL_PLAN_PRICE,VIDEO_PERSONAL_PLAN_VALIDITY,VIDEO_PREMIUM_PLAN_PRICE,VIDEO_PREMIUM_PLAN_VALIDITY



class Video(Subscription):
    def __init__(self,subscription_date,subscription_category,subscription_plan) -> None:
        plans_dict={
            "FREE":{"subscription_price":VIDEO_FREE_PLAN_PRICE,"subscription_validity":VIDEO_FREE_PLAN_VALIDITY},
            "PERSONAL":{"subscription_price":VIDEO_PERSONAL_PLAN_PRICE,"subscription_validity":VIDEO_PERSONAL_PLAN_VALIDITY},
              "PREMIUM":{"subscription_price":VIDEO_PREMIUM_PLAN_PRICE,"subscription_validity":VIDEO_PREMIUM_PLAN_VALIDITY},
        }
        super().__init__(subscription_date,subscription_category,subscription_plan,plans_dict)

    def __str__(self):
        return "Video"