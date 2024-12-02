import constants
class Final_Subscription:
    def __init__(self) -> None:
        __start_date_of_subscription=""
        __subscriptionlist=constants.SUBSCRIPTION_CATEGORY_PLAN_MAPPING
        __subscription_status=constants.SUBSCRIPTION_STATUS
        __topup_status=None
        __no_of_months_for_topup=0
        __device_type=constants.DEVICE_TYPE

    def doremi_subscription(self):
        __start_date_of_subscription=""
        __subscriptionlist=constants.SUBSCRIPTION_CATEGORY_PLAN_MAPPING
        __subscription_status=constants.SUBSCRIPTION_STATUS[2]
        __topup_status=None
        __no_of_months_for_topup=0
        __device_type=constants.DEVICE_TYPE
