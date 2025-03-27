from telegram.ext import Application
from handlers import get_handlers
from config import TOKEN
from data_retriever import some_function_name

def main():
    app = Application.builder().token(TOKEN).build()

    # Handlerləri əlavə edirik
    for handler in get_handlers():
        app.add_handler(handler)

    print("Bot işə düşdü...")
    app.run_polling()

if __name__ == "__main__":
    main()
