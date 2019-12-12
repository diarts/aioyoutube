from .base import YoutubeApiError


class ResponseApiError(YoutubeApiError):
    """Base class for api response exceptions."""
    pass


class ForbiddenError(ResponseApiError):
    """Exception raises when api work only for app with OAuth2.0
    authentication."""
    pass


class UnknownField(ResponseApiError):
    """Exception raises when passed parameter has wrong value."""
    pass


class InvalidChannelId(ResponseApiError):
    """Exception raises when passed parameter "channelId" is invalid."""
    pass


class InvalidApiKey(ResponseApiError):
    """Exception raises when passed parameter "key" is invalid."""
    pass


class InvalidVideoId(ResponseApiError):
    """Exception raises when passed parameter "videoId" is invalid."""
    pass


class InvalidCommentThreadId(ResponseApiError):
    """Exception raises when passed parameter "parentId" is invalid."""
    pass


class InvalidPageToken(ResponseApiError):
    """Exception raises when passed parameter "pageToken" is invalid."""
    pass


class InvalidPlaylistId(ResponseApiError):
    """Exception raises when playlist with passed id doesn't exist."""
    pass


class CommentsDisabled(ResponseApiError):
    """Exception raises when video comments is closed."""
    pass


class ChannelForbidden(ResponseApiError):
    """Exception raises when channel doesn't support the request."""
    pass


class PlaylistItemsNotAccessible(ResponseApiError):
    """Exception raises when playlist required OAuth2 authorization."""
    pass


class HistoryNotAccessible(ResponseApiError):
    """Exception raises when try getting playlist "history" items. Items
    of playlist "history" cannot be retrieved through the API."""
    pass


class PlaylistForbidden(ResponseApiError):
    """Exception raises when request playlist doesn't support the request
    or required OAuth2 authorization."""
    pass


class WatchLaterNotAccessible(ResponseApiError):
    """Exception raises when try getting playlist "watch later" items. Items
    of playlist "watch later" cannot be retrieved through the API."""
    pass
