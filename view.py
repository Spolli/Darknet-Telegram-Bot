#!/usr/bin/env python

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
    filePath = bot.get_file(update.message.photo[-1].file_id).file_path
    #filePath = file.file_path
    bot.send_photo(chat_id=update.message.chat.id, photo=open(get_file_url(filePath), 'rb'))
    #update.message.reply_text(img=urlopen(photo).read())

def echoText(bot, update):
    update.message.reply_text(update.message.text)
