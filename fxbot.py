import requests
import telegram as tl
import asyncio
from collections import defaultdict


async def getFxData():
    API_KEY = "<YOUR_API_KEY>"
    rate_list = ['USD/KRW', 'JPY/KRW']
    rate_dict = defaultdict(dict)

    for rate in rate_list:
        each_rate = requests.get(url=f'https://api.twelvedata.com/exchange_rate?symbol={rate}&apikey={API_KEY}').json()
        # 엔화인 경우 100엔 기준으로 보기 편하므로 100을 곱해서 100엔 기준으로 리턴
        if rate == "JPY/KRW":
            rate_dict[rate] = each_rate['rate'] * 100
        # 그 외 기준은 1달러로 기준
        else:
            rate_dict[rate] = each_rate['rate']

    return rate_dict


async def main():
    bot = tl.Bot("<YOUR_TELEGRAM_API_KEY>")
    chat_id = <YOUR_TELEGRAM_CHAT_ID>

    rate_dict = await getFxData()
    send_message = ""

    for k, v in rate_dict.items():
        send_message += f"[{k}] : {v:,.2f}원 "

    await bot.sendMessage(chat_id=chat_id, text=send_message)


asyncio.run(main())
