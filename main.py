import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# تفعيل اللوق عشان تشوف الاخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# التوكن مالتك من BotFather
TOKEN = "8254865492:AAGbD9cZ5XRtDZU4H1E0ZXjWGsl5vIbvT64"

# من /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"🔥 هلا {user.first_name} 🔥\n"
        f"بوت الهكر الحلال شغال 100%\n\n"
        f"ارسل اي شي واجاوبك 👊"
    )

# من يدز اي رسالة
async
