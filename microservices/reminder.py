from datetime import datetime, timedelta
from constants.constant import NO_OF_DAYS_BEFORE_TO_NOTIFY, NO_OF_DAYS_IN_A_MONTH


def calculate_reminder_date(subscription_start_date: datetime, months: int) -> datetime:
    expiration_date = subscription_start_date + timedelta(
        days=NO_OF_DAYS_IN_A_MONTH * months
    )
    reminder_date = expiration_date - timedelta(days=NO_OF_DAYS_BEFORE_TO_NOTIFY)
    return reminder_date
 