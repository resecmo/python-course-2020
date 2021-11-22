import json
from urllib.parse import quote

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests


def search_image(query):
    print(query)

    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"

    querystring = {"pageNumber": "1", "pageSize": "1", "q": quote(query), "autoCorrect": "true"}

    headers = {
        'x-rapidapi-key': CONFIG["search_api_key"],
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
        }

    print(querystring)
    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text, type(response.text))
    resp = json.loads(response.text)
    if resp["totalCount"] == 0:
        raise ValueError("no pictures found")
    else:
        return resp["value"][0]["url"]


CONFIG_FILE = 'botconfig'
with open(CONFIG_FILE, "r") as file:
    CONFIG = json.load(file)

secret_token = CONFIG["token"]

bot = Bot(token=secret_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    try:
        image_url = search_image(message.text)
        await message.answer_photo(image_url)
    except ValueError as e:
        assert str(e) == "no pictures found"
        await message.answer(str(e))


if __name__ == '__main__':
    executor.start_polling(dp)
