# from services.command_line import CommandLine


# def main():
#     processor = CommandLine()
#     file_path = "sample_input/input2.txt"
#     with open(file_path, "r") as file:
#         for line in file:
#             commands = line.strip().split()
#             if not commands:
#                 continue
#             command = commands[0]
#             if command == "START_SUBSCRIPTION":
#                 result = processor.validate_date(commands[1])
#                 if result:
#                     print(result)
#             elif command == "ADD_SUBSCRIPTION":
#                 result = processor.add_subscription(commands[1], commands[2])
#                 if result:
#                     print(result)
#             elif command == "ADD_TOPUP":
#                 result = processor.add_topup(commands[1], int(commands[2]))
#                 if result:
#                     print(result)
#             elif command == "PRINT_RENEWAL_DETAILS":
#                 print(processor.calculate_renewal_details())


# if __name__ == "__main__":
#     main()
import sys
from datetime import datetime
from services.subscription_service import SubscriptionService
from services.topup_service import TopupService
from services.renewal_service import RenewalService
from enums.subscription_category import SubscriptionCategory
from enums.plan_type import PlanType
from enums.topup_type import TopupType
from constants.error_codes import ErrorCodes


class Main:
    def __init__(self):
        self.subscription_service = SubscriptionService()
        self.topup_service = TopupService()
        self.renewal_service = RenewalService()

    def process_command(self, command: str):
        parts = command.strip().split()
        if not parts:
            return

        action = parts[0]

        if action == "START_SUBSCRIPTION":
            if len(parts) != 2:
                print("INVALID_INPUT")
                return
            start_date_str = parts[1]
            try:
                start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
                self.subscription_service.start_subscription(start_date)
            except ValueError:
                print(ErrorCodes.INVALID_DATE)

        elif action == "ADD_SUBSCRIPTION":
            if len(parts) != 3:
                print("INVALID_INPUT")
                return
            category_str, plan_str = parts[1], parts[2]
            try:
                category = SubscriptionCategory[category_str.upper()]
                plan = PlanType[plan_str.upper()]
                error = self.subscription_service.add_subscription(category, plan)
                if error:
                    print(error)
            except KeyError:
                print(ErrorCodes.INVALID_CATEGORY)

        elif action == "ADD_TOPUP":
            if len(parts) != 3:
                print("INVALID_INPUT")
                return
            topup_type_str, months_str = parts[1], parts[2]
            try:
                months = int(months_str)
                topup_type = TopupType[topup_type_str.upper()]
                if not self.subscription_service.has_active_subscriptions():
                    print("SUBSCRIPTIONS_NOT_FOUND")
                    return
                error = self.topup_service.add_topup(topup_type, months)
                if error:
                    print(error)
            except (KeyError, ValueError):
                print(ErrorCodes.INVALID_TOPUP_TYPE)

        elif action == "PRINT_RENEWAL_DETAILS":
            if not self.subscription_service.has_active_subscriptions():
                print(ErrorCodes.SUBSCRIPTION_NOT_FOUND)
                return
            start_date = self.subscription_service.get_start_date()
            subscriptions = self.subscription_service.get_subscriptions()
            topup_cost = self.topup_service.get_topup_cost()
            renewal_dates = self.renewal_service.calculate_renewal_dates(
                start_date, subscriptions
            )
            total_cost = self.subscription_service.calculate_total_cost() + topup_cost

            # Print Renewal Details
            for category, reminder_date in renewal_dates.items():
                print(f"RENEWAL_REMINDER {category} {reminder_date}")
            print(f"RENEWAL_AMOUNT {total_cost}")

        else:
            print("INVALID_COMMAND")

    def run(self, file_path):
        try:
            with open(file_path, "r") as file:
                for line in file:
                    self.process_command(line)
        except FileNotFoundError:
            print("File not found. Please provide a valid file path.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    app = Main()
    app.run(file_path)
