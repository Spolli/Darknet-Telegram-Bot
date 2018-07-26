#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from urllib.request import urlopen
import logging
from view import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bot_token = "630471052:AAFISIj7ZMAauSTPtzjEZEVBuyubOXCofb4"

def get_url(method):
    return "https://api.telegram.org/file/bot{}/{}".format(bot_token, method)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(bot_token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("vaffanculo", trigger))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.photo, echoPhoto))
    dp.add_handler(MessageHandler(Filters.text, echoText))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.start_webhook(listen='127.0.0.1', port=5002, url_path=bot_token)
    #updater.bot.set_webhook(url='https://0.0.0.0/' + bot_token)
    updater.idle()

if __name__ == '__main__':
    main()
