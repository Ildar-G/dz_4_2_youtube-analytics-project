
class PlayList:
    """
    Плейлист YouTube и предоставляет методы для получения информации о плейлисте.
    """

    def __init__(self, playlist_id: str):
        self.playlist_id = playlist_id
        self.title, self.url = self.get_playlist_info()
    def get_playlist_info(self) -> tuple[str, str]: