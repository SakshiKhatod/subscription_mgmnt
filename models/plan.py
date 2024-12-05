print(1)
# import sys
# import os

# sys.path.append(
#     os.path.abspath(os.path.join(os.path.dirname(__file__), "../subscription_mgmnt"))
# )
from subscription_mgmnt.constants.constant import (
    FREE_PLAN,
    PERSONAL_MUSIC,
    PREMIUM_MUSIC,
    PERSONAL_VIDEO,
    PREMIUM_VIDEO,
    PERSONAL_PODCAST,
    PREMIUM_PODCAST,
)
from subscription_mgmnt.constants.constant_group import (
    SubscriptionCategory,
    SubscriptionPlan,
)
from dataclasses import dataclass


@dataclass(frozen=True)
class Plan:
    subscription_plan: SubscriptionPlan
    subscription_category: SubscriptionCategory

    def get_subscription_category_plan(self) -> int:
        total_price = 0
        plan_price = {
            SubscriptionCategory.MUSIC: {
                SubscriptionPlan.FREE: FREE_PLAN,
                SubscriptionPlan.PERSONAL: PERSONAL_MUSIC,
                SubscriptionPlan.PREMIUM: PREMIUM_MUSIC,
            },
            SubscriptionCategory.VIDEO: {
                SubscriptionPlan.FREE: FREE_PLAN,
                SubscriptionPlan.PERSONAL: PERSONAL_VIDEO,
                SubscriptionPlan.PREMIUM: PREMIUM_VIDEO,
            },
            SubscriptionCategory.PODCAST: {
                SubscriptionPlan.FREE: FREE_PLAN,
                SubscriptionPlan.PERSONAL: PERSONAL_PODCAST,
                SubscriptionPlan.PREMIUM: PREMIUM_PODCAST,
            },
        }
        print(plan_price)
        return plan_price[self.subscription_category][self.subscription_plan]

    def get_price_for_subscription_plan(self) -> int:
        subscription_details = self.get_subscription_category_plan()
