import telebot  # Library to interact with Telegram Bot API

# Replace with your actual Telegram Bot Token
BOT_TOKEN = "7586628867:AAGrFV1TwqHZboLzivG_vT0K1qkWZD38u3o"

# Initialize the Telegram bot using the provided token
bot = telebot.TeleBot(BOT_TOKEN)

# This handler listens for the /start command.
@bot.message_handler(commands=["start"])
def start(message):
    # Send a simple welcome message to the user
    bot.send_message(message.chat.id, "Hello! Welcome to our simple Telegram bot.")

# Start the bot so it listens for incoming messages
if __name__ == "__main__":
    bot.infinity_polling()
