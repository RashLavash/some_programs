# Bot()
# Update()
from telegram import Bot
import asyncio
USER_ID = 1711747429


async def main():
    bot = Bot(token='your token')
    # massage = 'Salamaleykum'
    # Отправка сообщения
    # await bot.send_message(USER_ID, massage)
    # Отправка изображения
    photo_ref = 'https://wallpapers.com/images/featured/picture-en3dnh2zi84sgt3t.jpg'
    await bot.send_photo(USER_ID, photo_ref)

asyncio.run(main())