from pymsteams import connectorcard
from html2image import Html2Image
from lib import gb
from adaptivecardbuilder import *
from datetime import datetime

import base64
import asyncio

def generateImgFromHTML(pathToHTML: str ='./report/report.html', pathToCSS: str ='./report/assets/style.css') -> str:
    hti = Html2Image(output_path='./screenshot/', size=(1024, 768))
    hti.screenshot(
        html_str=open(pathToHTML, 'r').read(),
        css_str=open(pathToCSS, 'r').read(),
        save_as='test_report.png'
    )

    with open('./screenshot/test_report.png', 'rb') as f:
        encoded_string = base64.b64encode(f.read()).decode('utf-8')
    
    return encoded_string

def sendAdaptiveCard():
    encoded_string = generateImgFromHTML()
    myTeamsMessage = connectorcard(hookurl=gb.MSTEAMS_WEBHOOK)
    card = AdaptiveCard(schema=gb.SCHEMA_URL, version="1.5")
    card.add([
        TextBlock(text='Result Using Pytest', size='ExtraLarge', weight='Bolder', wrap='true', spacing='None'),
        TextBlock(text=f"{datetime.now().strftime('%d/%m/%Y')} Report Summary",
                       weight='Bolder', wrap='true', spacing='None'),
        Image(url=f'data:image/png;base64,{encoded_string}', msTeams={"allowExpand": "true"})
    ])

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    myTeamsMessage.payload = {
        "type": "message",
        "attachments": [
            {
                "contentType":"application/vnd.microsoft.card.adaptive",
                "contentUrl": "null",
                "content": loop.run_until_complete(card.to_dict(version='1.5', schema=gb.SCHEMA_URL))
            }
        ]
    }

    myTeamsMessage = myTeamsMessage.color("good")
    myTeamsMessage.send()