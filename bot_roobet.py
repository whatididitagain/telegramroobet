import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN", "8863397866:AAEvqI2Hh77cYfoz8Avga0ABrOj66C-g1Bc")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
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
    bot.reply_to(message, text)

print("Roobet bot started...")
bot.infinity_polling()
