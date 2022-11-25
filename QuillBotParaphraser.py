import time

import pyperclip
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from WebDriverFirefox import WebDriverFirefox
from Essay import Essay

account_button_xpath = "/html/body/div[1]/div[2]/div[2]/div/section/header/div/div[3]/div/a/button"
login_button_xpath = "/html/body/div[1]/div[2]/div[3]/section[1]/div/div/div/div/div/div[3]/div/div[5]/button"
email_label_xpath = "//label[contains( text( ), \"Email\")]"
password_label_xpath = "//label[contains( text( ), \"Password\")]"
loading_xpath = "/html/body/div[1]/div[2]/div[3]/section[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/button/div[2]"

close_premium_button_xpath = "/html/body/div[6]/div[3]/div/div[1]/button"
synonyms_mark_xpath = "/html/body/div[1]/div[2]/div[3]/section[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div/div[4]/div[2]/div/div[2]/div/span/span[5]"

text_input_xpath = "//*[@id=\"inputText\"]"
paraphrase_button_xpath = "/html/body/div[1]/div[2]/div[3]/section[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/button"
paraphrase_label_xpath = ""

output_xpath = "//*[@id=\"editable-content-within-article\"]"

filename = "individual-recommendation-report.txt"
email = "quocan29102000@gmail.com"
password = "Nguy3nQu0c@nQuillbot"

web_driver = WebDriverFirefox()
web_driver.web_driver.implicitly_wait(10)


def login():
    web_driver.click(web_driver.get_by_xpath(account_button_xpath))

    email_label = web_driver.get_by_xpath(email_label_xpath)
    email_mui = email_label.get_attribute("for")
    email_input_xpath = "//*[@id=\"" + email_mui + "\"]"
    email_input = web_driver.get_by_xpath(email_input_xpath)
    email_input.send_keys(email)

    password_label = web_driver.get_by_xpath(password_label_xpath)
    password_mui = password_label.get_attribute("for")
    password_input_xpath = "//*[@id=\"" + password_mui + "\"]"
    password_input = web_driver.get_by_xpath(password_input_xpath)
    password_input.send_keys(password)

    web_driver.click(web_driver.get_by_xpath(login_button_xpath))
    web_driver.click(web_driver.get_by_xpath(close_premium_button_xpath))


def paraphrase(text, paraphrase_button):
    text_input = web_driver.get_by_xpath(text_input_xpath)
    text_input.send_keys(Keys.CONTROL + "a")
    text_input.send_keys(Keys.DELETE)
    text_input.send_keys(text)

    # paraphrase_button = web_driver.get_by_xpath(paraphrase_button_xpath)
    web_driver.click(paraphrase_button)

    paraphrase_button_children = paraphrase_button.find_elements(By.XPATH, "./child::*")
    child_class = paraphrase_button_children[0].get_attribute("class")
    while paraphrase_button_children[0].get_attribute("class") == child_class:
        continue

    output = web_driver.get_by_xpath(output_xpath)
    output.send_keys(Keys.CONTROL + "a")
    output.send_keys(Keys.CONTROL + "c")
    print(pyperclip.paste())


def main():
    web_driver.go_to("https://www.quillbot.com")
    login()
    synonyms_mark = web_driver.get_by_xpath(synonyms_mark_xpath)
    web_driver.click(synonyms_mark)
    synonyms_mark.click()

    essay = Essay(filename)
    paraphrase_button = web_driver.get_by_xpath(paraphrase_button_xpath)

    starting_index = 0
    while starting_index < len(essay.sentences):
        sentences, starting_index = essay.get_next_sentences_under_limit(starting_index, 125)
        text = [sentence.text for sentence in sentences]
        paraphrase(". ".join(text), paraphrase_button)
