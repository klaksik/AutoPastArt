from create_pack import *
from toplivo import *
from create_toplivo import downloading
from threading import Thread
def main():
    bot = telebot.TeleBot('6058119719:AAF_GK3rEl2TF8aNZMxOl7bEdPdaAhmQv3s')
    channel_id = "-1001925057183"
    one_buffer = 6
    one_pack = 1
    path = f'ph/'
    print("a")
    while True:
        create_pack(one_buffer, one_pack, bot, channel_id)
        bot.send_message('888031887', f'осталось {toplivo(path)} артов, этого хватит на {(toplivo(path)/6)/4} часа')
        sleep(900) #спим


thread1 = Thread(target=main)
thread1.start()
thread2 = Thread(target=downloading("order%3Arank"))
thread2.start()
