from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import wget
updater = Updater(token='867568023:AAHd9URjy8m0j_Dxl8s0lMSdnLC_sk28f8U', use_context=True)

dispatcher = updater.dispatcher

# function handler for start command
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Welcome to the Meme Generator!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# function handler for help command
def help(update,context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Send us an image as a 'photo' in the telegram bot, and receive a Meme-ified image")

help_handler = CommandHandler('help',help)
dispatcher.add_handler(help_handler)

# function handler for images
def handle_images(update,context):
    # getting the link of the image on telegram server
    file = context.bot.getFile(update.message.photo[-1].file_id)
    file_path = file.file_path

    # location to download the image
    image_path = "./Telegram_Images"

    # downloading the image using wget, assigning the file path to downloaded_file
    downloaded_file = wget.download(file_path,image_path)

    # detect labels
    # rank the labels
    # make an image with the caption

    # sending the image over telegram bot
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open(downloaded_file, 'rb'))

    context.bot.send_message(chat_id=update.message.chat_id,text = "Do you like the meme?")

image_handler = MessageHandler(Filters.photo,handle_images)
dispatcher.add_handler(image_handler)

updater.start_polling()
