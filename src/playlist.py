import os
import datetime
import isodate
from typing import List
from googleapiclient.discovery import build

api_key = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class PlayList:
    """
    Плейлист YouTube и предоставляет методы для получения информации о плейлисте.
    """

    def __init__(self, playlist_id: str):
        self.playlist_id = playlist_id
        self.title, self.url = self.get_playlist_info()

    def get_playlist_info(self) -> tuple[str, str]:
        """
        Информация о видео для видео в плейлисте
        """
        playlist_response = youtube.playlists().list(
            part='snippet',
            id=self.playlist_id
        ).execute()
        playlist_info = playlist_response['items'][0]['snippet']
        title = playlist_info['title']
        url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        return title, url



