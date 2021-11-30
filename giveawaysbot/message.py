from giveawaysbot import settings
from random import choice


PARTICIPATION_INSTRUCTIONS_KEYWORDS = ("instructions", "like", "follow", "steps")
INTERJECTIONS = ("Aww", "Yoo", "Wow", "OMG", "No way")
SUPPORT_MESSAGES = (
    "I love it",
    "this is amazing",
    "this is awesome",
    "it's so cool",
    "I love your art",
    "I wish I win",
    "this is so cool",
    "such a pretty piece",
    "I love this piece",
)


def generate_message(wallet: str, giveaway_text: str = None) -> str:
    body = ""

    if "discord" in giveaway_text:
        body += f"\nDiscord: {settings.DISCORD}"

    if "twitter" in giveaway_text:
        body += f"\nTwitter: {settings.TWITTER}"

    for word in PARTICIPATION_INSTRUCTIONS_KEYWORDS:
        if word in giveaway_text:
            body += "\nDone!"
            break

    return f"{choice(INTERJECTIONS)}, {choice(SUPPORT_MESSAGES)}! {body} \n\n{wallet}"
