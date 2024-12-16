from datetime import timedelta
from constants.constant import NO_OF_DAYS_BEFORE_TO_NOTIFY, NO_OF_DAYS_IN_A_MONTH
from models.subscription import Subscription


class RenewalService:

    def __init__(self, subscription: Subscription):
        self.subscription = subscription

    def calculate_renewal_dates(self) -> dict:
        renewal_dates = {}
        for category, plan in self.subscription.plans.items():
            renewal_date = self.subscription.start_date + timedelta(
                days=NO_OF_DAYS_IN_A_MONTH * plan.duration
            )
            reminder_date = renewal_date - timedelta(days=NO_OF_DAYS_BEFORE_TO_NOTIFY)
            renewal_dates[category] = reminder_date.strftime("%d-%m-%Y")
        return renewal_dates

    def calculate_total_cost(self) -> int:
        total_cost = sum(plan.cost for plan in self.subscription.plans.values())
        if self.subscriptions.topup:
            total_cost += self.subscription.topup.cost
        return total_cost

    def get_renewal_details(self) -> list:
        renewal_dates = self.calculate_renewal_dates()
        total_cost = self.calculate_total_cost()
        renewal_details = []
        for category, date in renewal_dates.items():
            renewal_details.append(f"RENEWAL_REMINDER {category.name} {date}")
        renewal_details.append(f"RENEWAL_AMOUNT {total_cost}")
        return renewal_details
