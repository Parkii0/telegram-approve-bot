# telegram-approve-bot
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

TOKEN = "8509321582:AAFlSiaRXv-lx4MsqI0vX3fKMZsKfMWLF1Y"

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(approve))
app.run_polling()
