from lib import (
    gb,
    By,
    WebDriverException
)

from conftest import init_driver
from utils.sign_in import sign_in
from utils.waitElementPresent import waitElementPresent as wait
from logger import Logger

mlogger = Logger(__name__, 'testSignOut').get()

class TestSignOut:
    def test_sign_out(self, init_driver):
        mlogger.info('-- Running test_sign_out')
        driver = init_driver
        try:
            sign_in(driver)
            
            wait(driver, 10, (By.XPATH, "/html/body/header/div/ul/li[3]/a"))
            driver.find_element(By.XPATH, "/html/body/header/div/ul/li[3]/a").click()

            wait(driver, 10, (By.XPATH, "//ul[@id='sub-menu-top1']/li[13]/a"))
            driver.find_element(By.XPATH, "//ul[@id='sub-menu-top1']/li[13]/a").click()

            assert gb.URL in driver.current_url and 'login' in driver.current_url
            driver.close()
        
        except (Exception, WebDriverException) as e:
            mlogger.exception(e.msg)