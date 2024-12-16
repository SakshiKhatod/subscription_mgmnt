from datetime import datetime
from services.subscription_service import SubscriptionService
from services.topup_service import TopupService
from constants.error_codes import ErrorCodes


class Subscription:

    def __init__(self, start_date: str):
        self.start_date = start_date
        self.plans = {}
        self.topup = None

    def add_plan(self, category, plan):
        self.plans[category] = plan

    def add_topup(self, topup):
        self.topup = topup

    def has_active_subscriptions(self):
        return len(self.plans) > 0
        # try:
        #     self.start_date = datetime.strptime(start_date,"%d-%m-%Y")
        # except ValueError:
        #     raise ValueError(ErrorCodes.INVALID_DATE)
        # self.subscription_service=SubscriptionService()
        # self.topup_service=TopupService()
