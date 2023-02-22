from selenium import webdriver
import time
import logging
from pwinput import pwinput
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

LOGGER.setLevel(logging.CRITICAL)

email = input("Enter your Linkedin email: ")
password = input("Enter your Linkedin password: ")
role = input("Choose which role you want to connect: ")
qtd_desejadas = int(input("Choose the number of people you want to connect: "))




driver = webdriver.Chrome()



driver.get('https://www.linkedin.com/login')
email_field = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "username")))
email_field.send_keys(email)
pass_field = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "password")))
pass_field.send_keys(password)
submit_login = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
submit_login.click()

time.sleep(1)

driver.get("https://www.linkedin.com/search/results/people/?keywords={0}&origin=GLOBAL_SEARCH_HEADER&page=1".format(role))
time.sleep(5)

contador = 1
contador_conectadas = 0

while True:
    #buttons = driver.find_elements(By.XPATH, "//button[contains(.,'Conectar')]")
    buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(.,'Conectar')]")))

    for conectar in buttons:
        print(conectar)
        conectar.click()
        #driver.find_element(By.XPATH, "//button[contains(.,'Enviar')]").click()
        submit_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Enviar')]")))
        submit_btn.click()

    quantidade = len(buttons)
    contador_conectadas += quantidade
    print(contador_conectadas)
    contador += 1
    driver.get(f"https://www.linkedin.com/search/results/people/?keywords={role}&origin=GLOBAL_SEARCH_HEADER&page={contador}")
    time.sleep(5)

    if contador_conectadas >= qtd_desejadas:
        break
    else:
        pass

#print(f'Foram encontrados {len(buttons)} botões')

# Fecha o navegador
driver.quit()
