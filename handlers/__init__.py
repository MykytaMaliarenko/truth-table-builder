from telegram import Message
from telegram.ext import Dispatcher, MessageHandler, Filters

from .start import start
from .on_text_input import on_text_input
from .operations import operations

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

text_handlers = {
    "start": start,
    "ops": operations
}

default_handler = on_text_input


def error_handler(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    message: Message = update.message
    message.reply_text("Во время обработки этого сообщения произошла ошибка, попробуйте еще раз.", quote=True)


def register_handlers(dp: Dispatcher):
    for command in text_handlers:
        dp.add_handler(MessageHandler(Filters.regex('^/{}$'.format(command)), text_handlers[command]))

    dp.add_handler(MessageHandler(Filters.text, default_handler))

    # log all errors
    dp.add_error_handler(error_handler)
