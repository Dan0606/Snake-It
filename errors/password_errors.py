from .error import Error

class WrongPasswordError(Error):
    """WrongPasswordError Exeception raised when trying to log in with wrong password

    Args:
        Error (error.Error): Base class for custom errors
    """
    def __init__(self, message_type = "showerror", message = "Incorrect Password"):
        super().__init__(message_type, message)

class SamePasswordError(Error):
    """SamePasswordError Exepction raised when changing password to current password

    Args:
        Error (error.Error): Base class for custom errors
    """
    def __init__(self, message_type = "showerror", message="Can't change password to the current password"):
        super().__init__(message_type, message)