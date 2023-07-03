import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from settings import email, password


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open PetFriends base page:
    driver.get("https://petfriends.skillfactory.ru/")


    time.sleep(3)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success")
    btn_newuser.click()

    # click existing user button
    btn_exist_acc = driver.find_element(By.CSS_SELECTOR, "div.text-center>a")
    btn_exist_acc.click()

    # add email
    field_email = driver.find_element(By.CSS_SELECTOR, "input#email")
    field_email.clear()
    time.sleep(3)
    field_email.send_keys(email)

    # add password
    field_pass = driver.find_element(By.CSS_SELECTOR, "#pass")
    field_pass.clear()
    time.sleep(3)
    field_pass.send_keys(password)

    # click submit button
    btn_submit = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success")
    btn_submit.click()

    time.sleep(3)

    btn_my_pets = driver.find_element(By.CSS_SELECTOR, "div#navbarNav > ul > li > a")
    btn_my_pets.click()
    time.sleep(10)

    yield driver
    driver.quit()