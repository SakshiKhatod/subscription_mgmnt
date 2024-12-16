# from subscription_mgmnt.models import music,video,podcast
from constants.constant import SUBSCRIPTION_COSTS


class Subscription:

    def __init__(self, subscription_category: str, subscription_plan: str) -> None:
        self.subscription_category = subscription_category
        self.subscription_plan = subscription_plan

    def calculate_subscription_price(self) -> int:
        return SUBSCRIPTION_COSTS.get(self.subscription_category, {}).get(
            self.subscription_plan, 0
        )


