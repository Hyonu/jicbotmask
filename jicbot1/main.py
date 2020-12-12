import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from fastai.vision import load_learner

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text(
        "Si usted no tiene mascarilla es un maricon :V"
    )
    
def help_command(update, context):
    update.message.reply_text('mande foto de su cara, si no tiene mascarilla es petardo')

def main():
    updater = Updater(token="1383569100:AAFvzKVpq1ptELh165jr8d-eF21csC95gKQ", use_context=True)
    dp = updater.dispatcher    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))    
    updater.start_polling()
    updater.idle()
    
    if __name__ == '__main__':
     main()

def load_model():
    global model
    model = load_learner('/model.pkl')
    print('Model loaded')

def detect_mask(update, context):
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download('user_photo.jpg')
    
    label = model.predict('user_photo.jpg')[0]
    if label == "with_mask":
        update.message.reply_text(
            "Parece que usted tiene mascarilla, felicidades usted no es maricon!"
        )
    else:
        update.message.reply_text(
            "pongase una mascarilla, maricon :v"
        )

