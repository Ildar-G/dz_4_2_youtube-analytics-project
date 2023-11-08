import os
from googleapiclient.discovery import build


class Video:
    """Класс для представления информации о видео на YouTube."""
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        """Инициализирует объект класса Video с помощью данных из YouTube API."""
        self.__video_id = video_id
        try:
            video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                        id=video_id
                                                        ).execute()
            self.__title = video_response['items'][0]['snippet']['title']
            self.__url = f"https://www.youtube.com/watch?v={self.__video_id}"
            self.__view_count = int(video_response['items'][0]['statistics']['viewCount'])
            self.__like_count = int(video_response['items'][0]['statistics']['likeCount'])
        except IndexError:
            print(f"Видео с id={video_id} не существует")
            self.__title = None
            self.__url = None
            self.__view_count = None
            self.__like_count = None

    @property
    def video_id(self) -> str:
        """Возвращает идентификатор видео на YouTube."""
        return self.__video_id

    @property
    def title(self) -> str:
        """Возвращает название видео."""
        return self.__title

    @property
    def url(self) -> str:
        """Возвращает ссылку на видео."""
        return self.__url

    @property
    def view_count(self) -> int:
        """Возвращает количество просмотров видео."""
        return self.__view_count

    @property
    def like_count(self) -> int:
        """Возвращает количество лайков видео."""
        return self.__like_count

    def __str__(self):
        """Возвращает строковое представление объекта Video (название видео)."""
        return f"{self.__title}"


class PLVideo(Video):
    """
    Класс для представления информации о видео на YouTube в рамках плейлиста.
    """

    def __init__(self, video_id: str, playlist_id: str) -> None:
        """
        Инициализирует объект класса PLVideo с помощью данных из YouTube API.
        """
        self.__playlist_id = playlist_id
        super().__init__(video_id)

    @property
    def playlist_id(self) -> str:
        """Возвращает идентификатор плейлиста, к которому принадлежит видео."""
        return self.__playlist_id
