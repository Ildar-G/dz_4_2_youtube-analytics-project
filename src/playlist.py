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

    def get_video_details(self) -> List[dict]:
        """
        Получает детали видео для видео в плейлисте.
        """
        playlist_videos = youtube.playlistItems().list(
            playlistId=self.playlist_id,
            part='contentDetails',
            maxResults=50,
        ).execute()
        video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        video_response = youtube.videos().list(
            part='contentDetails',
            id=','.join(video_ids)
        ).execute()

        return video_response['items']

    def total_duration(self) -> datetime.timedelta:
        """
        Вычисляет общую продолжительность всех видео в плейлисте.
        """
        video_details = self.get_video_details()
        total_duration = sum(
            [isodate.parse_duration(video['contentDetails']['duration'])
             for video in video_details],
            datetime.timedelta()
        )
        return total_duration

    def show_best_video(self) -> str:
        """
        Находит и возвращает URL видео с наибольшим количеством лайков в плейлисте.
        """
        video_details = self.get_video_details()
        best_video_id = None
        max_likes = 0

        for video in video_details:
            video_id = video['id']
            video_response = youtube.videos().list(
                part='statistics',
                id=video_id
            ).execute()
            like_count = int(video_response['items'][0]['statistics']['likeCount'])
            if like_count > max_likes:
                max_likes = like_count
                best_video_id = video_id

        best_video_url = f"https://youtu.be/{best_video_id}"
        return best_video_url



