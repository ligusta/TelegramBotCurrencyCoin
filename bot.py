import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import requests
PORT = int(os.environ.get('PORT', 80))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = 'YOUR_API_TOKEN'


def get_prices():
    coins = ["BTC", "ETH", "XRP", "LTC", "BCH",
             "ADA", "DOT", "LINK", "BNB", "XLM"]

    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
        }

    return data


def start(update, context):
    chat_id = update.effective_chat.id
    message = ""

    message += f"DESCRIPTION"

    context.bot.send_message(chat_id=chat_id, text=message)


def tokens(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        message += f"Монета: {coin}\nЦена: ${price:,.2f}\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)


def btc(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for _ in crypto_data:
        i = "BTC"
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        message += f"Монета: {coin}\nЦена: ${price:,.2f}\n\n"
        break

    context.bot.send_message(chat_id=chat_id, text=message)


def eth(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for _ in crypto_data:
        i = "ETH"
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        message += f"Монета: {coin}\nЦена: ${price:,.2f}\n\n"
        break

    context.bot.send_message(chat_id=chat_id, text=message)


def xrp(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for _ in crypto_data:
        i = "XRP"
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        message += f"Монета: {coin}\nЦена: ${price:,.2f}\n\n"
        break

    context.bot.send_message(chat_id=chat_id, text=message)


def ltc(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for _ in crypto_data:
        i = "LTC"
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        message += f"Монета: {coin}\nЦена: ${price:,.2f}\n\n"
        break

    context.bot.send_message(chat_id=chat_id, text=message)


def bch(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for _ in crypto_data:
        i = "BCH"
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        message += f"Монета: {coin}\nЦена: ${price:,.2f}\n\n"
        break

    context.bot.send_message(chat_id=chat_id, text=message)


def ada(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for _ in crypto_data:
        i = "ADA"
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        message += f"Монета: {coin}\nЦена: ${price:,.2f}\n\n"
        break

    context.bot.send_message(chat_id=chat_id, text=message)


def dot(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for _ in crypto_data:
        i = "DOT"
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        message += f"Монета: {coin}\nЦена: ${price:,.2f}\n\n"
        break

    context.bot.send_message(chat_id=chat_id, text=message)


def link(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for _ in crypto_data:
        i = "LINK"
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        message += f"Монета: {coin}\nЦена: ${price:,.2f}\n\n"
        break

    context.bot.send_message(chat_id=chat_id, text=message)


def bnb(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for _ in crypto_data:
        i = "BNB"
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        message += f"Монета: {coin}\nЦена: ${price:,.2f}\n\n"
        break

    context.bot.send_message(chat_id=chat_id, text=message)


def xlm(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for _ in crypto_data:
        i = "XLM"
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        message += f"Монета: {coin}\nЦена: ${price:,.2f}\n\n"
        break

    context.bot.send_message(chat_id=chat_id, text=message)


def main():

    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("tokens", tokens))
    dispatcher.add_handler(CommandHandler("btc", btc))
    dispatcher.add_handler(CommandHandler("eth", eth))
    dispatcher.add_handler(CommandHandler("xrp", xrp))
    dispatcher.add_handler(CommandHandler("ltc", ltc))
    dispatcher.add_handler(CommandHandler("bch", bch))
    dispatcher.add_handler(CommandHandler("ada", ada))
    dispatcher.add_handler(CommandHandler("dot", dot))
    dispatcher.add_handler(CommandHandler("link", link))
    dispatcher.add_handler(CommandHandler("bnb", bnb))
    dispatcher.add_handler(CommandHandler("xlm", xlm))

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + TOKEN)

    updater.idle()


if __name__ == "__main__":
    main()