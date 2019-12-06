from aiohttp.client_exceptions import ContentTypeError

from aioyoutube.exeptions import (
    UnknownField,
    WrongApiName,
    InvalidApiKey,
    InvalidVideoId,
    InvalidParameterValue,
    InvalidUserName,
    InvalidPageToken,
    InvalidPlaylistId,
    ExceededDailyLimit,
    ChannelClosed,
    ChannelNotExist,
    ChannelSuspended,
)


def response_error_handler(coroutine):
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
                    raise InvalidApiKey(code=400, mess=(
                        f'Passed youtube api key:{key} is invalid.'
                    ))
                elif reason == 'unknownPart':
                    raise UnknownField(code=400, mess=(
                        f'Unknown parameter: {message} has been passed.'
                    ))
                elif reason == 'invalidParameter':
                    raise InvalidParameterValue(code=400, mess=(
                        'One of passed parameters value is not '
                        f'allowed: {message}.'
                    ))
                elif reason == 'invalidPageToken':
                    token = kwargs.get('page_token')
                    raise InvalidPageToken(code=400, mess=(
                        f'Passed invalid page token {token}.'
                    ))

            elif code == 403:
                if reason == 'dailyLimitExceededUnreg':
                    raise ExceededDailyLimit(code=403, mess=(
                        f'Day request limit for api key {kwargs.get("key")} '
                        f'was exceeded.'
                    ))
                elif reason == 'channelClosed':
                    raise ChannelClosed(code=403, mess=(
                        f'Channel {kwargs.get("channel_id")} was closed.'
                    ))
                elif reason == 'channelSuspended':
                    raise ChannelSuspended(code=403, mess=(
                        f'Channel {kwargs.get("channel_id")} was suspended.'
                    ))

            elif code == 404:
                if reason == 'channelNotFound':
                    raise ChannelNotExist(code=404, mess=(
                        f"Channel {kwargs.get('channel_id')} doesn't exist."
                    ))

        return json

    return wrapper


def comments_error_handler(coroutine):
    async def wrapper(*args, **kwargs):
        """Decorator checker api comments response."""

        json = await coroutine(*args, **kwargs)

        if json.get('error'):
            reason = json['error']['errors'][0]['reason']

            if json['error']['code'] == 404:
                if reason == 'videoNotFound':
                    video_id = kwargs.get('video_id')
                    raise InvalidVideoId(code=404, mess=(
                        f"Video with passed id:{video_id} doesn't exist."
                    ))

        return json

    return wrapper


def channels_error_handler(coroutine):
    async def wrapper(*args, **kwargs):
        """Decorator checker api channels response."""

        json = await coroutine(*args, **kwargs)

        if not json.get('items'):
            channel_id = kwargs.get('channel_id')
            user_name = kwargs.get('user_name')

            if user_name:
                raise InvalidUserName(mess=(
                    f"Channel with user name {user_name} doesn't exist."
                ))
            elif channel_id:
                raise ChannelNotExist(code=404, mess=(
                    f"Channel with id {channel_id} doesn't exist."
                ))

        return json

    return wrapper


def playlist_items_error_handler(coroutine):
    async def wrapper(*args, **kwargs):
        """Decorator checker api playlist items response."""

        json = await coroutine(*args, **kwargs)

        if json.get('error'):
            reason = json['error']['errors'][0]['reason']

            if json['error']['code'] == 404:
                if reason == 'playlistNotFound':
                    raise InvalidPlaylistId(code=404, mess=(
                        f"Playlist with id {kwargs.get('playlist_id')} "
                        "doesn't exist."
                    ))

        return json

    return wrapper
