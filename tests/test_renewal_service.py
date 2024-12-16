import unittest
from services.renewal_service import RenewalService
from models.subscription import Subscription
from datetime import datetime
from enums.subscription_category import SubscriptionCategory
from enums.plan_type import PlanType


class TestRenewalService(unittest.TestCase):

    def setUp(self):

        self.subscription = Subscription("01-01-2022")
        self.renewal_service = RenewalService(self.subscription)

    def test_calculate_renewal_date(self):

        renewal_date = self.renewal_service.calculate_renewal_dates()
        expected_renewal_date = "01-02-2022"
        self.assertEqual(renewal_date, expected_renewal_date)

    def test_calculate_total_renewal_amount(self):

        # Assuming subscription and topup services have been set up properly
        self.subscription.add_subscription(
            SubscriptionCategory.MUSIC, PlanType.PERSONAL
        )
        self.subscription.add_topup("FOUR_DEVICE")
        renewal_amount = self.renewal_service.calculate_total_cost()
        expected_amount = 100 + 50
        self.assertEqual(renewal_amount, expected_amount)


if __name__ == "__main__":
    unittest.main()
