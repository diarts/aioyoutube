from aioyoutube.exeptions import YoutubeApiError


class RequestValidationError(YoutubeApiError):
    """Base class for validation exceptions api request data."""
    pass


class VariableTypeError(RequestValidationError):
    """Exception raises when request passed parameters has wrong type."""
    pass


class VariableValueError(RequestValidationError):
    """Exception raises when request passed parameters has wrong value."""
    pass


class ExceededDailyLimit(RequestValidationError):
    """Exception raises when request daily limit was exceeded."""
    pass


class ChannelClosed(RequestValidationError):
    """Exception raises when target channel was closed."""
    pass


class ChannelSuspended(RequestValidationError):
    """Exception raises when target channel was suspended."""
    pass


class ChannelNotExist(RequestValidationError):
    """Exception raises when target channel doesn't exist."""
    pass


class WrongApiName(YoutubeApiError):
    """Exception raises when request parameter "name" contained
    nonexistent api name."""
    pass
