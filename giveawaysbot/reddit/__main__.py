from sys import argv
from giveawaysbot import tools
from giveawaysbot.reddit import bot as reddit_bot
from giveawaysbot.reddit import links
from giveawaysbot.settings import GIVEAWAY_PARTICIPATIONS


def start_bot(argv) -> None:
    username, password, wallet = argv[0], argv[1], argv[2]
    bot = reddit_bot.RedditBot(username, password)
    giveaways = tools.remove_duplicates(
        [
            *bot.search_giveaways(links.REDDIT_OPENSEA_LAST_HOUR_GIVEAWAYS_LINK),
            *bot.search_giveaways(links.REDDIT_LAST_HOUR_NFT_GIVEAWAY_LINK),
        ]
    )
    if not giveaways:
        return
    bot.login()
    for _ in range(GIVEAWAY_PARTICIPATIONS):
        for giveaway in giveaways:
            bot.join_giveaway(giveaway, wallet)


if __name__ == "__main__":
    start_bot(argv[1:4])
