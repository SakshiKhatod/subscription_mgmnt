class add_subscription_failed_exception(Exception):
     def __init__(self,message):
        self.message = message
        super().__init__(f'{message}')