import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8863397866:AAEvqI2Hh77cYfoz8Avga0ABrOj66C-g1Bc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎰 Roobet — BONUS2026\n\n"
        "🔑 Promo code: BONUS2026\n"
        "🔗 Sign up: https://roobet.com/?ref=bonus2026\n\n"
        "💰 $100,000 Weekly Cash Drops\n\n"
        "Every week $100K is distributed among active players\n"
        "automatically — no extra steps needed.\n\n"
        "📋 How to get started:\n\n"
        "1️⃣ Sign up via the link above\n"
        "2️⃣ Enter code BONUS2026 at registration\n"
        "3️⃣ Start playing and get your share of $100K weekly\n\n"
        "✅ Good luck!"
    )
    await update.message.reply_text(text)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Roobet bot started...")
    app.run_polling()
