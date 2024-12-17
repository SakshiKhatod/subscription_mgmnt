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


def validate_date(given_date: str) -> datetime:
    try:
        datetime.strptime(given_date, "%d-%m-%Y")
        return True
    except ValueError:
        return False


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
                    print(subscription)
                    subscription_service = SubscriptionService(subscription)
                    print(subscription_service)
                    topup_service = TopupService(subscription)
                    print(topup_service)
                    renewal_service = RenewalService(subscription)
                    print(renewal_service)

                elif command == "ADD_SUBSCRIPTION":
                    if not subscription:
                        print(ErrorCodes.SUBSCRIPTION_NOT_FOUND)

                    category = SubscriptionCategory[parts[1]]
                    plan_type = PlanType[parts[2]]
                    print(category, plan_type)
                    result = subscription_service.add_subscription(category, plan_type)
                    if result:
                        print("E", result)  # Print any errors (like DUPLICATE_CATEGORY)
                        break

                # ADD_TOPUP Command
                elif command == "ADD_TOPUP":
                    if not subscription:
                        print(ErrorCodes.SUBSCRIPTION_NOT_FOUND)
                        continue
                    topup_name = parts[1]
                    months = int(parts[2])
                    result = topup_service.add_topup(TopupType[topup_name], months)
                    if result:
                        print(result)
                        break

                # PRINT_RENEWAL_DETAILS Command
                elif command == "PRINT_RENEWAL_DETAILS":
                    if not subscription:
                        print(ErrorCodes.SUBSCRIPTION_NOT_FOUND)
                        continue
                    renewal_service.get_renewal_details()

                else:
                    print("INVALID_INPUT")

    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Input file path from command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = "inputs/sample_input1.txt"
    input_file = sys.argv[1]
    process_commands(input_file)

print(1)

# import os
# import sys
# from models.subscription import Subscription
# from services.subscription_service import SubscriptionService
# from services.topup_service import TopupService
# from services.renewal_service import RenewalService
# from enums.subscription_category import SubscriptionCategory
# from enums.plan_type import PlanType
# from enums.topup_type import TopupType
# from constants.error_codes import ErrorCodes


# def process_commands(input_file):
#     """
#     Process input commands from a single input file and print the output.
#     """
#     try:
#         # Initialize core objects
#         subscription = None
#         subscription_service = None
#         topup_service = None
#         renewal_service = None

#         # Read file line-by-line
#         with open(input_file, "r") as file:
#             for line in file:
#                 parts = line.strip().split()

#                 if not parts:
#                     continue

#                 command = parts[0]

#                 # START_SUBSCRIPTION Command
#                 if command == "START_SUBSCRIPTION":
#                     start_date = parts[1]
#                     subscription = Subscription(start_date)
#                     subscription_service = SubscriptionService(subscription)
#                     topup_service = TopupService(subscription)
#                     renewal_service = RenewalService(subscription)

#                 # ADD_SUBSCRIPTION Command
#                 elif command == "ADD_SUBSCRIPTION":
#                     if not subscription:
#                         print("INVALID_INPUT")
#                         continue

#                     category = SubscriptionCategory[parts[1]]
#                     plan_type = PlanType[parts[2]]

#                     result = subscription_service.add_subscription(category, plan_type)
#                     if result:
#                         print(result)  # Print any errors (like DUPLICATE_CATEGORY)

#                 # ADD_TOPUP Command
#                 elif command == "ADD_TOPUP":
#                     if not subscription:
#                         print("INVALID_INPUT")
#                         continue

#                     topup_name = parts[1]
#                     months = int(parts[2])

#                     result = topup_service.add_topup(TopupType[topup_name], months)
#                     if result:
#                         print(result)  # Print errors (like DUPLICATE_TOPUP)

#                 # PRINT_RENEWAL_DETAILS Command
#                 elif command == "PRINT_RENEWAL_DETAILS":
#                     if not subscription:
#                         print("INVALID_INPUT")
#                         continue

#                     # Use RenewalService to calculate and print output
#                     renewal_service.calculate_renewal_reminders()

#                 else:
#                     print("INVALID_INPUT")

#     except Exception as e:
#         print(f"Error occurred while processing {input_file}: {e}")


# def process_folder(input_folder):
#     """
#     Process all files in the input folder and execute commands.
#     """
#     if not os.path.exists(input_folder):
#         print("Invalid folder path")
#         sys.exit(1)

#     # Iterate over all files in the folder
#     for file_name in os.listdir(input_folder):
#         file_path = os.path.join(input_folder, file_name)

#         # Only process .txt files
#         if file_name.endswith(".txt"):
#             print(f"Processing file: {file_name}")
#             process_commands(file_path)
#             print("-" * 50)


# if __name__ == "__main__":
#     # Input folder path from command-line arguments
#     if len(sys.argv) != 2:
#         print("Usage: python main.py <input_folder>")
#         sys.exit(1)

#     input_folder = sys.argv[1]
#     process_folder(input_folder)
