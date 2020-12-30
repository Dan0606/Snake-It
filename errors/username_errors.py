from .error import Error

class SameUserNameError(Error):
    """SamePasswordError Exepction raised when changing username to current username

    Args:
        Error (error.Error): Base class for custom errors
    """
    def __init__(self, message_type = "showerror", message = "Can't change username to current username"):
        super().__init__(message_type, message)

class UserNameExistsError(Error):
    """SamePasswordError Exepction raised when changing username to current username

    Args:
        Error (error.Error): Base class for custom errors
    """
    def __init__(self, message_type = "showerror", message = "Username is taken!"):
        super().__init__(message_type, message)

class UserNameNotFoundError(Error):
    """UserNameNotFoundError Exeption raised for errors in get_post_by_name function
    
    Args:
        Error (error.Error): Base class for custom errors
    """
    def __init__(self, message_type = "showerror", message = "Incorrect username!"):
        super().__init__(message_type, message)