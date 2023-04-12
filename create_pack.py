from create_buffer import *
import telebot
from del_files_from_array import *
from time import *


def create_pack(one_buffer, one_pack, bot, channel_id):
    for i in range(one_pack):
        photos = createbuff(one_buffer)
        print(photos)

        media = [telebot.types.InputMediaPhoto(open(photo, 'rb').read()) for photo in photos]
        print(media)


        try:
            bot.send_media_group(channel_id, media=media)
        except:
            print("смерть")
        finally:
            del_files_from_array(photos)
        sleep(15)
