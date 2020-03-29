from telegram.update import Update, Message
from telegram.ext.callbackcontext import CallbackContext
from bool_operations import bool_operations, basic_funcs,  bool_operations_desc


OPERATIONS_DESC = "Операции:\n"


def operations(update: Update, context: CallbackContext):
    message: Message = update.message
    message.reply_text(OPERATIONS_DESC)


def generate_operations_desc():
    global OPERATIONS_DESC
    for operation, operation_desc in bool_operations_desc.items():
        OPERATIONS_DESC += f"{bool_operations[operation] if operation in bool_operations else basic_funcs[operation]} " \
                           f"- {operation_desc}\n"
    OPERATIONS_DESC += "! - отрицание"


generate_operations_desc()
