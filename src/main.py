# from models.subscription import Subscription
# from services.subscription_service import SubscriptionService
# from services.topup_service import TopupService
# from services.renewal_service import RenewalService
# from enums.subscription_category import SubscriptionCategory
# from enums.plan_type import PlanType
# from enums.topup_type import TopupType
# from constants.error_codes import ErrorCodes
# import sys
# from datetime import datetime


# def validate_date(given_date: str):
#     try:
#         datetime.strptime(given_date, "%d-%m-%Y")
#         return True
#     except ValueError:
#         return False


# def process_commands(input_file):

#     try:
#         subscription = None
#         subscription_service = None
#         topup_service = None
#         renewal_service = None

#         with open(input_file, "r") as file:
#             for line in file:
#                 parts = line.strip().split()
#                 if not parts:
#                     continue
#                 command = parts[0]

#                 if command == "START_SUBSCRIPTION":

#                     start_date = parts[1]
#                     if not validate_date(start_date):
#                         print(ErrorCodes.INVALID_DATE)
#                         break
#                     subscription = Subscription(start_date)
#                     subscription_service = SubscriptionService(subscription)
#                     topup_service = TopupService(subscription)
#                     renewal_service = RenewalService(subscription)
#                 elif command == "ADD_SUBSCRIPTION":
#                     if not subscription:
#                         print(ErrorCodes.SUBSCRIPTION_NOT_FOUND)
#                         break

#                     category = parts[1]
#                     plan_type = parts[2]
#                     if not category in SubscriptionCategory:
#                         print(ErrorCodes.INVALID_CATEGORY)
#                         break
#                     if not plan_type in PlanType:
#                         print(ErrorCodes.INVALID_PLAN_TYPE)
#                         break
#                     result = subscription_service.add_subscription(
#                         SubscriptionCategory[category], PlanType[plan_type]
#                     )
#                     if result:
#                         print(result)
#                         break
#                 elif command == "ADD_TOPUP":
#                     if not subscription:
#                         print(ErrorCodes.SUBSCRIPTION_NOT_FOUND)
#                         continue
#                     topup_name = parts[1]
#                     months = int(parts[2])
#                     if topup_name not in TopupType:
#                         print(ErrorCodes.INVALID_TOPUP_TYPE)
#                         break
#                     result = topup_service.add_topup(TopupType[topup_name], months)
#                     if result:
#                         print(result)
#                         break

#                 elif command == "PRINT_RENEWAL_DETAILS":
#                     if not subscription:
#                         print(ErrorCodes.SUBSCRIPTION_NOT_FOUND)
#                         continue
#                     renewal_service.print_renewal_details()

#                 else:
#                     print("INVALID_INPUT")
#                     break

#     except Exception as e:
#         print(f"Error occurred: {e}")
#         sys.exit(1)


# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python main.py <input_file>")
#         sys.exit(1)

#     input_file = "inputs/sample_input1.txt"
#     input_file = sys.argv[1]
#     process_commands(input_file)
from models.subscription import Subscription
from services.subscription_service import SubscriptionService
from services.topup_service import TopupService
from services.renewal_service import RenewalService
from enums.subscription_category import SubscriptionCategory
from enums.plan_type import PlanType
from enums.topup_type import TopupType
from constants.error_codes import ErrorCodes
import sys
from datetime import datetime
from services.helper_functions import (
    validate_plan_type,
    validate_date,
    validate_category,
    validate_topup_type,
)


# ---------------- Core Processing Logic ----------------
def process_commands(input_file):
    try:
        subscription = None
        subscription_service = None
        topup_service = None
        renewal_service = None

        with open(input_file, "r") as file:
            for line in file:
                parts = line.strip().split()
                if not parts:
                    continue
                command = parts[0]

                if command == "START_SUBSCRIPTION":
                    start_date = parts[1]
                    if not validate_date(start_date):
                        print(ErrorCodes.INVALID_DATE)
                        break
                    subscription = Subscription(start_date)
                    subscription_service = SubscriptionService(subscription)
                    topup_service = TopupService(subscription)
                    renewal_service = RenewalService(subscription)

                elif command == "ADD_SUBSCRIPTION":
                    if not subscription:
                        print(ErrorCodes.SUBSCRIPTION_NOT_FOUND)
                        break

                    category_input = parts[1]
                    plan_type_input = parts[2]

                    # Validate inputs
                    category = validate_category(category_input)
                    plan_type = validate_plan_type(plan_type_input)
                    if not category or not plan_type:
                        break

                    result = subscription_service.add_subscription(category, plan_type)
                    if result:
                        print(result)
                        break

                elif command == "ADD_TOPUP":
                    if not subscription:
                        print(ErrorCodes.SUBSCRIPTION_NOT_FOUND)
                        continue

                    topup_name_input = parts[1]
                    months = int(parts[2])

                    # Validate inputs
                    topup_name = validate_topup_type(topup_name_input)
                    if not topup_name:
                        break

                    result = topup_service.add_topup(topup_name, months)
                    if result:
                        print(result)
                        break

                elif command == "PRINT_RENEWAL_DETAILS":
                    if not subscription:
                        print(ErrorCodes.SUBSCRIPTION_NOT_FOUND)
                        continue
                    renewal_service.print_renewal_details()

                else:
                    print("INVALID_INPUT")
                    break

    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)


# ---------------- Script Entry Point ----------------
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    process_commands(input_file)
