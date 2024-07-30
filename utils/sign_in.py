from utils.typeAccount import typeAccount
from utils.load_accounts import load_accounts
from lib import gb

def sign_in(driver):
    if 'login' in driver.current_url:
        if len(gb.accounts['Success']) == 0:
            load_accounts()
            
        account = gb.accounts['Success'][0]
        typeAccount(driver, account[0], account[1])