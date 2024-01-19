from selenium import webdriver

class monkeytype_cheater:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(options=options)