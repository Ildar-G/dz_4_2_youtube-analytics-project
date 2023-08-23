import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.__channel_id = channel_id
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        snippet = channel['items'][0]['snippet']
        statistics = channel['items'][0]['statistics']

        self.__name = snippet['title']
        self.__description = snippet['description']
        self.__url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.__subscriber_count = int(statistics['subscriberCount'])
        self.__video_count = int(statistics['videoCount'])
        self.__view_count = int(statistics['viewCount'])

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__channel_id, indent=2, ensure_ascii=False))
