# from subscription_mgmnt.models import music,video,podcast
from constants.constant import NO_OF_DAYS_BEFORE_TO_NOTIFY
from dateutil.relativedelta import relativedelta
class Subscription:

    def __init__(
        self,
        subscription_date,
        subscription_category,
        subscription_plan,
        category_plan_dict,
    ) -> None:

        self.subscription_date = subscription_date
        self.subscription_category = subscription_category
        self.subscription_plan = subscription_plan
        self.category_plan_dict = category_plan_dict
        self.subscription_cost = None
        self.subscription_month = None
        self.reminder_date = None
        self.reminder_days = NO_OF_DAYS_BEFORE_TO_NOTIFY
        self.__set_subscription_plan_detils()

    def __set_subscription_plan_detils(self):

        plan_details = self.category_plan_dict.get(self.subscription_plan)
        if plan_details:
            self.subscription_cost = plan_details["subscription_price"]
            self.subscription_month = plan_details["subscription_validity"]

    def calculate_renewal_reminder_date(self):
        if self.subscription_date and self.subscription_month:
            self.reminder_date=self.subscription_date+relativedelta(months=self.subscription_month)-relativedelta(days=self.reminder_days)
        

    def __repr__(self) -> str:
        if self.reminder_date:
            return f""
        return ""

    


# subclass_dict={
#     MUSIC:Music,
#     VIDEO:Video
#     PODCAST:Podcast

# }
