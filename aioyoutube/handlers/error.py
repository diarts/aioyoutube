from aiohttp.client_exceptions import ContentTypeError
from functools import wraps

from aioyoutube.exeptions import *


def response_error_handler(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator checker api response."""

        try:
            json = await coroutine(*args, **kwargs)
        except ContentTypeError as err:
            url = err.request_info.url
            raise WrongApiName(mess=(
                f'Wrong api name "{url.parts[-1]}" has been passed '
                f'into request url.'
            ))

        if json.get('error'):
            reason = json['error']['errors'][0]['reason']
            message = json['error']['message']
            code = json['error']['code']

            if code == 400:
                if reason == 'keyInvalid':
                    key = kwargs.get('key')
                    raise InvalidApiKey(code=400, json=json, mess=(
                        f'Passed youtube api key:{key} is invalid.'
                    ))
                elif reason == 'unknownPart':
                    raise UnknownField(code=400, json=json, mess=(
                        f'Unknown parameter: {message} has been passed.'
                    ))
                elif reason == 'invalidParameter':
                    raise InvalidParameterValue(code=400, json=json, mess=(
                        'One of passed parameters value is not '
                        f'allowed: {message}.'
                    ))
                elif reason == 'invalidPageToken':
                    token = kwargs.get('page_token')
                    raise InvalidPageToken(code=400, json=json, mess=(
                        f'Passed invalid page token {token}.'
                    ))
                elif reason == 'processingFailure':
                    raise ProcessingFailure(code=400, json=json, mess=(
                        "Youtube can't process request, try repeat after "
                        "some time later."
                    ))
                elif reason == 'missingRequiredParameter':
                    raise MissingRequiredParameter(code=400, json=json, mess=(
                        "Some required parameter has been miss."
                    ))
                elif reason == 'unexpectedParameter':
                    raise UnexpectedParameter(code=400, json=json, mess=(
                        'Unexpected parameter has been passed.'
                    ))

            elif code == 401:
                if reason == 'authorizationRequired':
                    raise NoAuthorized(code=401, json=json, mess=(
                        'Request required OAuth2 authorization.'
                    ))

            elif code == 403:
                if reason in ('dailyLimitExceededUnreg', 'quotaExceeded'):
                    raise ExceededDailyLimit(code=403, json=json, mess=(
                        f'Day request limit for api key {kwargs.get("key")} '
                        'was exceeded.'
                    ))
                elif reason == 'channelClosed':
                    raise ChannelClosed(code=403, json=json, mess=(
                        f'Channel {kwargs.get("channel_id")} was closed.'
                    ))
                elif reason == 'channelSuspended':
                    raise ChannelSuspended(code=403, json=json, mess=(
                        f'Channel {kwargs.get("channel_id")} was suspended.'
                    ))
                elif reason == 'forbidden':
                    raise ForbiddenError(code=403, json=json, mess=(
                        f'Some of the parameter passed: {args}, {kwargs}, work'
                        ' only with OAuth2 authenticated app.'
                    ))

            elif code == 404:
                if reason == 'channelNotFound':
                    raise ChannelNotExist(code=404, json=json, mess=(
                        f"Channel {kwargs.get('channel_id')} doesn't exist."
                    ))
                elif reason == 'contentOwnerAccountNotFound':
                    raise InvalidOwnerAccount(code=404, json=json, mess=(
                        f"Owner account not found."
                    ))
                elif reason == 'videoNotFound':
                    raise InvalidVideoId(code=404, json=json, mess=(
                        f"Video with passed id:{kwargs.get('id')} "
                        "doesn't exist."
                    ))

        return json

    return wrapper


def comment_threads_error_handler(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator checker api comments response."""
        video_id = kwargs.get('video_id')

        json = await coroutine(*args, **kwargs)

        if json.get('error'):
            reason = json['error']['errors'][0]['reason']

            if json['error']['code'] == 403:
                if reason == 'commentsDisabled':
                    raise CommentsDisabled(code=403, json=json, mess=(
                        f'Comments for video: {video_id}, is disabled.'
                    ))

        return json

    return wrapper


def comments_error_handler(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator checker api comments response."""
        parent_id = kwargs.get('parentId')

        json = await coroutine(*args, **kwargs)

        if json.get('error'):
            reason = json['error']['errors'][0]['reason']

            if json['error']['code'] == 404:
                if reason == 'commentNotFound':
                    raise InvalidCommentThreadId(code=404, json=json, mess=(
                        f"Comment thread with id={parent_id} doesn't exist."
                    ))

        return json

    return wrapper


def channels_error_handler(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator checker api channels response."""
        channel_id = kwargs.get('channel_id')
        user_name = kwargs.get('user_name')

        json = await coroutine(*args, **kwargs)

        if not json.get('items') and not json.get('error'):
            if user_name:
                raise InvalidUserName(json=json, mess=(
                    f"Channel with user name {user_name} doesn't exist."
                ))
            elif channel_id:
                raise ChannelNotExist(code=404, json=json, mess=(
                    f"Channel with id {channel_id} doesn't exist."
                ))

        elif json.get('error'):
            reason = json['error']['errors'][0]['reason']

            if json['error']['code'] == 400:
                if reason == 'invalidChannelId':
                    raise InvalidChannelId(code=400, json=json, mess=(
                        f'Passed channel id parameter: {channel_id} is invalid.'
                    ))

            if json['error']['code'] == 403:
                if reason == 'channelForbidden':
                    raise ChannelForbidden(code=403, json=json, mess=(
                        f"Channel with id {channel_id} doesn't support "
                        "requests."
                    ))

        return json

    return wrapper


def playlist_items_error_handler(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator checker api playlist items response."""
        playlist_id = kwargs.get('playlist_id')

        json = await coroutine(*args, **kwargs)

        if json.get('error'):
            reason = json['error']['errors'][0]['reason']

            if json['error']['code'] == 403:
                if reason == 'playlistItemsNotAccessible':
                    raise PlaylistItemsNotAccessible(code=403, json=json, mess=(
                        f'Playlist with id={playlist_id} required OAuth2 '
                        f'authorization.'
                    ))
                elif reason == 'watchHistoryNotAccessible':
                    raise HistoryNotAccessible(code=403, json=json, mess=(
                        f"Items of playlist 'history' can't be get through API."
                    ))
                elif reason == 'watchLaterNotAccessible':
                    raise WatchLaterNotAccessible(code=403, json=json, mess=(
                        f"Items of playlist 'watch later' can't be get "
                        f"through API."
                    ))

            if json['error']['code'] == 404:
                if reason == 'playlistNotFound':
                    raise InvalidPlaylistId(code=404, json=json, mess=(
                        f"Playlist with id {kwargs.get('playlist_id')} "
                        "doesn't exist."
                    ))

        return json

    return wrapper


def playlist_error_handler(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator checker api playlist response."""

        json = await coroutine(*args, **kwargs)

        if json.get('error'):
            reason = json['error']['errors'][0]['reason']

            if json['error']['code'] == 403:
                if reason == 'playlistForbidden':
                    raise PlaylistForbidden(code=403, json=json, mess=(
                        "Request playlist required OAuth2 authentication "
                        "or doesn't support api requests."
                    ))

        return json

    return wrapper
