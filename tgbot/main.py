from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters,
    CallbackQueryHandler
) 
from get_token import GetToken
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.constants import ParseMode

from random import randint, choice, shuffle

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

async def Quiz(update:Update, context=ContextTypes.DEFAULT_TYPE):
    eded_1 = randint(0, 100) # 5
    eded_2 = randint(0, 100) # 8

    emeller = ["+","-","*", "/"] # *
    emel = choice(emeller)

    sual = f"{eded_1}{emel}{eded_2}" # 5*8
    cavab = eval(sual) # 40
    sual += "=?"


    variant_a = cavab
    variant_b = randint(0, 1000)
    variant_c = randint(0, 1000)

    options = [
        InlineKeyboardButton(text=variant_a, callback_data=variant_a),
        InlineKeyboardButton(text=variant_b, callback_data=variant_b),
        InlineKeyboardButton(text=variant_c, callback_data=variant_c),
    ]

    shuffle(options)

    options_markup = InlineKeyboardMarkup(inline_keyboard=[options])

    await update.effective_chat.send_message(
            text=sual, 
            reply_markup=options_markup,
            parse_mode=ParseMode.HTML
        )

async def CheckAnswer(update:Update, context=ContextTypes.DEFAULT_TYPE):
    cavab = str(update.callback_query.data)
    sual = update.callback_query.message.text
    sual = sual[0:len(sual)-2]
    dogru_cavab = str(eval(sual))
    
    if cavab == dogru_cavab:
        await update.effective_chat.send_message("Cavabin doğrudur!!")
        await context.bot.delete_message(update.effective_chat.id, update.callback_query.message.id)

 
if __name__ == "__main__":
    MYTOKEN = GetToken()

    application = ApplicationBuilder().token(MYTOKEN).build()
    application.add_handler(CommandHandler("salamla", Salamla)) 
    application.add_handler(CommandHandler("quiz", Quiz)) 
    application.add_handler(CallbackQueryHandler(CheckAnswer))
    application.add_handler(MessageHandler(filters.TEXT, ReplyToMessage))
    application.run_polling()

 