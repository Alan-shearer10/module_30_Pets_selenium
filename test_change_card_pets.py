import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import email, password


def test_change_card_pets():
#   Проверка карточек питомцев
    browser = webdriver.Chrome()
# Устанавливаем неявное ожидание
    browser.implicitly_wait(10)
#    Open PetFriends base page:
    browser.get("https://petfriends.skillfactory.ru/")



    browser.maximize_window()

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

    browser.find_element(By.CSS_SELECTOR, "body > div > div > form > div.text-center > a").click()


       # Вводим email
    browser.find_element(By.CSS_SELECTOR, "input#email").send_keys(email)

       # Вводим пароль
    browser.find_element(By.CSS_SELECTOR, "#pass").send_keys(password)

       # Нажимаем на кнопку входа в аккаунт
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

       # Нажимая кнопку входим на строницу "Мои питоцы"


    browser.find_element(By.CSS_SELECTOR, "div#navbarNav > ul > li > a").click()


       # Проверяем, что мы оказались на главной странице пользователя
    assert browser.current_url == 'https://petfriends.skillfactory.ru/my_pets'


    images = browser.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody')
    names = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
    assert names[0].text != ''

    for i in range(len(names)):
          assert images[i].get_attribute('src') != ''
          assert names[i].text != ''
          assert descriptions[i].text != ''
          assert ',' in descriptions[i].text
          parts = descriptions[i].text.split(", ")
          assert len(parts[0]) > 0
          assert len(parts[1]) > 0

