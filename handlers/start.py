from telegram.update import Update, Message
from telegram.ext.callbackcontext import CallbackContext

GREETING = "Привет!\nЯ могу построить таблицу истинности " \
           ", просто напиши булевую функцию и я выведу результат." \
           "\nДля того чтобы увидеть как символами записать какую-либо операцию напиши /ops, " \
            "работает для таких переменных: x, y, z, t" \
           "\n\nАвтор: @Zikim"


def start(update: Update, context: CallbackContext):
    message: Message = update.message
    message.reply_text(GREETING)
