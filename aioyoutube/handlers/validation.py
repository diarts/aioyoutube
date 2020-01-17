from functools import wraps
from aioyoutube.exeptions import (
    VariableTypeError, VariableValueError
)


def search_validation(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator validate passed parameters for api method getting
        search result."""

        acceptable_order = (
            'date', 'rating', 'relevance', 'title', 'videoCount', 'viewCount',
        )
        acceptable_search_by = (
            'video', 'channel', 'playlist',
        )

        key = kwargs.get('key')
        text = kwargs.get('text')
        max_results = kwargs.get('max_results')
        page_token = kwargs.get('page_token')
        order = kwargs.get('order')
        published_after = kwargs.get('published_after')
        published_before = kwargs.get('published_before')
        search_by = kwargs.get('search_by')

        if key and not isinstance(key, str):
            raise VariableTypeError(
                f'Argument "key" must be an str, current type is {type(key)}.'
            )
        elif text and not isinstance(text, str):
            raise VariableTypeError(
                f'Argument "text" must be an str, current type is {type(text)}.'
            )
        elif max_results and not isinstance(max_results, int):
            raise VariableTypeError(
                'Argument "max_results" must be an int, current type is'
                f' {type(max_results)}.'
            )
        elif max_results and not 0 <= max_results <= 50:
            raise VariableValueError(
                'Argument "max_result" must be in range from 1 to 50, '
                f'current value is {max_results}.'
            )
        elif page_token and not isinstance(page_token, str):
            raise VariableTypeError(
                'Argument "page_token" must be an str, current type is '
                f'{type(page_token)}.'
            )
        elif order and not isinstance(order, str):
            raise VariableTypeError(
                'Argument "order" must be an str, current type is '
                f'{type(order)}.'
            )
        elif order and order not in acceptable_order:
            raise VariableValueError(
                'Acceptable values for argument "order" is '
                f'{acceptable_order}, current value is {order}.'
            )
        elif published_after and not isinstance(published_after, int):
            raise VariableTypeError(
                'Argument "published_after" must be an int, current type is '
                f'{type(published_after)}.'
            )
        elif published_before and not isinstance(published_before, int):
            raise VariableTypeError(
                'Argument "published_before" must be an int, current type is '
                f'{type(published_before)}.'
            )
        elif search_by and not isinstance(search_by, str):
            raise VariableTypeError(
                'Argument "search_by" must be an str, current type is '
                f'{type(search_by)}.'
            )
        elif search_by and search_by not in acceptable_search_by:
            raise VariableValueError(
                'Acceptable values for argument "search_by" is '
                f'{acceptable_search_by}, current value is {search_by}.'
            )

        return await coroutine(*args, **kwargs)

    return wrapper


def comment_threads_validation(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator validate passed parameters for api method getting
        video comment_threads."""
        acceptable_part = ('id', 'replies', 'snippet',)
        acceptable_order = ('time', 'relevance',)
        acceptable_text_format = ('plainText', 'html',)

        key = kwargs.get('key')
        part = kwargs.get('part')
        video_id = kwargs.get('video_id')
        max_results = kwargs.get('max_results')
        page_token = kwargs.get('page_token')
        order = kwargs.get('order')
        text_format = kwargs.get('text_format')
        search_text = kwargs.get('search_text')

        if key and not isinstance(key, str):
            raise VariableTypeError(
                f'Argument "key" must be an str, current type is {type(key)}.'
            )
        elif part and not isinstance(part, list):
            raise VariableTypeError(
                'Argument "part" must be an list, current type is'
                f' {type(part)}.'
            )
        elif part and not all(isinstance(item, str) for item in part):
            raise VariableTypeError(
                'Argument "part" must contain only str.'
            )
        elif part and not all(item in acceptable_part for item in part):
            raise VariableValueError(
                'Acceptable values for part contain parameter is '
                f'{acceptable_part}, current part contain {part}.'
            )
        elif max_results and not isinstance(max_results, int):
            raise VariableTypeError(
                'Argument "max_results" must be an int, current type is'
                f' {type(max_results)}.'
            )
        elif max_results and not 0 <= max_results <= 100:
            raise VariableValueError(
                'Argument "max_result" must be in range from 1 to 100, '
                f'current value is {max_results}.'
            )
        elif page_token and not isinstance(page_token, str):
            raise VariableTypeError(
                'Argument "page_token" must be an str, current type is '
                f'{type(page_token)}.'
            )
        elif order and not isinstance(order, str):
            raise VariableTypeError(
                'Argument "order" must be an str, current type is '
                f'{type(order)}.'
            )
        elif order and order not in acceptable_order:
            raise VariableValueError(
                'Acceptable values for argument "order" is '
                f'{acceptable_order}, current value is {order}.'
            )
        elif video_id and not isinstance(video_id, str):
            raise VariableTypeError(
                'Argument "video_id" must be an str, current type is'
                f' {type(video_id)}.'
            )
        elif text_format and not isinstance(text_format, str):
            raise VariableTypeError(
                'Argument "text_format" must be an str, current type is'
                f' {type(text_format)}.'
            )
        elif text_format and text_format not in acceptable_text_format:
            raise VariableValueError(
                'Acceptable values for argument "order" is '
                f'{acceptable_text_format}, current value is {text_format}.'
            )
        elif search_text and not isinstance(search_text, str):
            raise VariableTypeError(
                'Argument "search_text" must be an str, current type is'
                f' {type(search_text)}.'
            )

        return await coroutine(*args, **kwargs)

    return wrapper


def comments_validation(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator validate passed parameters for api method getting
        comments from comment_threads."""
        acceptable_part = ('id', 'snippet',)
        acceptable_text_format = ('plainText', 'html',)

        key = kwargs.get('key')
        part = kwargs.get('part')
        max_results = kwargs.get('max_results')
        page_token = kwargs.get('page_token')
        parent_id = kwargs.get('parent_id')
        text_format = kwargs.get('text_format')

        if key and not isinstance(key, str):
            raise VariableTypeError(
                f'Argument "key" must be an str, current type is {type(key)}.'
            )
        elif part and not isinstance(part, list):
            raise VariableTypeError(
                'Argument "part" must be an list, current type is'
                f' {type(part)}.'
            )
        elif part and not all(isinstance(item, str) for item in part):
            raise VariableTypeError(
                'Argument "part" must contain only str.'
            )
        elif part and not all(item in acceptable_part for item in part):
            raise VariableValueError(
                'Acceptable values for part contain parameter is '
                f'{acceptable_part}, current part contain {part}.'
            )
        elif max_results and not isinstance(max_results, int):
            raise VariableTypeError(
                'Argument "max_results" must be an int, current type is'
                f' {type(max_results)}.'
            )
        elif max_results and not 0 <= max_results <= 100:
            raise VariableValueError(
                'Argument "max_result" must be in range from 1 to 100, '
                f'current value is {max_results}.'
            )
        elif page_token and not isinstance(page_token, str):
            raise VariableTypeError(
                'Argument "page_token" must be an str, current type is '
                f'{type(page_token)}.'
            )
        elif text_format and not isinstance(text_format, str):
            raise VariableTypeError(
                'Argument "text_format" must be an str, current type is'
                f' {type(text_format)}.'
            )
        elif text_format and text_format not in acceptable_text_format:
            raise VariableValueError(
                'Acceptable values for argument "order" is '
                f'{acceptable_text_format}, current value is {text_format}.'
            )
        elif parent_id and not isinstance(parent_id, str):
            raise VariableTypeError(
                'Argument "parent_id" must be an str, current type is'
                f' {type(parent_id)}.'
            )

        return await coroutine(*args, **kwargs)

    return wrapper


def channels_validation(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator validate passed parameters for api method getting
            channels data."""
        acceptable_part = (
            'brandingSettings', 'contentDetails', 'contentOwnerDetails', 'id',
            'localizations', 'snippet', 'statistics', 'status', 'topicDetails',
        )

        key = kwargs.get('key')
        part = kwargs.get('part')
        max_results = kwargs.get('max_results')
        channel_id = kwargs.get('channel_id')
        user_name = kwargs.get('user_name')

        if key and not isinstance(key, str):
            raise VariableTypeError(
                f'Argument "key" must be an str, current type is {type(key)}.'
            )
        elif part and not isinstance(part, list):
            raise VariableTypeError(
                'Argument "part" must be an list, current type is'
                f' {type(part)}.'
            )
        elif part and not all(isinstance(item, str) for item in part):
            raise VariableTypeError(
                'Argument "part" must contain only str.'
            )
        elif part and not all(item in acceptable_part for item in part):
            raise VariableValueError(
                'Acceptable values for part contain parameter is '
                f'{acceptable_part}, current part contain {part}.'
            )
        elif max_results and not isinstance(max_results, int):
            raise VariableTypeError(
                'Argument "max_results" must be an int, current type is'
                f' {type(max_results)}.'
            )
        elif max_results and not 0 <= max_results <= 50:
            raise VariableValueError(
                'Argument "max_result" must be in range from 1 to 50, '
                f'current value is {max_results}.'
            )
        elif channel_id and user_name:
            raise VariableValueError(
                'Variable "channel_id" and "user_name" is not compatible, '
                'pass only one of them.'
            )
        elif channel_id and not isinstance(channel_id, str):
            raise VariableTypeError(
                'Argument "channel_id" must be an str, current type'
                f' is {type(channel_id)}.'
            )
        elif user_name and not isinstance(user_name, str):
            raise VariableTypeError(
                'Argument "user_name" must be an str, current type'
                f' is {type(user_name)}.'
            )

        return await coroutine(*args, **kwargs)

    return wrapper


def playlist_items_validation(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator validate passed parameters for api method getting
            playlist items data."""
        acceptable_part = (
            'contentDetails', 'id', 'snippet', 'status',
        )

        key = kwargs.get('key')
        part = kwargs.get('part')
        max_results = kwargs.get('max_results')
        playlist_id = kwargs.get('playlist_id')
        page_token = kwargs.get('page_token')

        if key and not isinstance(key, str):
            raise VariableTypeError(
                f'Argument "key" must be an str, current type is {type(key)}.'
            )
        elif part and not isinstance(part, list):
            raise VariableTypeError(
                'Argument "part" must be an list, current type is'
                f' {type(part)}.'
            )
        elif part and not all(isinstance(item, str) for item in part):
            raise VariableTypeError(
                'Argument "part" must contain only str.'
            )
        elif part and not all(item in acceptable_part for item in part):
            raise VariableValueError(
                'Acceptable values for part contain parameter is '
                f'{acceptable_part}, current part contain {part}.'
            )
        elif max_results and not isinstance(max_results, int):
            raise VariableTypeError(
                'Argument "max_results" must be an int, current type is'
                f' {type(max_results)}.'
            )
        elif max_results and not 0 <= max_results <= 50:
            raise VariableValueError(
                'Argument "max_result" must be in range from 1 to 50, '
                f'current value is {max_results}.'
            )
        elif playlist_id and not isinstance(playlist_id, str):
            raise VariableTypeError(
                'Argument "playlist_id" must be an str, current type is'
                f' {type(playlist_id)}.'
            )
        elif page_token and not isinstance(page_token, str):
            raise VariableTypeError(
                'Argument "page_token" must be an str, current type is '
                f'{type(page_token)}.'
            )

        return await coroutine(*args, **kwargs)

    return wrapper


def playlists_validation(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator validate passed parameters for api method getting
            playlists data."""
        acceptable_part = (
            'contentDetails', 'id', 'snippet', 'status', 'localizations',
            'player',
        )

        key = kwargs.get('key')
        part = kwargs.get('part')
        max_results = kwargs.get('max_results')
        channel_id = kwargs.get('channel_id')
        page_token = kwargs.get('page_token')

        if key and not isinstance(key, str):
            raise VariableTypeError(
                f'Argument "key" must be an str, current type is {type(key)}.'
            )
        elif part and not isinstance(part, list):
            raise VariableTypeError(
                'Argument "part" must be an list, current type is'
                f' {type(part)}.'
            )
        elif part and not all(isinstance(item, str) for item in part):
            raise VariableTypeError(
                'Argument "part" must contain only str.'
            )
        elif part and not all(item in acceptable_part for item in part):
            raise VariableValueError(
                'Acceptable values for part contain parameter is '
                f'{acceptable_part}, current part contain {part}.'
            )
        elif max_results and not isinstance(max_results, int):
            raise VariableTypeError(
                'Argument "max_results" must be an int, current type is'
                f' {type(max_results)}.'
            )
        elif max_results and not 0 <= max_results <= 50:
            raise VariableValueError(
                'Argument "max_result" must be in range from 1 to 50, '
                f'current value is {max_results}.'
            )
        elif channel_id and not isinstance(channel_id, str):
            raise VariableTypeError(
                'Argument "channel_id" must be an str, current type is'
                f' {type(channel_id)}.'
            )
        elif page_token and not isinstance(page_token, str):
            raise VariableTypeError(
                'Argument "page_token" must be an str, current type is '
                f'{type(page_token)}.'
            )

        return await coroutine(*args, **kwargs)

    return wrapper


def videos_validation(coroutine):
    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        """Decorator validate passed parameters for api method getting
            video data."""
        acceptable_part = (
            'contentDetails', 'id', 'liveStreamingDetails', 'localizations',
            'player', 'recordingDetails', 'snippet', 'statistics',
            'status', 'topicDetails',
        )

        key = kwargs.get('key')
        part = kwargs.get('part')
        max_results = kwargs.get('max_results')
        video_ids = kwargs.get('video_ids')
        page_token = kwargs.get('page_token')

        if key and not isinstance(key, str):
            raise VariableTypeError(
                f'Argument "key" must be an str, current type is {type(key)}.'
            )
        elif part and not isinstance(part, list):
            raise VariableTypeError(
                'Argument "part" must be an list, current type is'
                f' {type(part)}.'
            )
        elif part and not all(isinstance(item, str) for item in part):
            raise VariableTypeError(
                'Argument "part" must contain only str.'
            )
        elif part and not all(item in acceptable_part for item in part):
            raise VariableValueError(
                'Acceptable values for part contain parameter is '
                f'{acceptable_part}, current part contain {part}.'
            )
        elif max_results and not isinstance(max_results, int):
            raise VariableTypeError(
                'Argument "max_results" must be an int, current type is'
                f' {type(max_results)}.'
            )
        elif max_results and not 0 <= max_results <= 50:
            raise VariableValueError(
                'Argument "max_result" must be in range from 1 to 50, '
                f'current value is {max_results}.'
            )
        elif video_ids and not isinstance(video_ids, list):
            raise VariableTypeError(
                'Argument "video_ids" must be an list, current type is'
                f' {type(video_ids)}.'
            )
        elif video_ids and not all(isinstance(item, str) for item in video_ids):
            raise VariableTypeError(
                'Argument "video_ids" must contain only str.'
            )
        elif page_token and not isinstance(page_token, str):
            raise VariableTypeError(
                'Argument "page_token" must be an str, current type is '
                f'{type(page_token)}.'
            )

        return await coroutine(*args, **kwargs)

    return wrapper
