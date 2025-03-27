from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from questions import get_question  # Google Sheets-dən alınan sualları istifadə edirik

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Salam! IQ Test botuna xoş gəldiniz. Başlamaq üçün /test yazın.")

async def test(update: Update, context: CallbackContext):
    question, options, correct_answer = get_question(level='normal')  # 'normal' səviyyəsi
    options_text = "\n".join([f"{i+1}. {option}" for i, option in enumerate(options)])
    await update.message.reply_text(f"Sual: {question}\nCavab variantları:\n{options_text}")

# Handlerləri qaytarmaq
def get_handlers():
    return [
        CommandHandler("start", start),
        CommandHandler("test", test),
        ]
