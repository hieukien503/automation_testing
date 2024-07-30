from lib import (
    gb,
    pytest,
    webdriver
)

@pytest.fixture(params=['chrome', 'edge'], autouse=True)
def init_driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        service = webdriver.ChromeService('./driver/chromedriver.exe')
        driver = webdriver.Chrome(
            service=service,
            options=options
        )
    
    elif request.param == 'edge':
        options = webdriver.EdgeOptions()
        options.add_argument('--start-maximized')
        service = webdriver.EdgeService('./driver/msedgedriver.exe')
        driver = webdriver.Edge(
            service=service,
            options=options
        )
    
    driver.get(gb.URL)
    request.driver = driver
    yield driver

    driver.quit()