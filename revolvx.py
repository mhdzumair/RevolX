from os import path
import platform
from random import choice
from threading import Thread
from time import sleep
import json
from urllib import parse
from xml.etree import ElementTree

from selenium import webdriver
from selenium.common.exceptions import (ElementNotInteractableException,
                                        NoSuchElementException)
from selenium.webdriver.common.keys import Keys

extensions = [
    "extensions/ads-fucker-full@mhdzumair.xpi",
    "extensions/uBlock0@raymondhill.net.xpi"
]

sites = ElementTree.parse('sites.xml').getroot()
with open("ptc_site.json") as file:
    config = json.load(file)

options = webdriver.FirefoxOptions()
options.headless = True

if platform.system() == "Linux":
    geckodriver = path.abspath("geckodriver")
elif platform == "Windows":
    geckodriver = path.abspath("geckodriver.exe")
else:
    print("configure geckodriver on your own. configure this.")


class RevolvX(Thread):
    def __init__(self, name, username, password):
        super(RevolvX, self).__init__()
        print(f"fucking: {name}")
        self.config = config[name]
        self.firefox = webdriver.Firefox(executable_path=geckodriver, options=options)
        self.username = username
        self.password = password

    def run(self):
        self.install_extension()
        if not self.login():
            print("login failed")
            return self.firefox.close()

        self.collect_package()
        if self.check_bonus():
            print(f"daily bonus available.: {self.username}")
            self.get_bonus()
        else:
            print(f"already got daily bonus.: {self.username}")

        self.view_ads()
        self.logout()

    def install_extension(self):
        for extension in extensions:
            self.firefox.install_addon(path.abspath(extension), temporary=False)

    def login(self):
        print(f"login: {self.username}")
        self.firefox.get(self.config["login"])
        sleep(5)
        username = self.firefox.find_element_by_id("user_name")
        username.send_keys(self.username)
        password = self.firefox.find_element_by_id("user_password")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        sleep(5)
        if self.firefox.current_url == self.config["success"]:
            return True
        else:
            return False

    def collect_package(self):
        # collect package money
        self.firefox.get(parse.urljoin(self.firefox.current_url, "/packages"))
        collect_money = self.firefox.find_element_by_css_selector(self.config["package"])
        collect_money.click()
        print(f"get package money: {self.username}")
        sleep(5)

    def get_bonus(self):
        banner_div = self.firefox.find_element_by_css_selector(self.config["banner"])
        banners = [banner for banner in banner_div.find_elements_by_tag_name("a")
                   if banner.find_element_by_tag_name("img").is_displayed()]

        while banners:
            banner = choice(banners)
            try:
                banner.click()
                break
            except ElementNotInteractableException:
                banners.remove(banner)

        current_index = self.firefox.window_handles.index(self.firefox.current_window_handle)
        self.firefox.switch_to.window(self.firefox.window_handles[current_index + 1])
        self.firefox.close()
        self.firefox.switch_to.window(self.firefox.window_handles[current_index])
        self.firefox.find_element_by_id(self.config["bonus"]).click()

    def check_bonus(self):
        # check bonus
        self.firefox.get(parse.urljoin(self.firefox.current_url, "/bonus"))
        try:
            self.firefox.find_element_by_id(self.config["bonus"])
            return True
        except NoSuchElementException:
            return False

    def view_ads(self):
        # viewads
        self.firefox.get(parse.urljoin(self.firefox.current_url, "/viewads"))
        print(f"opened viewads: {self.username}")

        while True:
            ads = self.firefox.find_elements_by_css_selector(self.config["ads"])
            if ads:
                sleep(10)
            else:
                print("no ads available!")
                break

    def logout(self):
        self.firefox.get(parse.urljoin(self.firefox.current_url, "/exit"))
        print(f"logout: {self.username}")
        self.firefox.close()


for site in sites:
    try:
        revolvx = RevolvX(site.get("name"), site[0].text, site[1].text)
    except KeyError:
        print(f"Wrong Site Name: {site.get('name')}")
        continue

    revolvx.start()

