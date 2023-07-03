from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_pets_have_fhoto(driver):
          #    Поверяем что на странице со списком моих питомцев хотя бы у половины питомцев есть фото

          # Сохраняем в переменную descriptions элементы статистики
    descriptions = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "body > div.task2.fill > div > div.\.col-sm-4.left")))

         # Сохраняем в переменную images элементы с атрибутом img
    images = driver.find_elements(By.CSS_SELECTOR, ('.table.table-hover img'))



# Получаем количество питомцев из данных статистики
    number = descriptions[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

   # Находим половину от количества питомцев
    half = number // 2

   # Находим количество питомцев с фотографией
    number_t_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
         number_t_photos += 1

   # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
    assert number_t_photos >= half
    print(f'количество фото: {number_t_photos}')
    print(f'Половина от числа питомцев: {half}')