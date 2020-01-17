from aiohttp import ClientSession
from typing import List

from aioyoutube.helpers import insert_name, time_converting
from aioyoutube.handlers import (
    response_error_handler,
    search_validation,
    comment_threads_validation,
    comment_threads_error_handler,
    channels_validation,
    channels_error_handler,
    playlist_items_error_handler,
    playlist_items_validation,
    playlists_validation,
    playlist_error_handler,
    comments_validation,
    comments_error_handler,
    videos_validation,
)

__all__ = [
    'Api',
]


class Api:
    """youtube.com REST API."""
    _API_VERSION = 3
    _API_URL_TEMP = 'https://www.googleapis.com/youtube/v{version}/'

    __slots__ = ('_session', '_api_version', '_api_url')

    def __init__(self, session: ClientSession = None, version: int = None):
        self._session = session or ClientSession
        self._api_version = version or self._API_VERSION
        self._api_url = self._API_URL_TEMP.format(version=self.api_version)

    def __repr__(self):
        return f'<class {self.__class__.__name__} version={self.api_version}>'

    def __str__(self):
        return f'Youtube Api v{self.api_version} requester.'

    @property
    def api_url(self) -> str:
        return self._api_url

    @property
    def api_version(self) -> int:
        return self._api_version

    async def _request(self, method_name: str, params: dict) -> dict:
        """Sending request and getting data from youtube api server.

        Args:
            method_name (str): Request method api name.
            params (dict): Dict of request parameters.

        """
        url = self.api_url + method_name

        async with self._session() as sess:
            async with sess.get(url, params=params) as res:
                return await res.json()

    @search_validation
    @response_error_handler
    @insert_name
    async def search(self, *, key: str, text: str, max_results: int = 50,
                     page_token: str = None, published_after: int = None,
                     published_before: int = None, order: str = 'date',
                     search_by: str = 'video', **kwargs) -> dict:
        """Getting result of searching in youtube service search.

        Args:
            key (str): Key of youtube application, for access to youtube api.
            text (str): Text of searching.
            max_results (int, optional): Count of items in response.
                Minimal value is 1, maximum value is 50. Default value is 50.
            page_token (str, optional): Identifies a specific page in the
                result set that should be returned.
            order (str, optional): Method of response items sorting. Default
                value is "date". Acceptable values are:
                - date – Resources are sorted in reverse chronological
                    order based on the date they were created.
                - rating – Resources are sorted from highest to lowest rating.
                - relevance – Resources are sorted based on their relevance
                    to the search query. This is the default value for
                    this parameter.
                - title – Resources are sorted alphabetically by title.
                - videoCount – Channels are sorted in descending order
                    of their number of uploaded videos.
                - viewCount – Resources are sorted from highest to lowest
                    number of views. For live broadcasts, videos are sorted
                    by number of concurrent viewers while the broadcasts
                    are ongoing.
            published_after (int, optional): Datetime in unixtime format.
                Response will contain items created at or after the
                specified time. If value more then current time, this
                parameter has been ignored.
            published_before (int, optional): Datetime in unixtime format.
                Response will contain items created at or before the
                specified time.
            search_by (str, optional): Type of api response items. Default
                value is "video". Acceptable values: video, channel, playlist.

        """
        params = {
            'key': key,
            'part': 'snippet',
            'q': text,
            'maxResults': max_results,
            'order': order,
            'type': search_by,
        }
        if page_token:
            params['pageToken'] = page_token
        if published_after:
            params['publishedAfter'] = time_converting(published_after)
        if published_before:
            params['publishedBefore'] = time_converting(published_before)

        return await self._request(kwargs.get('name'), params)

    @comment_threads_validation
    @response_error_handler
    @comment_threads_error_handler
    @insert_name
    async def commentThreads(self, *, key: str, part: List[str], video_id: str,
                             max_results: int = 100, order: str = 'time',
                             text_format: str = 'plainText',
                             page_token: str = None, search_text: str = None,
                             **kwargs) -> dict:
        """Getting comment threads for video.

        Args:
            key (str): Key of youtube application, for access to youtube api.
            part (List[str]): Sections list which must contained in response.
                Acceptable part sections: id, replies, snippet.
            video_id (str): Id of youtube video.
            max_results (int, optional): Count of items in response.
                Minimal value is 1, maximum value is 100. Default value is 100.
            page_token (str, optional): Identifies a specific page in the
                result set that should be returned.
            order (str, optional): Method of response items sorting. Default
                value is "time". Acceptable values are:
                - time – Comment threads are ordered by time.
                - relevance – Comment threads are ordered by relevance.
            text_format (str, optional): Type of format response items.
                Default value is "plainText". Acceptable values are:
                - plainText – Returns the comments in plain text format.
                - html – Returns the comments text in HTML format.
            search_text (str, optional): Filtering response comment by text.

        """
        params = {
            'key': key,
            'part': ','.join(part),
            'videoId': video_id,
            'maxResults': max_results,
            'order': order,
            'textFormat': text_format,
        }

        if search_text:
            params['searchTerms'] = search_text
        if page_token:
            params['pageToken'] = page_token

        return await self._request(kwargs.get('name'), params=params)

    @comments_validation
    @response_error_handler
    @comments_error_handler
    @insert_name
    async def comments(self, *, key: str, part: List[str], parent_id: str,
                       max_results: int = 100, text_format: str = 'plainText',
                       page_token: str = None, **kwargs) -> dict:
        """Getting comments for comment thread.

        Args:
            key (str): Key of youtube application, for access to youtube api.
            part (List[str]): Sections list which must contained in response.
                Acceptable part sections: id, replies, snippet.
            parent_id (str): Id of parent comment thread.
            max_results (int, optional): Count of items in response.
                Minimal value is 1, maximum value is 100. Default value is 100.
            page_token (str, optional): Identifies a specific page in the
                result set that should be returned.
            text_format (str, optional): Type of format response items.
                Default value is "plainText". Acceptable values are:
                - plainText – Returns the comments in plain text format.
                - html – Returns the comments text in HTML format.

        """
        params = {
            'key': key,
            'part': ','.join(part),
            'parentId': parent_id,
            'maxResults': max_results,
            'textFormat': text_format,
        }

        if page_token:
            params['pageToken'] = page_token

        return await self._request(kwargs.get('name'), params=params)

    @channels_validation
    @response_error_handler
    @channels_error_handler
    @insert_name
    async def channels(self, *, key: str, part: List[str],
                       max_results: int = 50,
                       channel_id: str = None, user_name: str = None,
                       **kwargs) -> dict:
        """Getting channel data.

        Args:
            key (str): Key of youtube application, for access to youtube api.
            part (List[str]): Sections list which must contained in response.
                Acceptable part sections: brandingSettings, contentDetails,
                contentOwnerDetails, id, localizations, snippet, statistics,
                status, topicDetails.
            max_results (int, optional): Count of items in response.
                Minimal value is 1, maximum value is 50. Default value is 50.

            Acceptable and required only one identifier parameter at the
                same time:
            channel_id (str): Youtube channel id. Can take from
                youtube url: ./channel/<user_id>.
            user_name (str): Youtube channel owner. Can take from
                youtube url: ./user/<user_name>.

        """
        params = {
            'key': key,
            'part': ','.join(part),
            'maxResults': max_results,
        }
        if user_name:
            params['forUsername'] = user_name
        else:
            params['id'] = channel_id

        return await self._request(kwargs.get('name'), params=params)

    @playlist_items_validation
    @response_error_handler
    @playlist_items_error_handler
    @insert_name
    async def playlistItems(self, *, key: str, part: List[str],
                            playlist_id: str, max_results: int = 50,
                            page_token: str = None, **kwargs) -> dict:
        """Getting playlist videos.

        Args:
            key (str): Key of youtube application, for access to youtube api.
            part (List[str]): Sections list which must contained in response.
                Acceptable part sections: contentDetails, id, snippet, status.
            playlist_id (str): Id of playlist which contain videos.
            max_results (int, optional): Count of items in response.
                Minimal value is 1, maximum value is 50. Default value is 50.
            page_token (str, optional): Identifies a specific page in the
                result set that should be returned.

        """
        params = {
            'key': key,
            'part': ','.join(part),
            'playlistId': playlist_id,
            'maxResults': max_results,
        }
        if page_token:
            params['pageToken'] = page_token

        return await self._request(kwargs.get('name'), params=params)

    @playlists_validation
    @response_error_handler
    @playlist_error_handler
    @insert_name
    async def playlists(self, *, key: str, part: List[str], channel_id: str,
                        max_results: int = 50, page_token: str = None,
                        **kwargs) -> dict:
        """Getting channel playlists.

        Args:
            key (str): Key of youtube application, for access to youtube api.
            part (List[str]): Sections list which must contained in response.
                Acceptable part sections: contentDetails, id, snippet, status,
                localizations, player.
            channel_id (str): Youtube channel id. Can take from youtube
                url: ./channel/<user_id>.
            max_results (int, optional): Count of items in response.
                Minimal value is 1, maximum value is 50. Default value is 50.
            page_token (str, optional): Identifies a specific page in the
                result set that should be returned.

            """
        params = {
            'key': key,
            'part': ','.join(part),
            'channelId': channel_id,
            'maxResults': max_results,
        }
        if page_token:
            params['pageToken'] = page_token

        return await self._request(kwargs.get('name'), params=params)

    @videos_validation
    @response_error_handler
    @insert_name
    async def videos(self, *, key: str, part: List[str], video_ids: List[str],
                     max_results: int = 50, page_token: str = None,
                     **kwargs):
        """Getting videos by id.

        Args:
            key (str): Key of youtube application, for access to youtube api.
            part (List[str]): Sections list which must contained in response.
                Acceptable part sections: contentDetails, id,
                liveStreamingDetails, localizations, player, recordingDetails,
                snippet, statistics, status, topicDetails.
            video_ids (List[str]): list of youtube video ids.
            max_results (int, optional): Count of items in response.
                Minimal value is 1, maximum value is 50. Default value is 50.
            page_token (str, optional): Identifies a specific page in the
                result set that should be returned.

        """
        params = {
            'key': key,
            'id': ','.join(video_ids),
            'part': ','.join(part),
            'maxResults': max_results,
        }
        if page_token:
            params['pageToken'] = page_token

        return await self._request(kwargs.get('name'), params=params)
