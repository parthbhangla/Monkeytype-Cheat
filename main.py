from selenium import webdriver
import keyboard
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

class monkeytype_cheater:
    
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(options=options)

        self.driver.get("https://monkeytype.com/")

    def cookies_selection(self):
        time.sleep(1)
        button = self.driver.find_element(by = "class name", value = "rejectAll")
        try:
            button.click()
            time.sleep(5)
        except Exception as e:
            print(e)

    def solver(self, delay):
        self.cookies_selection()

        words = self.driver.find_elements(by = "class name", value = "word")
        try:
            while len(words) != 0:
                sentence = ""
                active_word = self.driver.find_element(by = "class name", value ="word.active")
                letters = active_word.find_elements(by = "tag name", value = "letter")
                for letter in letters:
                    sentence = sentence + letter.text
                sentence = sentence + " "
                keyboard.write(sentence)
                time.sleep(delay)
                words = self.driver.find_elements(by = "class name", value = "word")
        except (StaleElementReferenceException, NoSuchElementException):
            pass 

if __name__ == "__main__":
    delay = float(input("Enter the delay in seconds (e.g., 0.1): "))
    typer = monkeytype_cheater()
    typer.solver(delay)
    input("Press Enter to Exit.")