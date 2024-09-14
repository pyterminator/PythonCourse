from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
) 
from get_token import GetToken
from telegram import Update

from telegram.constants import ParseMode

async def ReplyToMessage(update:Update, context=ContextTypes.DEFAULT_TYPE):
    if update.message.text == "Salam":
        my_message = "Aleykum Salam!"
    else:
        my_message = "sadlmasiudgasud"

    await update.message.reply_text(
        my_message,
        reply_to_message_id=update.message.id,
        parse_mode=ParseMode.HTML 
    )


async def Salamla(update:Update, context=ContextTypes.DEFAULT_TYPE):
    await update.effective_chat.send_message("Salam, necəsən ?")
    print("Salam Dunya!")

if __name__ == "__main__":
    MYTOKEN = GetToken()

    application = ApplicationBuilder().token(MYTOKEN).build()
    application.add_handler(CommandHandler("salamla", Salamla))
    application.add_handler(MessageHandler(filters.TEXT, ReplyToMessage))
    application.run_polling()


