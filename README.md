# Aioyoutube
- [About](#about)
- [Usage](#usage)

## About
Aioyoutube is a Python async wrapper for youtube.com REST API.

## Usage
Note:
```
For use aioyoutube package, you must create youtube application 
and generate API application key. You can do it 
on https://console.developers.google.com
```

### Install package
```
pip install aioyoutube
```

### Use api
All description of youtube api methods you can find on
[youtube api page](https://developers.google.com/youtube/v3/docs).
All api method names in package match with youtube api method names.

Currently implemented methods: 
- search
- comments
- commentThreads
- channels
- playlistItems
- playlists
- videos

Exapmple using youtube api method "search":
```python
import asyncio
from aioyoutube import Api

api = Api()

loop = asyncio.get_event_loop()
search = api.search(
    key='your application key',
    text='search text'
)
task = loop.create_task(search)
result = loop.run_until_complete(task)
```

