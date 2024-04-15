class BaseOrderException(Exception):
    default_message = "An error occurred."

    def __init__(self, message=None):
        self.message = message or self.default_message
        super().__init__(self.message)


class RoomBookedException(BaseOrderException):
    default_message = "Room is already booked for the given date."


class InvalidBookingDatesException(BaseOrderException):
    default_message = "Start date must be before end date!"
