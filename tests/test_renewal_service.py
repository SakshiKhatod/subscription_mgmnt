# import unittest
# from src.services.renewal_service import RenewalService
# from src.models.subscription import Subscription
# from datetime import datetime
# from src.enums.subscription_category import SubscriptionCategory
# from src.enums.plan_type import PlanType


# class TestRenewalService(unittest.TestCase):

#     def setUp(self):

#         self.subscription = Subscription("01-01-2022")
#         self.renewal_service = RenewalService(self.subscription)

#     def test_calculate_renewal_date(self):

#         renewal_date = self.renewal_service.calculate_renewal_dates()
#         expected_renewal_date = "01-02-2022"
#         self.assertEqual(renewal_date, expected_renewal_date)

#     def test_calculate_total_renewal_amount(self):

#         # Assuming subscription and topup services have been set up properly
#         self.subscription.add_subscription(
#             SubscriptionCategory.MUSIC, PlanType.PERSONAL
#         )
#         self.subscription.add_topup("FOUR_DEVICE")
#         renewal_amount = self.renewal_service.calculate_total_cost()
#         expected_amount = 100 + 50
#         self.assertEqual(renewal_amount, expected_amount)


# if __name__ == "__main__":
#     unittest.main()

import unittest
from models.subscription import Subscription
from services.renewal_service import RenewalService
from enums.subscription_category import SubscriptionCategory
from models.plan import Plan
from enums.plan_type import PlanType

import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


class TestRenewalService(unittest.TestCase):

    def setUp(self):
        self.subscription = Subscription(start_date="20-02-2022")
        self.subscription.plans[SubscriptionCategory.MUSIC] = Plan(
            PlanType.PERSONAL, SubscriptionCategory.MUSIC
        )
        self.service = RenewalService(self.subscription)

    def test_calculate_renewal_dates(self):
        renewal_dates = self.service.calculate_renewal_dates()
        self.assertIn(SubscriptionCategory.MUSIC, renewal_dates)
        self.assertEqual(renewal_dates[SubscriptionCategory.MUSIC], "10-03-2022")

    def test_calculate_total_cost(self):
        total_cost = self.service.calculate_total_cost()
        self.assertEqual(total_cost, 100)

    def test_get_renewal_details(self):
        details = self.service.get_renewal_details()
        self.assertIn("RENEWAL_REMINDER MUSIC 10-03-2022", details)
        self.assertIn(
            "RENEWAL_AMOUNT 100", details
        )  # Replace 100 with actual total cost


if __name__ == "__main__":
    unittest.main()
