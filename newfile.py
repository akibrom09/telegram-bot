from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📚 Education Channel", url="https://t.me/SCORE4POINT")],
        [InlineKeyboardButton("💼 Education Channel 2", url="https://t.me/freshmanpackage")],
        [InlineKeyboardButton("🎥 technology news", url="https://t.me/tigraytechn")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome! Choose a category below:",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()