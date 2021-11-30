from time import sleep
from giveawaysbot.selenium_bot import SeleniumBot
from giveawaysbot.selenium_bot import try_action
from giveawaysbot import settings
from giveawaysbot import message
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class RedditBot(SeleniumBot):
    REDDIT_LOGIN_LINK = "https://www.reddit.com/login/"

    def __init__(self, username, password):
        super().__init__(username, password)
        self.replies_sent = 0

    def login(self):
        self.driver.get(self.REDDIT_LOGIN_LINK)
        sleep(settings.SLEEP_SECONDS)
        self.driver.find_element(By.NAME, "username").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(
            self.password, Keys.RETURN
        )
        sleep(settings.SLEEP_SECONDS)

    @try_action
    def search_giveaways(self, reddit_search_link):
        self.driver.get(reddit_search_link)
        return self._get_posts_links(self.get_links())

    def join_giveaway(self, link, wallet):
        self._safely_get_to_link(link)
        msg = message.generate_message(wallet, self._get_post_text())
        self._reply_post(msg)
        self.driver.get(link)
        print(f"\n\n[GIVEAWAY] successfully replied to {link}.")

    @try_action
    def _safely_get_to_link(self, link):
        self.driver.get(link)

    def _get_posts_links(self, links):
        """
        Finds reddit post links from a given list of links
        """
        return [link for link in links if "comments" in link]

    @try_action
    def _reply_post(self, message):
        self._write_reply(message)
        self._press_send_button()
        self.replies_sent += 1

    def _write_reply(self, message):
        WebDriverWait(self.driver, settings.SLEEP_SECONDS).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[@id='SHORTCUT_FOCUSABLE_DIV']/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div/div",
                )
            )
        ).send_keys(message)

    @try_action
    def _press_send_button(self):
        sleep(settings.SLEEP_SECONDS)
        self.driver.find_element(
            By.XPATH,
            "//*[@id='SHORTCUT_FOCUSABLE_DIV']/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div[3]/div[1]/button",
        ).click()

    def _get_post_text(self):
        return (
            self.driver.find_element_by_tag_name("body")
            .get_attribute("innerText")
            .lower()
        )
