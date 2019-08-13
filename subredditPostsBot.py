import feedparser
from lxml import etree as ET
import random
from telegram.ext import Updater, CommandHandler
import argparse
import logging


logging.basicConfig(format='%(asctime)s, %(name)s, %(levelname)s, %(message)s',
    level=logging.INFO)


argumentsDescMsg = 'Bot initialization parameters.'
tokenArgHelp     = 'telegram token'
subredditArgHelp = 'subreddit name to use'


subredditUrl = 'https://www.reddit.com/r/%s/'


startMsg          = 'Hello! Im the %s posts getter bot. You can ask me the last post with /last, or a random one with /random'
helpMsg           = 'Functions: /last /random /which'
whichSubredditMsg = 'The subreddit being used is: /r/%s'


def parse_input():
    parser = argparse.ArgumentParser(description=argumentsDescMsg, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('token', metavar='TOKEN', type=str, help=tokenArgHelp)
    parser.add_argument('subreddit', metavar='SUBREDDIT', type=str, help=subredditArgHelp)

    args = parser.parse_args()
    return args


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=startMsg%(botArgs.subreddit))


def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=helpMsg)


def last_pic(bot, update):
    data = feedparser.parse(subredditUrl%(botArgs.subreddit)+'.rss')
    link = data.entries[0]['content'][0]['value']
    root = ET.fromstring(link)
    bot.send_message(chat_id=update.message.chat_id, text=root.xpath("//a")[2].get("href"))


def random_pic(bot, update):
    data = feedparser.parse(subredditUrl%(botArgs.subreddit)+'.rss')
    entrie = random.randint(0,len(data.entries))
    link = data.entries[entrie]['content'][0]['value']
    root = ET.fromstring(link)
    bot.send_message(chat_id=update.message.chat_id, text=root.xpath("//a")[2].get("href"))


def which_subreddit(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=whichSubredditMsg%(botArgs.subreddit))


def main():
    global botArgs
    botArgs = parse_input()


    updater = Updater(botArgs.token)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('last', last_pic))
    updater.dispatcher.add_handler(CommandHandler('random', random_pic))
    updater.dispatcher.add_handler(CommandHandler('which', which_subreddit))

    
    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process_reply_msg receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == "__main__":
    main()