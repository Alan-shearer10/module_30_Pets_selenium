from selenium.webdriver.common.by import By


def test_petfriends(driver):
#   Проверка карточек питомцев
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    images = driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
    for i in range(len(names)):
         assert images[i].get_attribute('src') != ''
         assert names[i].text != ''
         assert descriptions[i].text != ''
         assert ', ' in descriptions[i]
         parts = descriptions[i].text.split(", ")
         assert len(parts[0]) > 0
         assert len(parts[1]) > 0






