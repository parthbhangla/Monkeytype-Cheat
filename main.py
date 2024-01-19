from selenium import webdriver
import keyboard
import time

class monkeytype_cheater:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(options=options)

        self.driver.get("https://monkeytype.com/")

    def cookies_selection(self):
        time.sleep(2)
        button = self.driver.find_elements(by = "class name", value = "active acceptAll")
        time.sleep(2)
        try:
            button.click()
        except:
            pass

    def get_sentence(self):
        self.cookies_selection()
        words_set = self.driver.find_element(by = "id", value = "wordsWrapper")
        try:
            words_set.click()
        except:
            pass

        words = self.driver.find_elements(by = "class name", value = "word")
        sentence = ""
        for word in words:
            letters = word.find_elements(by = "tag name", value = "letter")
            for letter in letters:
                if not "correct" in letter.get_attribute("class"):
                    sentence = sentence + letter.text
            sentence = sentence + " "
        print(sentence)

    def start(self):
        sentence = self.get_sentence()
        keyboard.write(sentence)
    
if __name__ == "__main__":
    typer = monkeytype_cheater()
    typer.start()