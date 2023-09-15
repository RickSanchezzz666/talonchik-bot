from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import pygame

#python 3.10.8

driver = webdriver.Chrome()

pygame.mixer.init()
sound = pygame.mixer.Sound('alert.mp3')
sound.set_volume(1.0)

driver.get('https://eq.hsc.gov.ua/site/step2?chdate=2023-09-16&question_id=55&id_es=') #силка на карту з вибраною дату, наприклад: ДАТА ПРИЙОМУ — 16.09.23


time.sleep(40)

while True:
    try:
        try:
            err_elem = driver.find_element(By.XPATH, "//*[contains(text(), 'nginx')]")
            driver.refresh()
            time.sleep(3) 
        except NoSuchElementException:
            pass
        time.sleep(1)
        first_location = driver.find_element('css selector', "img[style*='z-index: 194']") # координата міста по z-index у її css style
        first_location.click()
        time.sleep(2)

        try:
            second_location = driver.find_element('css selector', '#submit')
            second_location.click()
            sound.play()
            print('Талончик знайдено!')
            time.sleep(2.5)
            final_location = driver.find_element('css selector', '.btn-hsc-green')
            final_location.click()
            input('Нажми Enter для завершення...')
            break
        except NoSuchElementException:
            driver.refresh()
            time.sleep(1)
    except NoSuchElementException:
            driver.refresh()
            time.sleep(1)