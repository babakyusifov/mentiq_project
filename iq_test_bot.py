from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Botun Token-i (bunu Telegram'dan almalıyam)
TOKEN = "7646936369:AAEigQ6aYyUYyrBkY2MiasuYrILai9d3ia0"

# /start komandası
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Salam! IQ Test botuna xoş gəldiniz. Başlamaq üçün /test yazın.")

# Botun əsas funksiyası
def main():
    app = Application.builder().token(TOKEN).build()

    # Komandalar
    app.add_handler(CommandHandler("start", start))

    print("Bot işə düşdü...")
    app.run_polling()

if __name__ == "__main__":
    main()
