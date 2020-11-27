import json

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests


def search_image(query):

    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"

    querystring = {"pageNumber": "1", "pageSize": "1", "q": query, "autoCorrect": "true"}

    headers = {
        'x-rapidapi-key': CONFIG["search_api_key"],
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text


CONFIG_FILE = 'botconfig'
with open(CONFIG_FILE, "r") as file:
    CONFIG = json.load(file)

# PROXY_URL = 'socks5://xxx.xxx.xxx.xxx'  # Вставить здесь подходящий IP

secret_token = CONFIG["token"]

bot = Bot(token=secret_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(search_image(message.text))


if __name__ == '__main__':
    executor.start_polling(dp)