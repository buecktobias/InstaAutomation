from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

EBAY_URL = "https://www.ebay-kleinanzeigen.de/"


class EbayAPI:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def search(self, city):
        self.load_start_page()
        self.fill_city(city)
        self.find()
        return self.read_elements()

    def load_start_page(self):
        self.browser.get(EBAY_URL)

    def fill_city(self, city):
        x_path_city = r"/html/body/header/section[2]/div/div/div[1]/div/form/div/div[2]/div/div[1]/div/input[1]"
        city_input = self.browser.find_element_by_xpath(x_path_city)
        city_input.send_keys(city)

    def find(self):
        x_path_submit = "/html/body/header/section[2]/div/div/div[1]/div/form/div/div[3]/button"
        self.browser.find_element_by_xpath(x_path_submit).click()

    def read_elements(self):
        image_x_path = "/html/body/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[2]/ul/li[1]/article/div[1]/div/img"
        image_src = self.browser.find_element_by_xpath(image_x_path).get_attribute("src")
        title_x_path = "/html/body/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[2]/ul/li[1]/article/div[2]/h2/a"
        title = self.browser.find_element_by_xpath(title_x_path)
        title_href = title.get_attribute("href")
        print(title)
        title_text = title.get_attribute("innerHTML")
        return image_src, title_text, title_href


if __name__ == '__main__':
    print(EbayAPI().search("Mainz"))