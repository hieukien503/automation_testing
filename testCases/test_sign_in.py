from lib import (
    gb,
    By,
    pytest,
    WebDriverException
)

# from browser import init_driver
from utils.typeAccount import typeAccount
from utils.waitElementPresent import waitElementPresent as wait
from utils.load_accounts import load_accounts
from logger import Logger

mlogger = Logger(__name__, 'testSignIn').get()

load_accounts()

class TestSignIn:
    @pytest.mark.parametrize("username, password", gb.accounts['Success'])
    def test_sign_in_success(self, username, password, init_driver):
        mlogger.info('-- Running test_sign_in_success')
        driver = init_driver
        try:
            typeAccount(driver, username, password)
            assert driver.current_url == "https://elearning.dai-ichi-life.com.vn/index.php"
            driver.close()

        except (Exception, WebDriverException) as e:
            mlogger.exception(exc_info=True)
    
    @pytest.mark.parametrize("username, password", gb.accounts['Failed'])
    def test_sign_in_failed(self, username, password, init_driver):
        mlogger.info('-- Running test_sign_in_failed')
        driver = init_driver
        try:
            typeAccount(driver, username, password)
            assert gb.URL in driver.current_url and 'login' in driver.current_url and 'errorcode=3' in driver.current_url
            driver.close()

        except (Exception, WebDriverException) as e:
            mlogger.exception(exec_info=True)
    
    @pytest.mark.parametrize("username, password", gb.accounts['Error'])
    def test_sign_in_error_click_link(self, username, password, init_driver):
        mlogger.info('-- Running test_sign_in_error_click_link')
        driver = init_driver
        try:
            typeAccount(driver, username, password)

            assert driver.find_elements(By.XPATH, "//section[@id='region-main']/gmessage/div/div/p[2]/a") != [] and \
                driver.find_elements(By.XPATH, "//section[@id='region-main']/gmessage/div/div[2]/form/div/input") != []
            
            driver.find_element(By.XPATH, "//section[@id='region-main']/gmessage/div/div/p[2]/a").click()
            assert gb.URL in driver.current_url and 'login' in driver.current_url
            driver.close()

        except (Exception, WebDriverException) as e:
            mlogger.exception(exec_info=True)
    
    @pytest.mark.parametrize("username, password", gb.accounts['Error'])
    def test_sign_in_error_click_button(self, username, password, init_driver):
        mlogger.info('-- Running test_sign_in_error_click_butto')
        driver = init_driver
        try:
            typeAccount(driver, username, password)

            assert driver.find_elements(By.XPATH, "//section[@id='region-main']/gmessage/div/div/p[2]/a") != [] and \
                driver.find_elements(By.XPATH, "//section[@id='region-main']/gmessage/div/div[2]/form/div/input") != []
            
            driver.find_element(By.XPATH, "//section[@id='region-main']/gmessage/div/div[2]/form/div/input").click()
            assert gb.URL in driver.current_url and 'login' in driver.current_url
            driver.close()

        except (Exception, WebDriverException) as e:
            mlogger.exception(exec_info=True)
    
    @pytest.mark.parametrize("username, password", gb.accounts['Empty'])
    def test_sign_in_empty(self, username, password, init_driver):
        mlogger.info('-- Running test_sign_in_empty')
        driver = init_driver
        try:
            typeAccount(driver, username, password)
            assert gb.URL in driver.current_url and 'login' in driver.current_url
            driver.close()

        except (Exception, WebDriverException) as e:
            mlogger.exception(exec_info=True)