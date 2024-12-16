import unittest
from models.topup import Topup
from services.topup_service import TopupService
from enums.topup_type import TopupType
from constants.error_codes import ErrorCodes


class TestTopupService(unittest.TestCase):
    def setUp(self):
        self.service = TopupService()

    def test_add_topup_valid(self):
        result = self.service.add_topup(TopupType.FOUR_DEVICE)
        self.assertIsNone(result)
        self.assertIsInstance(self.service.topup, Topup)

    def test_add_topup_invalid_type(self):
        result = self.service.add_topup("INVALID_TOPUP")
        self.assertEqual(result, ErrorCodes.INVALID_TOPUP_TYPE)


if __name__ == "__main__":
    unittest.main()
