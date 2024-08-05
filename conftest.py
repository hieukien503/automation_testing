from lib import (
    gb,
    pytest,
    webdriver,
)

@pytest.fixture(params=['chrome', 'edge'], autouse=True)
def init_driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--verbose')
        options.add_argument(r'--log-path=.\logs\chromedriver.log')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = webdriver.ChromeService('./driver/chromedriver.exe')
        driver = webdriver.Chrome(
            service=service,
            options=options
        )
    
    elif request.param == 'edge':
        options = webdriver.EdgeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--verbose')
        options.add_argument(r'--log-file=.\logs\msedgedriver.log')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = webdriver.EdgeService('./driver/msedgedriver.exe')
        driver = webdriver.Edge(
            service=service,
            options=options
        )
    
    driver.get(gb.URL)
    request.driver = driver
    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if "[" in report.nodeid and "]" in report.nodeid:
        end_idx = report.nodeid.index("-")
        if end_idx != -1:
            report.nodeid = report.nodeid[:end_idx] + ']'