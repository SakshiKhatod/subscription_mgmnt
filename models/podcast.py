from services import Subscription
from subscription_mgmnt.constants.constant import (
    PODCAST_FREE_PLAN_PRICE,
    PODCAST_FREE_PLAN_VALIDITY,
    PODCAST_PERSONAL_PLAN_PRICE,
    PODCAST_PERSONAL_PLAN_VALIDITY,
    PODCAST_PREMIUM_PLAN_PRICE,
    PODCAST_PREMIUM_PLAN_VALIDITY,
)


class Podcast(Subscription):
    def __init__(
        self, subscription_date, subscription_category, subscription_plan
    ) -> None:
        plans_dict = {
            "FREE": {
                "subscription_price": PODCAST_FREE_PLAN_PRICE,
                "subscription_validity": PODCAST_FREE_PLAN_VALIDITY,
            },
            "PERSONAL": {
                "subscription_price": PODCAST_PERSONAL_PLAN_PRICE,
                "subscription_validity": PODCAST_PERSONAL_PLAN_VALIDITY,
            },
            "PREMIUM": {
                "subscription_price": PODCAST_PREMIUM_PLAN_PRICE,
                "subscription_validity": PODCAST_PREMIUM_PLAN_VALIDITY,
            },
        }
        super().__init__(
            subscription_date, subscription_category, subscription_plan, plans_dict
        )

    def __str__(self):
        return "Podcast"
