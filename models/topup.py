from enums.topup_type import TopupType
from constants.error_codes import ErrorCodes


class Topup:
    def __init__(self, topup_type: str, months: int):
        self.topup_type = topup_type
        if not isinstance(topup_type, TopupType):
            raise ValueError(ErrorCodes.INVALID_TOPUP_TYPE)

        details = topup_type.get_details()
        self.duration = details["duration"] * months
        self.devices = details["devices"]
        self.cost = details["cost"] * months

    def get_details(self):
        return {
            "topup_type": self.topup_type.name,
            "devices": self.devices,
            "duration_in_months": self.duration,
            "total_cost": self.cost,
        }
