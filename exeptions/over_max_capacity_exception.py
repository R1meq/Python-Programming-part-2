class OverMaxCapacityException(Exception):
    """Raised when the ship's cargo load exceeds its maximum capacity"""
    def __init__(self, exception_massage="current load exceeds maximum capacity"):
        self.exception_massage = exception_massage
        super().__init__(self.exception_massage)
