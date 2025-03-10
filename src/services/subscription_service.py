from constants.error_codes import ErrorCodes
from models.plan import Plan
from models.subscription import Subscription
from enums.subscription_category import SubscriptionCategory
from enums.plan_type import PlanType


class SubscriptionService:
    def __init__(self, subscription: Subscription):
        self.subscription = subscription

    def add_subscription(
        self, subscription_category: SubscriptionCategory, plan_type: PlanType
    ):
        if subscription_category not in SubscriptionCategory:
            return ErrorCodes.INVALID_CATEGORY
        if subscription_category in self.subscription.plans:
            return ErrorCodes.DUPLICATE_CATEGORY

        plan = Plan(plan_type, subscription_category)
        self.subscription.plans[subscription_category] = plan
        return None

    def get_subscriptions(self):
        return self.subscriptions
