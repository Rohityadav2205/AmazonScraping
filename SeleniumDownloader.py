import time

from selenium import webdriver


def downloadUrl(url):
    driver = webdriver.Chrome(
        'D:/chrome/chromedriver.exe')  # Optional argument, if not specified will search path.

    driver.get(
        url)

    time.sleep(5)  # Let the user actually see something!

    src = driver.page_source
    driver.quit()
    return src
