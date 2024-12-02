class invalid_date_exception(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(f'{message}')