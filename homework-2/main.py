from src.channel import Channel
import pprint

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # получаем значения атрибутов
    pprint.pprint(moscowpython.title)  # MoscowPython
    pprint.pprint(moscowpython.video_count)  # 685 (может уже больше)
    pprint.pprint(moscowpython.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A
    pprint.pprint(moscowpython.view_count)

    # менять не можем
    moscowpython.channel_id = 'Новое название'
    pprint.pprint(moscowpython.channel_id)
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    pprint.pprint(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'moscowpython.json' в данными по каналу
    moscowpython.to_json('moscowpython.json')
