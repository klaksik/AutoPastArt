from create_pack import *
from toplivo import *

bot = telebot.TeleBot('6058119719:AAF_GK3rEl2TF8aNZMxOl7bEdPdaAhmQv3s')
channel_id = "-1001925057183"
one_buffer = 6
one_pack = 1
path = f'ph/'

while True:
    create_pack(one_buffer, one_pack, bot, channel_id)
    bot.send_message('888031887', f'осталось {toplivo(path)} артов, этого хватит на {(toplivo(path)/6)/4} часа')

    sleep(900) #спим



