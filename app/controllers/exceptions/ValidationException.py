class ValidationException(Exception):
    def __init__(self, message, field):
        super().__init__(message)
        self.field = field