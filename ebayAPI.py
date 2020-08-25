from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ebay_object import EbayObject
EBAY_URL = "https://www.ebay-kleinanzeigen.de/"


class EbayAPI:
    def __init__(self):
        opts = Options()
        opts.add_argument("--headless")
        self.browser = webdriver.Chrome(options=opts)

    def search(self, city):
        self.__load_start_page()
        self.__fill_city(city)
        self.__find()
        return self.__read_elements()

    def __load_start_page(self):
        self.browser.get(EBAY_URL)

    def __fill_city(self, city):
        x_path_city = r"/html/body/header/section[2]/div/div/div[1]/div/form/div/div[2]/div/div[1]/div/input[1]"
        city_input = self.browser.find_element_by_xpath(x_path_city)
        city_input.send_keys(city)

    def __find(self):
        x_path_submit = "/html/body/header/section[2]/div/div/div[1]/div/form/div/div[3]/button"
        self.browser.find_element_by_xpath(x_path_submit).click()

    def __read_elements(self):
        #image_x_path = "/html/body/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[2]/ul/li[1]/article/div[1]/div/img"
        #image_src = self.browser.find_element_by_xpath(image_x_path).get_attribute("src")

        title_x_path = "/html/body/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[2]/ul/li[1]/article/div[2]/h2/a"
        title = self.browser.find_element_by_xpath(title_x_path)
        title_href = title.get_attribute("href")
        print(title)
        title_text = title.get_attribute("innerHTML")
        self.browser.get(title_href)
        big_image_x = "/html/body/div[1]/div[2]/div/section[1]/section/section/article/div[1]/div[1]/img"
        image_src = self.browser.find_element_by_xpath(big_image_x).get_attribute("src")

        eb_o = EbayObject(image_src, title_text, title_href)
        return eb_o


if __name__ == '__main__':
    print(EbayAPI().search("Mainz"))