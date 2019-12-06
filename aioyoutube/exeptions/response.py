from .base import YoutubeApiError


class ResponseApiError(YoutubeApiError):
    """Base class for api response exceptions."""
    pass


class UnknownField(ResponseApiError):
    """Exception raises when passed parameter has wrong value."""
    pass


class InvalidApiKey(ResponseApiError):
    """Exception raises when passed parameter "key" is invalid."""
    pass


class InvalidVideoId(ResponseApiError):
    """Exception raises when passed parameter "videoId" is invalid."""
    pass


class InvalidPageToken(ResponseApiError):
    """Exception raises when passed parameter "pageToken" is invalid."""
    pass


class InvalidPlaylistId(ResponseApiError):
    """Exception raises when playlist with passed id doesn't exist."""
    pass


class InvalidParameterValue(ResponseApiError):
    """Exception raises when passed parameter value not allowed."""
    pass


class InvalidUserName(InvalidParameterValue):
    """Exception raises when response of api method "getting youtube
    channel data by user name" not contains items."""
    pass
