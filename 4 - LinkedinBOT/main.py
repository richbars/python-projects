from selenium import webdriver
import time
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.common.by import By

LOGGER.setLevel(logging.CRITICAL)
# Define as credenciais de login
email = input("Coloque seu email do Linkedin: ")
senha = input("Coloque sua senha do Linkedin: ")
funcao = input("Escolhe o cargo que queira se conectar: ")
qtd_desejadas = int(input("Escolha a quantidade de pessoas que queira se conectar: "))



# Configura o driver do Chrome
driver = webdriver.Chrome()


# Abre o LinkedIn e faz login
driver.get('https://www.linkedin.com/login')
time.sleep(5)
driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.ID, 'password').send_keys(senha)
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# Aguarda o login ser concluído
time.sleep(5)

# Acessa o perfil a ser seguido e clica no botão "Seguir"
driver.get("https://www.linkedin.com/search/results/people/?keywords={0}&origin=GLOBAL_SEARCH_HEADER&page=1".format(funcao))
time.sleep(3)

contador = 1
contador_conectadas = 0
while True:
    buttons = driver.find_elements(By.XPATH, "//button[contains(.,'Conectar')]")

    for conectar in buttons:
        time.sleep(3)
        print(conectar)
        conectar.click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[contains(.,'Enviar')]").click()
        time.sleep(3)

    quantidade = len(buttons)
    contador_conectadas += quantidade
    print(contador_conectadas)
    contador += 1
    driver.get(f"https://www.linkedin.com/search/results/people/?keywords={funcao}&origin=GLOBAL_SEARCH_HEADER&page={contador}")
    time.sleep(5)

    if contador_conectadas >= qtd_desejadas:
        break
    else:
        pass

#print(f'Foram encontrados {len(buttons)} botões')

# Fecha o navegador
driver.quit()
