from lib import (
    By, Keys
)

from utils.waitElementPresent import waitElementPresent as wait

def typeAccount(driver, username, password):
    wait(driver, 10, (By.XPATH, '//*[@id="username"]'))
    driver.find_element(By.XPATH, '//*[@id="username"]').click()
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)

    wait(driver, 10, (By.XPATH, '//*[@id="frm-login"]/input[2]'))
    driver.find_element(By.XPATH, '//*[@id="frm-login"]/input[2]').click()
    driver.find_element(By.XPATH, '//*[@id="frm-login"]/input[2]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="frm-login"]/input[2]').send_keys(Keys.ENTER)