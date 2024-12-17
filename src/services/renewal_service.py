from datetime import timedelta, datetime
from constants.constant import NO_OF_DAYS_BEFORE_TO_NOTIFY, NO_OF_DAYS_IN_A_MONTH
from models.subscription import Subscription
from dateutil.relativedelta import relativedelta


class RenewalService:

    def __init__(self, subscription: Subscription):
        self.subscription = subscription

    def calculate_renewal_dates(self) -> dict:
        renewal_dates = {}
        print("Renewal date function")

        # Ensure the start date is a datetime object
        if isinstance(self.subscription.start_date, str):
            start_date = datetime.strptime(self.subscription.start_date, "%d-%m-%Y")
        else:
            start_date = self.subscription.start_date

        # Loop through plans and calculate dates
        for category, plan in self.subscription.plans.items():
            print(f"Category: {category}, Plan: {plan}")
            print(f"Start Date: {start_date} (Type: {type(start_date)})")

            # Use relativedelta to add months for renewal date
            renewal_date = start_date + relativedelta(months=plan.duration)
            reminder_date = renewal_date - relativedelta(
                days=NO_OF_DAYS_BEFORE_TO_NOTIFY
            )

            # Store reminder date in a proper string format
            renewal_dates[category] = reminder_date.strftime("%d-%m-%Y")
            print(f"Renewal Date: {renewal_date}, Reminder Date: {reminder_date}")

        return renewal_dates

    # def calculate_renewal_dates(self) -> dict:
    #     renewal_dates = {}
    #     print("Renewal date function")
    #     for category, plan in self.subscription.plans.items():
    #         print(category, plan)
    #         print(self.subscription.start_date)
    #         print(type(self.subscription.start_date))
    #         self.subscription.start_date = datetime.strptime(self.subscription.start_date, "%d-%m-%Y" )
    #         renewal_date = self.subscription.start_date + relativedelta(months=plan.duration)
    #         print(renewal_date)
    #         reminder_date = renewal_date - relativedelta(days=NO_OF_DAYS_BEFORE_TO_NOTIFY)
    #         renewal_dates[category] = reminder_date.strftime("%d-%m-%Y")
    #         print(32)
    #         print(renewal_dates[category])
    #         print("Renewal dates final", renewal_dates)
    #     print(renewal_dates)
    #     return renewal_dates

    def calculate_total_cost(self) -> int:
        print("in total cost func")
        print(self.subscription.plans)
        total_cost = sum(plan.cost for plan in self.subscription.plans.values())
        if self.subscription.topup:
            total_cost += self.subscription.topup.cost
        print("T", total_cost)
        return total_cost

    def get_renewal_details(self) -> list:
        renewal_dates = self.calculate_renewal_dates()
        print("In renewal details function")
        total_cost = self.calculate_total_cost()
        print("Total cost", total_cost)
        renewal_details = []
        for category, date in renewal_dates.items():
            renewal_details.append(f"RENEWAL_REMINDER {category.name} {date}")
        renewal_details.append(f"RENEWAL_AMOUNT {total_cost}")
        print(renewal_details)
        for detail in renewal_details:
            print(detail)
