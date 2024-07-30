URL = 'https://elearning.dai-ichi-life.com.vn/'

# Dataframe
dfLogin = None
dfEbookData = None
dfEbookName = None

# Browser version
CHROME_VERSION = '126.0.6478.182 (Official Build) (64-bit)'
MSEDGE_VERSION = '127.0.2651.61 (Official build) stable app, beta channel (64-bit)'

# Driver directory
CHROME_DRIVER = r'.\driver\chromedriver.exe'
MSEDGE_DRIVER = r'.\driver\msedgedriver.exe'

# data
accounts = {
    "Success": [],
    "Failed": [],
    "Error": [],
    "Empty": []
}
ebooks = {
    "Detail": [],
    "Download": [],
    "ReadOnline": [],
    "Detail_Download": []
}