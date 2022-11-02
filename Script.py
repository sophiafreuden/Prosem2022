
# loading packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# setting up Google Chrome driver to be able to open Chrome via bot
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# telling driver to go to rt.com
driver.get("https://rt.com")

# telling Python script to wait 2 seconds to allow page to fully load
time.sleep(2)

# finding the search box by HTML element name
search = driver.find_element(By.NAME, "q")

time.sleep(1)

# entering "soros" into search box
search.send_keys("soros")

time.sleep(7)

# hitting virtual enter/return key
search.send_keys(Keys.ENTER)

time.sleep(7)

# finding all URLs to stories by Xpath; Xpath is works alongside HTML and can serve as an alternative
# when finding HTML elements becomes tricky/error-prone
scraped = driver.find_elements(By.XPATH, "//a[@class='link link_hover']")

time.sleep(2)

# establishing an empty list to put URLs into
rawlinks = []

# stripping actual URLs from HTML elements
for url in scraped:
    rawlinks.append(url.get_attribute("href"))

time.sleep(2)

# isolating the first story in list of URLs in a new variable; Python indexes at 0, something you will learn
# about early on in your Python education
first_story = rawlinks[0]

# printing a message to the console with the URL of the first story
print("")
print("This is the url of the first story we pulled: " + str(first_story) + ".")
print("")

time.sleep(1)

# telling driver to use this URl to go to the first story
driver.get(first_story)

time.sleep(5)

# finding the HTML element that contains the title of the article; the .text suffix tells driver to strip the
# actual text (the title itself) from that HTML element
title = driver.find_element(By.CLASS_NAME, "article__heading").text

time.sleep(1)

# printing a message to the console containing the text (title) we just found
print("This is the title of the first story we pulled: " + str(title) + ".")
print("")

time.sleep(3)

# finding all body paragraphs of the first story; the "p" is a very common HTML tag used to denote body text.
# "p" is used almost universally across websites in this fashion, though it still can differ
all_paragraphs = driver.find_elements(By.TAG_NAME, "p")

time.sleep(1)

# printing a message before paragraphs
print("Now printing all paragraphs:")

# printing paragraphs
for paragraph in all_paragraphs:
    print(paragraph.text)

time.sleep(2)

# printing script end message
print("")
print("")
print("End of script. Chrome will terminate automatically.")
