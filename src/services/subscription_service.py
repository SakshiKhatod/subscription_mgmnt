from subscription_mgmnt.constants.error_codes import ErrorCodes
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
        if subscription_category in self.subscription.plans:
            return ErrorCodes.DUPLICATE_CATEGORY
        if not isinstance(subscription_category, SubscriptionCategory):
            return ErrorCodes.INVALID_CATEGORY
        if not isinstance(plan_type, PlanType):
            return ErrorCodes.INVALID_PLAN_TYPE
        plan = Plan(plan_type, subscription_category)
        self.subscription.plans[subscription_category] = plan
        return None

    def get_subscriptions(self):
        return self.subscriptions
