from aioyoutube.exeptions import (
    VariableTypeError, VariableValueError
)


def search_validation(coroutine):
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
