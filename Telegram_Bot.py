import telebot
# print(telebot.__version__)
token = '867568023:AAHd9URjy8m0j_Dxl8s0lMSdnLC_sk28f8U'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):
	bot.send_message(msg.chat.id, "Howdy, how are you doing?")

@bot.message_handler(content_types=['photo'])
def picture(msg):
    print("entered photo")
    file_id = msg.json['photo'][0]['file_id']
    file_url = bot.download_file(file_id)
    print(file_url)
    bot.send_message(msg.chat.id,"picture has been sent")

@bot.message_handler(content_types=['document'])
def document_picture(msg):
    if(msg.document.mime_type in ["image/png","image/jpeg","image/jpg"]):
        print(msg)
        bot.send_message(msg.chat.id,"picture has been sent")


bot.polling()
