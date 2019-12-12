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


class InvalidOwnerAccount(RequestValidationError):
    """Exception raises when passed owner account doesn't exist."""
    pass


class MissingRequiredParameter(RequestValidationError):
    """Exception raises when missed required parameter."""
    pass


class UnexpectedParameter(RequestValidationError):
    """Exception raises when unexpected parameter has been passed."""
    pass


class WrongApiName(YoutubeApiError):
    """Exception raises when request parameter "name" contained
    nonexistent api name."""
    pass


class ProcessingFailure(YoutubeApiError):
    """Exception raises when api can't process request. Try repeat this
     request after some time later, if this error was raised."""
    pass


class InvalidParameterValue(RequestValidationError):
    """Exception raises when passed parameter value not allowed."""
    pass


class InvalidUserName(InvalidParameterValue):
    """Exception raises when response of api method "getting youtube
    channel data by user name" not contains items."""
    pass


class NoAuthorized(RequestValidationError):
    """Exception raises when request required OAuth2 authorization."""
    pass
