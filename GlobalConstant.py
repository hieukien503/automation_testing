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

# For MS Teams
MSTEAMS_WEBHOOK = "https://dlvn.webhook.office.com/webhookb2/2c926cd4-6a47-4403-8344-66b5b5f9543a@c19239e5-1337-436d-800a-1b4283c280dd/IncomingWebhook/36f93937606b437cbea3d8736de5ca3b/07f23511-0004-4a49-94db-b2b8b16308cf"
SCHEMA_URL = "http://adaptivecards.io/schemas/adaptive-card.json"