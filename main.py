import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 بوت الهكر الحلال شغال 100% 🔥\nاكتب /gold")

async def gold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سعر الذهب: 85,000 دينار عيار 21")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("gold", gold))
app.run_polling()
