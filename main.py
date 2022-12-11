import logging
from imlofunc import checkword
from aiogram import Bot, Dispatcher, executor, types
from transliterate import to_cyrillic, to_latin

API_TOKEN = '5837863967:AAGuGVLisjQj81sm2jU_S760UAf9y0qIzlw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def Salom(message: types.Message):
    await message.reply(f"Assalomu aleykum botimizga xush kelibsiz.\
                        \nBotdan foydalanishni bilmasangiz /help ni bosing")
@dp.message_handler(commands=['help'])
async def Yordam(message: types.Message):
    matn = f"Botga kiril lotin alifbosi yordamida matn yuboring.\n"
    matn += f"Bot sizning imlo xatoingizni aniqlab javob beradi!"
    await message.answer(matn)



@dp.message_handler()
async def Imloxato(message: types.Message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if to_cyrillic(msg) else to_latin(msg)
    if len(message.text)==1:
        word = str(javob).text
        resul = checkword(word)
        if resul['available']:
            response = f"✅ {word.capitalize()}"
            await message.answer(response)

    if len(message.text)>1:
        word = str(javob(msg)).split()
        listt = []
        for words in word:
            words = words
            listt.append(word)
            resul = checkword(words)
            if resul['available']:
                response = f"✅ {words.capitalize()}"
                await message.answer(response)
            else:
                response = f"❌ {words.capitalize()}\n"
                for text in resul['matches']:
                    response += f"✅ {text.capitalize()}\n"
                await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)