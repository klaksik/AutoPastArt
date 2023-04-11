from del_files_from_array import *
def send(media, bot, channel_id, photos):
    try:
        bot.send_media_group(channel_id, media=media)
    except:
        print("смерть")
    finally:
        del_files_from_array(photos)