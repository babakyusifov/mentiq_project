from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from questions import get_question  # Google Sheets-dən alınan sualları istifadə edirik
from scores import add_score, update_score

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Salam! IQ Test botuna xoş gəldiniz. Başlamaq üçün /test yazın.")

async def test(update: Update, context: CallbackContext):
    question, options, correct_answer = get_question(level='normal')  # 'normal' səviyyəsi
    options_text = "\n".join([f"{i+1}. {option}" for i, option in enumerate(options)])
    await update.message.reply_text(f"Sual: {question}\nCavab variantları:\n{options_text}")

    # Cavabı yoxlamaq üçün istifadəçi cavabını saxlayırıq
    context.user_data['correct_answer'] = correct_answer

async def answer(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_answer = update.message.text

    if 'correct_answer' in context.user_data:
        correct_answer = context.user_data['correct_answer']
        if user_answer == correct_answer:
            add_score(user_id, 10)
            await update.message.reply_text("Doğru cavab! 10 puan qazandınız.")
        else:
            await update.message.reply_text("Yanlış cavab. Təəssüf ki, puan qazana bilmədiniz.")

        # İstifadəçinin yenilənmiş skorunu göstəririk
        score = update_score(user_id)
        await update.message.reply_text(f"Sizin ümumi skorunuz: {score}")

# Handlerləri qaytarmaq
def get_handlers():
    return [
        CommandHandler("start", start),
        CommandHandler("test", test),
        MessageHandler(filters.TEXT & ~filters.COMMAND, answer)
    ]
