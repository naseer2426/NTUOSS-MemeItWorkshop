# image detection and ranking images to find the best matching text
from Image_Detection import label_detection
import pandas as pd
data_path = "./Database/database.xls"
data = pd.read_excel(data_path)
labels = data['Labels'].tolist()
text = data['Text'].tolist()

# importing library to write text onto an image
from Image_Writing import make_meme
import random

def best_text(recieved_image_labels):
    max_matches = -1
    max_index = []
    for i,curr_labels in enumerate(labels):
        # print(text[i],end="\n\n")
        if(text[i]!="" and type(text[i])==str):
            # curr_labels = curr_labels.split(' , ')
            count = 0
            # print(recieved_image_labels,curr_labels)
            for j in recieved_image_labels:
                if j in curr_labels:
                    # print("got here")
                    count+=1
            if(count==max_matches):
                max_index.append(i)
            if(count>max_matches):
                # print("got here also")
                max_matches = count
                max_index = [i]
    out_index = random.choice(max_index)
    return text[out_index]


# telegram bot starting
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
    labels = label_detection(downloaded_file)
    print(labels)

    # rank the labels to find the text of best fit
    picture_text = best_text(labels)
    # print(picture_text)
    # make an image with the caption
    make_meme("",picture_text,downloaded_file)
    make_meme(picture_text,"",downloaded_file,2)
    
    # sending the image over telegram bot
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open("./Completed/output1.png", 'rb'))

    context.bot.send_message(chat_id=update.message.chat_id,text = "Do you like the meme?")

    context.bot.send_photo(chat_id=update.message.chat_id, photo=open("./Completed/output2.png", 'rb'))
    context.bot.send_message(chat_id=update.message.chat_id,text = "Or do you like this better?")


image_handler = MessageHandler(Filters.photo,handle_images)
dispatcher.add_handler(image_handler)

updater.start_polling()
