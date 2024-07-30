from lib import pd, gb

def load_accounts():
    gb.dfLogin = pd.read_excel(
        open('./testData/loginData.xlsx', mode='rb'),
    )

    gb.dfLogin = gb.dfLogin.fillna('')

    for action, username, password in zip(gb.dfLogin['Action'], gb.dfLogin['Username'], gb.dfLogin['Password']):
        gb.accounts[action].append((username, password))