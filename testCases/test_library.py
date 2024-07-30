from lib import (
    gb,
    By,
    pytest,
    re,
    os, time,
    WebDriverException
)

from conftest import init_driver
from utils.sign_in import sign_in
from utils.waitElementPresent import waitElementPresent as wait
from utils.load_books import load_books
from logger import Logger

mlogger = Logger(__name__, 'testLibrary').get()

load_books()

def waitDownload(fileName):
    dlWait = True
    while dlWait:
        time.sleep(1)
        dlWait = False
        files = os.listdir(r"C:\Users\dhh.kien\Downloads")
        if fileName in files:
            return
        
        for file in files:
            if file.endswith('.crdownload') and fileName in file:
                dlWait = True

class TestLibrary:
    def perform_action(self, driver, ebook_name, status):
        assert status in ['Download', 'Detail', 'ReadOnline', 'Detail_Download']
        sign_in(driver)
        
        wait(driver, 10, (By.XPATH, "/html/body/header/div/ul/li[3]/a"))
        driver.find_element(By.XPATH, "/html/body/header/div/ul/li[3]/a").click()

        wait(driver, 10, (By.XPATH, "//ul[@id='sub-menu-top1']/li[5]/a"))
        driver.find_element(By.XPATH, "//ul[@id='sub-menu-top1']/li[5]/a").click()

        idx = gb.dfEbookName[gb.dfEbookName['Name'] == ebook_name].index.to_list()[0]
        xpath = None

        if status == 'Detail' or status == 'Detail_Download':
            xpath = f"(//a[contains(text(),'Chi tiết')]){'[' + str(idx + 1) + ']' if idx > 0 else ''}"
            driver.find_element(By.XPATH, xpath).click()
            ebook_title = driver.find_element(By.XPATH, "//div[@id='content-main']/h4/span").text
            assert ebook_title.lower() == ebook_name.lower()
            if status == 'Detail_Download':
                wait(driver, 10, (By.XPATH, "//div[@id='content-main']/div[3]/div[2]/div[5]/a"))
                element = driver.find_element(By.XPATH, "//div[@id='content-main']/div[3]/div[2]/div[5]/a")
                href = element.get_attribute('href')
                element.click()
                fileName = re.search('[A-Za-z0-9]+.pdf', href).group()
                waitDownload(fileName)

                assert fileName in os.listdir(r"C:\Users\dhh.kien\Downloads")
                os.remove(rf"C:\Users\dhh.kien\Downloads\{fileName}")

        
        elif status == 'Download':
            xpath = f"(//a[contains(text(),'Tải về')]){'[' + str(idx + 1) + ']' if idx > 0 else ''}"
            element = driver.find_element(By.XPATH, xpath)
            href = element.get_attribute('href')
            element.click()
            fileName = re.search('[A-Za-z0-9]+.pdf', href).group()
            waitDownload(fileName)

            assert fileName in os.listdir(r"C:\Users\dhh.kien\Downloads")
            os.remove(rf"C:\Users\dhh.kien\Downloads\{fileName}")
        
        else:
            assert len(driver.window_handles) == 1
            xpath = f"(//a[contains(text(),'Xem trực tuyến')]){'[' + str(idx + 1) + ']' if idx > 0 else ''}"
            driver.find_element(By.XPATH, xpath).click()
            assert len(driver.window_handles) > 1
            original_window = driver.current_window_handle
            for window_handle in driver.window_handles:
                if original_window != window_handle:
                    driver.switch_to.window(window_handle)
                    break
            
            assert driver.current_window_handle != original_window
            driver.close()
            driver.switch_to.window(original_window)
        
        driver.close()

    @pytest.mark.parametrize("ebook_name", gb.ebooks['Detail'])
    def test_library_detail(self, ebook_name, init_driver):
        mlogger.info('-- Running test_library_detail')
        driver = init_driver
        try:
            self.perform_action(driver, ebook_name, 'Detail')

        except (Exception, WebDriverException) as e:
            mlogger.exception(e.msg)
        
    @pytest.mark.parametrize("ebook_name", gb.ebooks['Download'])
    def test_library_download(self, ebook_name, init_driver):
        mlogger.info('-- Running test_library_download')
        driver = init_driver
        try:
            self.perform_action(driver, ebook_name, 'Download')

        except (Exception, WebDriverException) as e:
            mlogger.exception(e.msg)

    
    @pytest.mark.parametrize("ebook_name", gb.ebooks['ReadOnline'])
    def test_library_read_online(self, ebook_name, init_driver):
        mlogger.info('-- Running test_library_read_online')
        driver = init_driver
        try:
            self.perform_action(driver, ebook_name, 'ReadOnline')

        except (Exception, WebDriverException) as e:
            mlogger.exception(e.msg)
    
    @pytest.mark.parametrize("ebook_name", gb.ebooks['Detail_Download'])
    def test_library_detail_download(self, ebook_name, init_driver):
        mlogger.info('-- Running test_library_detail_download')
        driver = init_driver
        try:
            self.perform_action(driver, ebook_name, 'Detail_Download')

        except (Exception, WebDriverException) as e:
            mlogger.exception(e.msg)