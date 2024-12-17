from constants.plan_mapping import PLAN_DETAILS
from enums.plan_type import PlanType
from enums.subscription_category import SubscriptionCategory
from constants.error_codes import ErrorCodes


class Plan:
    def __init__(self, plan_type: PlanType, category: SubscriptionCategory):
        if not isinstance(plan_type, PlanType):
            raise ValueError(ErrorCodes.INVALID_PLAN_TYPE)
        if not isinstance(category, SubscriptionCategory):
            return ErrorCodes.INVALID_CATEGORY
        plan_details = PLAN_DETAILS[category][plan_type]
        self.category = category
        self.plan_type = plan_type
        self.cost = plan_details["cost"]
        self.duration = plan_details["duration"]

    def get_details(self):
        print(self.category.name, self.plan_type.name, self.cost, self.duration)
        return {
            "category": self.category.name,
            "plan_type": self.plan_type.name,
            "cost": self.cost,
            "duration_in_months": self.duration,
        }
