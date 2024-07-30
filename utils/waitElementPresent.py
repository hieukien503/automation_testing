from lib import (
    WebDriverWait, EC
)

def waitElementPresent(driver, timeout: float, locator):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))