import logging
from aiogram import Bot, Dispatcher, executor,types
import os
import settings


API_TOKEN = os.getenv(TOKEN)

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):

    await message.photo[-1].download('test.jpg')
    os.system('python art.py')
    await message.reply_document(open('ascii_image_full.txt', 'rb'))
    
    
    
    
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
