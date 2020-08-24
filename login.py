from selenium import webdriver
from selenium.webdriver.chrome.options import Options
INSTAGRAM_URL = "http://www.instagram.com"


class Login:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

        opts = Options()
        opts.add_argument("user-agent=Mozilla/5.0 (Linux; Android 8.1.0; Infinix X572) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36")
        self.browser = webdriver.Chrome(chrome_options=opts)

    def login(self):
        self.load_instagram_start_page()
        self.click_login_button()
        self.fill_form()

    def load_instagram_start_page(self):
        self.browser.get(INSTAGRAM_URL)
        self.browser.implicitly_wait(20)

    def click_login_button(self):
        login_button = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/div[2]/button")
        login_button.click()

    def fill_form(self):
        x_path_email = r"/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input"
        x_path_password = r"/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input"
        x_path_submit = r"/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button"
        email_INP = self.browser.find_element_by_xpath(x_path_email)
        password_INP = self.browser.find_element_by_xpath(x_path_password)
        submit = self.browser.find_element_by_xpath(x_path_submit)
        email_INP.send_keys(self.user_name)
        password_INP.send_keys(self.password)
        submit.click()


if __name__ == '__main__':
    l = Login("ichbinkeinbot48", "T1o7b6i0")
    l.login()