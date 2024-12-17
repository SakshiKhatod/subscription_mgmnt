# import unittest
# from models.subscription import Subscription
# from enums.subscription_category import SubscriptionCategory
# from enums.plan_type import PlanType
# from services.subscription_service import SubscriptionService
# from constants.error_codes import ErrorCodes


# class TestSubscriptionService(unittest.TestCase):

#     def setUp(self):
#         self.subscription = Subscription("01-01-2022")
#         self.service = SubscriptionService(self.subscription)

#     def test_add_subscription_valid(self):
#         result = self.service.add_subscription(
#             SubscriptionCategory.MUSIC, PlanType.PERSONAL
#         )
#         self.assertIsNone(result)
#         self.assertIn(SubscriptionCategory.MUSIC, self.subscription.plans)

#     def test_add_subscription_duplicate_category(self):
#         self.service.add_subscription(SubscriptionCategory.MUSIC, PlanType.PERSONAL)
#         result = self.service.add_subscription(
#             SubscriptionCategory.MUSIC, PlanType.PERSONAL
#         )
#         self.assertEqual(result, ErrorCodes.DUPLICATE_CATEGORY)

#     def test_add_subscription_invalid_plan(self):
#         result = self.service.add_subscription(
#             SubscriptionCategory.VIDEO, "INVALID_PLAN"
#         )
#         self.assertEqual(result, ErrorCodes.INVALID_PLAN_TYPE)


# if __name__ == "__main__":
#     unittest.main()
import unittest
from src.models.subscription import Subscription
from src.services.subscription_service import SubscriptionService
from src.enums.subscription_category import SubscriptionCategory
from src.enums.plan_type import PlanType
from src.constants.error_codes import ErrorCodes

import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


class TestSubscriptionService(unittest.TestCase):

    def setUp(self):
        self.subscription = Subscription(start_date="01-01-2024")
        self.service = SubscriptionService(self.subscription)

    def test_add_subscription_valid(self):
        result = self.service.add_subscription(
            SubscriptionCategory.MUSIC, PlanType.PERSONAL
        )
        self.assertIsNone(result)
        self.assertIn(SubscriptionCategory.MUSIC, self.subscription.plans)

    def test_add_subscription_duplicate(self):
        self.service.add_subscription(SubscriptionCategory.MUSIC, PlanType.PERSONAL)
        result = self.service.add_subscription(
            SubscriptionCategory.MUSIC, PlanType.PREMIUM
        )
        self.assertEqual(result, ErrorCodes.DUPLICATE_CATEGORY)

    def test_add_subscription_invalid_category(self):
        result = self.service.add_subscription("INVALID", PlanType.PERSONAL)
        self.assertEqual(result, ErrorCodes.INVALID_CATEGORY)


if __name__ == "__main__":
    unittest.main()
