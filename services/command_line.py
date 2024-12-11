from datetime import datetime
from microservices.subscription import Subscription
from microservices.topup import Topup
from microservices.reminder import calculate_reminder_date
from constants.error_codes import ErrorCodes


class CommandLine:
    def __init__(self):
        self.subscription_start_date = None
        self.subscriptions = {}
        self.topup = None
        self.topup_validity = 0

    def validate_date(self, given_date: str) -> datetime:
        try:
            self.subscription_start_date = datetime.strptime(given_date, "%d-%m-%Y")
            return None
        except ValueError:
            return ErrorCodes.INVALID_DATE

    def add_subscription(
        self, subscription_category: str, subscription_plan: str
    ) -> str:
        if subscription_category in self.subscriptions:
            return ErrorCodes.DUPLICATE_CATEGORY
        self.subscriptions[subscription_category] = Subscription(
            subscription_category, subscription_plan
        )
        return None

    def add_topup(self, topup_type: str, months: int) -> str:
        if self.topup:
            return ErrorCodes.DUPLICATE_TOPUP
        self.topup = Topup(topup_type)
        self.topup_validity = months
        return None

    def calculate_renewal_details(self) -> str:
        if not self.subscriptions:
            return ErrorCodes.SUBSCRIPTION_NOT_FOUND
        result = []
        for category, plan in self.subscriptions.items():
            reminder_date = calculate_reminder_date(self.subscription_start_date)
            result.append(
                f"RENEWAL_REMINDER {category} {reminder_date.strftime('%d-%m-%Y')}"
            )
        return "\n".join(result)
