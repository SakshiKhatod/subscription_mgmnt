from constants.error_codes import ErrorCodes
from models.topup import Topup
from models.subscription import Subscription
from enums.topup_type import TopupType


class TopupService:
    def __init__(self, subscription: Subscription):
        self.subscription = subscription

    def add_topup(self, topup_type: TopupType, no_of_months: int):
        if not self.subscription.plans:
            return ErrorCodes.SUBSCRIPTION_NOT_FOUND
        if self.subscription.topup:
            return ErrorCodes.DUPLICATE_TOPUP

        self.subscription.topup = Topup(topup_type, no_of_months)
        return None
