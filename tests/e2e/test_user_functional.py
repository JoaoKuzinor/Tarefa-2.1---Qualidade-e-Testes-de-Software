from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Teste correto usando wait
def test_create_user_e2e_wait():

    driver = webdriver.Chrome()

    driver.get("http://localhost:5000")

    input_name = driver.find_element(By.ID, "name")
    input_name.send_keys("Maylon")

    driver.find_element(By.ID, "submit").click()

    from selenium.webdriver.support.ui import WebDriverWait

    wait = WebDriverWait(driver, 5)

    wait.until(
        lambda d: any("Maylon" in el.text for el in d.find_elements(By.TAG_NAME, "li"))
    )

    users = driver.find_elements(By.TAG_NAME, "li")

    assert any("Maylon" in user.text for user in users)

    driver.quit()


# NOVOS TESTES


def test_create_multiple_users_e2e():

    driver = webdriver.Chrome()

    driver.get("http://localhost:5000")

    input_name = driver.find_element(By.ID, "name")

    input_name.send_keys("João")
    driver.find_element(By.ID, "submit").click()

    time.sleep(1)

    input_name = driver.find_element(By.ID, "name")

    input_name.send_keys("Maria")
    driver.find_element(By.ID, "submit").click()

    time.sleep(1)

    users = driver.find_elements(By.TAG_NAME, "li")

    assert any("João" in user.text for user in users)
    assert any("Maria" in user.text for user in users)

    driver.quit()


def test_page_loads_e2e():

    driver = webdriver.Chrome()

    driver.get("http://localhost:5000")

    assert "Users" in driver.page_source or "Usuários" in driver.page_source

    driver.quit()
