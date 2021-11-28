from sys import argv
from giveawaysbot import message
from giveawaysbot.reddit import bot as reddit_bot
from giveawaysbot.reddit import links


def start_bot(argv) -> None:
    username, password, wallet = argv[0], argv[1], argv[2]
    bot = reddit_bot.RedditBot(username, password)
    giveaways = bot.search_giveaways(links.REDDIT_OPENSEA_LAST_HOUR_GIVEAWAYS_LINK)
    if not giveaways:
        return
    bot.login()
    for giveaway in giveaways:
        bot.join_giveaway(giveaway, message.generate_message(wallet))


if __name__ == "__main__":
    start_bot(argv[1:4])
