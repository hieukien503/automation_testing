import urllib3
import json

MSTEAMS_WEBHOOK = "https://dlvn.webhook.office.com/webhookb2/2c926cd4-6a47-4403-8344-66b5b5f9543a@c19239e5-1337-436d-800a-1b4283c280dd/IncomingWebhook/36f93937606b437cbea3d8736de5ca3b/07f23511-0004-4a49-94db-b2b8b16308cf"

class TeamsWebhookException(Exception):
    """custom exception for failed webhook call"""
    pass

class ConnectorCard:
    def __init__(self, hookurl, http_timeout=60):
        self.http = urllib3.PoolManager()
        self.payload = {}
        self.hookurl = hookurl
        self.http_timeout = http_timeout

    def send(self):
        headers = {"Content-Type":"application/json"}
        r = self.http.request(
                'POST',
                f'{self.hookurl}',
                body=json.dumps(self.payload).encode('utf-8'),
                headers=headers, timeout=self.http_timeout)
        if r.status == 200: 
            return True
        else:
            raise TeamsWebhookException(r.reason)