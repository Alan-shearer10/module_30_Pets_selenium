from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_are_present(driver):
#   Проверяем что на странице со списком моих питомцев присутствуют все питомцы
#   Сохраняем в переменную pets элементы карточек питомцев
    pets = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
#   Сохраняем в переменную descriptions элементы статистики
    descriptions = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "body > div.task2.fill > div > div.\.col-sm-4.left")))
#   Получаем количество питомцев из данных статистики
    number = descriptions[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])
    number_of_pets = len(pets)
#   Получаем количество карточек питомцев
    assert number == number_of_pets
    print(number_of_pets)








