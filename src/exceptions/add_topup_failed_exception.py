class AddTopupFailedException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(f"{message}")

class DuplicateTopupFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(f"{message}")

        

