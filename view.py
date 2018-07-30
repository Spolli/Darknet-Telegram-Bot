#!/usr/bin/env python
import telegram.ext
from subprocess import Popen, PIPE, call

bot_token = "630471052:AAFISIj7ZMAauSTPtzjEZEVBuyubOXCofb4"


def get_file_url(method):
  return "https://api.telegram.org/file/bot{}/{}".format(bot_token, method)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    bot.send_photo(chat_id=update.message.chat.id, photo=open("./mtasmr.jpeg", 'rb'))
    update.message.reply_text("Ciaoo era da un anno che ti aspettavo... Comunque questo è un bot che riconosce gli oggetti nelle foto che mandi!")

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Nessun aiuto.')

def trigger(bot, update):
    update.message.reply_text("Stai zitta cagnolina!" + u'\U0001F415')

def echoPhoto(bot, update):
    """Echo the user message."""

    bot.get_file(update.message.photo[-1].file_id).download('./darknet/data/photo.jpeg')
    update.message.reply_text("Foto Scaricata!")
    bot.send_chat_action(chat_id=update.message.chat.id, action=telegram.ChatAction.TYPING)
    p = Popen(["./darknet", "detect", "cfg/yolov3.cfg", "yolov3.weights", "data/photo.jpeg"], stdout=PIPE, stderr=PIPE, cwd=r"./darknet")
    stdout, stderr = p.communicate()
    bot.send_chat_action(chat_id=update.message.chat.id, action=telegram.ChatAction.UPLOAD_PHOTO)
    bot.send_photo(chat_id=update.message.chat.id, photo=open("./darknet/predictions.png", 'rb'))
    update.message.reply_text("Scansione Completata!")

def echoAudio(bot, update):
    bot.send_chat_action(chat_id=update.message.chat.id, action=telegram.ChatAction.UPLOAD_AUDIO)
    bot.send_voice(chat_id=update.message.chat.id, voice=open('tests/telegram.ogg', 'rb'))

def echoVideo(bot, update):
    bot.get_file(update.message.video[-1].file_id).download('./darknet/data/video.mp4')
    bot.send_chat_action(chat_id=update.message.chat.id, action=telegram.ChatAction.TYPING)
    p = Popen(["./darknet", "detect", "demo", "cfg/coco.data", "cfg/yolov3.cfg", "yolov3.weights", "data/video.mp4"], stdout=PIPE, stderr=PIPE, cwd=r"./darknet")
    stdout, stderr = p.communicate()
    bot.send_chat_action(chat_id=update.message.chat.id, action=telegram.ChatAction.UPLOAD_VIDEO)
    bot.send_document(chat_id=update.message.chat.id, document=open('./darknet/predictions.mp4', 'rb'))

def echoText(bot, update):
    update.message.reply_text(update.message.text)
