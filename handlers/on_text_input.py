from telegram.update import Update, Message
from telegram.ext.callbackcontext import CallbackContext
from builder import build_truth_table
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DEFAULT_BOOL_VARS = ["x", "y", "z", "t"]


def on_text_input(update: Update, context: CallbackContext):
    message: Message = update.message
    bool_vars = [default_bool_var for default_bool_var in DEFAULT_BOOL_VARS if default_bool_var in message.text]

    logger.info(f'function: "{message.text}" bool vars: [{",".join(bool_vars)}]')

    res = f"{' '.join(bool_vars)} | result\n"

    truth_table = build_truth_table(message.text, bool_vars)
    for set_number, value in enumerate(truth_table):
        row = ""
        for i in range(len(bool_vars))[::-1]:
            row += f"{1 if set_number & 2**i else 0} "
        row += f"| {1 if value else 0}" + "\n"
        res += row

    message.reply_text(res, quote=True)
