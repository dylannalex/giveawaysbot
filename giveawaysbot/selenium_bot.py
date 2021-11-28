from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from typing import Callable
from giveawaysbot import settings
from abc import ABC, abstractmethod
from time import sleep


class SeleniumBot(ABC):
    ACTION_TRIES = 5

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        options = Options()
        options.add_argument("log-level=3")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        if settings.GOOGLE_CHROME_BIN:
            options.binary_location = settings.GOOGLE_CHROME_BIN
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(
            executable_path=settings.CHROMEDRIVER_PATH, options=options
        )

    @abstractmethod
    def login(self) -> None:
        pass

    def get_links(self) -> list[str]:
        """
        Returns a list containing all lists in the current website
        """
        elements = self.driver.find_elements(By.XPATH, "//a[@href]")
        links = [element.get_attribute("href").strip() for element in elements]
        return list(dict.fromkeys(links))


def try_action(function):
    def wrapper(*args, **kwargs):
        for try_ in range(SeleniumBot.ACTION_TRIES):
            try:
                return function(*args, **kwargs)
            except Exception:
                print(
                    f"[ERROR] {SeleniumBot.ACTION_TRIES - try_ + 1} tries left. Retrying in {settings.SLEEP_SECONDS}."
                )
                sleep(settings.SLEEP_SECONDS)

    return wrapper
