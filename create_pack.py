from create_buffer import *
import telebot
from send_pack import send
from time import *

def create_pack(one_buffer, one_pack, bot, channel_id):
    for i in range (one_pack):
        photos = createbuff(one_buffer)
        print(photos)
        media = [telebot.types.InputMediaPhoto(open(photo, 'rb').read()) for photo in photos]
        print(media)
        send(media, bot, channel_id, photos)
    sleep(15)

