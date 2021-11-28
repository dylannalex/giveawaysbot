from random import choice


INTERJECTIONS = ["Aww", "Yoo", "Wow", "OMG", "No way"]
SUPPORT_MESSAGES = [
    "I love it",
    "This is amazing",
    "This is awesome",
    "It's so cool",
    "I love your art",
    "I wish I win",
    "This is so cool",
    "Such a pretty piece",
    "I love this piece",
]


def generate_message(wallet) -> str:
    return f"{choice(INTERJECTIONS)}, {SUPPORT_MESSAGES}! \n\n{wallet}"
