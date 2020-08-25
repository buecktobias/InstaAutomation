from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

import login_user

INSTAGRAM_URL = "http://www.instagram.com"


class InstaAPI:
    def __init__(self):
        opts = Options()
        opts.add_argument("user-agent=Mozilla/5.0 (Linux; Android 8.1.0; Infinix X572) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36")
        self.browser = webdriver.Chrome(options=opts)

    def login(self, user_name, password):
        self.load_instagram_start_page()
        self.click_login_button()
        self.fill_form(user_name, password)
        self.not_save()
        self.not_homescreen()

    def load_instagram_start_page(self):
        self.browser.get(INSTAGRAM_URL)
        self.browser.implicitly_wait(2)

    def click_login_button(self):
        login_button = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/div[2]/button")
        login_button.click()

    def fill_form(self, user_name, password):
        x_path_email = r"/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input"
        x_path_password = r"/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input"
        x_path_submit = r"/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button"
        email_INP = self.browser.find_element_by_xpath(x_path_email)
        password_INP = self.browser.find_element_by_xpath(x_path_password)
        submit = self.browser.find_element_by_xpath(x_path_submit)
        email_INP.send_keys(user_name)
        password_INP.send_keys(password)
        submit.click()

    def not_save(self):
        xpath_not_save = "/html/body/div[1]/section/main/div/div/div/button"
        not_save = self.browser.find_element_by_xpath(xpath_not_save)
        not_save.click()

    def not_homescreen(self):
        xpath_not_home = "/html/body/div[4]/div/div/div/div[3]/button[2]"
        wait = WebDriverWait(self.browser, 2)
        not_home = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_not_home)))
        not_home.click()

    def no_notifications(self):
        try:
            self.not_homescreen()
        except Exception as e:
            print(e)
            pass

    def yes_notifications(self):
        try:
            xpath_yes = "/html/body/div[4]/div/div/div/div[3]/button[1]"
            wait = WebDriverWait(self.browser, 5)
            not_home = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_yes)))
            not_home.click()
        except Exception as e:
            print(e)
            pass

    def post(self, fp, caption):
        self.press_new_post()
        self.select_file(fp)
        self.yes_notifications()
        self.next_post()
        self.post_options(caption)
        self.share()
        self.yes_notifications()

    def press_new_post(self):
        x_path_post = "/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]"
        post = self.browser.find_element_by_xpath(x_path_post)
        post.click()

    def select_file(self, file):
        _, path = file.split("tobias/")
        elems = path.split("/")

        for elem in elems:
            pyautogui.hotkey('ctrl', 'f')
            pyautogui.write(elem)
            pyautogui.press('enter')

    def next_post(self):
        x_path_next = "/html/body/div[1]/section/div[1]/header/div/div[2]/button"
        self.browser.find_element_by_xpath(x_path_next).click()

    def post_options(self, caption):
        x_path_textarea_caption = "/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea"
        self.browser.find_element_by_xpath(x_path_textarea_caption).send_keys(caption)

    def share(self):
        x_path_share_button = "/html/body/div[1]/section/div[1]/header/div/div[2]/button"
        self.browser.find_element_by_xpath(x_path_share_button).click()


if __name__ == '__main__':
    file = "home/tobias/Pictures/Frankfurt.jpg"
    caption = "Krasses Bild aus ffm"
    l = InstaAPI()

    l.login(login_user.username, login_user.PASSWORD)
    l.post(file, caption)
