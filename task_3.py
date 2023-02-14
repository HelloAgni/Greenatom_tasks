"""
3. Сколько HTML-тегов в коде главной страницы сайта greenatom.ru?
Сколько из них содержит атрибуты?
Напиши скрипт на Python, который выводит ответы на вопросы выше.

>>> Всего HTML-тегов: 798
>>> Всего HTML-тегов с атрибутами: 500
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


service = Service(executable_path=ChromeDriverManager().install())
option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('--window-size=1920,1080')
option.add_argument("--disable-3d-apis")  # Fix for Windows
option.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/100.0.0.0 Safari/537.36')
driver = webdriver.Chrome(service=service, options=option)

URL = 'https://greenatom.ru/'
ALL_TAGS = '//*'
TAG_WITH_ATTR = '//*[@*]'


def count_tags():
    driver.get(url=URL)
    driver.implicitly_wait(15)
    tags_all = driver.find_elements(By.XPATH, ALL_TAGS)
    tags_items = [x for x in tags_all]
    tags_w_attr = driver.find_elements(By.XPATH, TAG_WITH_ATTR)
    tags_w_attr_items = [x for x in tags_w_attr]
    driver.quit()
    print(f'Всего HTML-тегов: {len(tags_items)}')
    print(f'Всего HTML-тегов с атрибутами: {len(tags_w_attr_items)}')


if __name__ == '__main__':
    count_tags()
