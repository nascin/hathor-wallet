from typing import Optional, List

import requests
from urllib import parse


configs: dict = {
    'headers': {
        'X-API-KEY': '123456',
        'X-Wallet-Id': 'mailson-nascin',
    },
    'data': {
        'wallet-id': 'mailson-nascin',
        'seed': 'coral quarter dismiss notice sorry shoulder length sting marine arrange portion split spawn knee zone cover rebel ring code just version afford same fossil',
    }
}

class HathorWallet:

    def __init__(
        self, 
        wallet_base_url: str = 'https://hathor-wallet-headless-replit.mailsonnascin.repl.co/', 
        **configs
        ):
        self.wallet_base_url: str = wallet_base_url
        self.configs: dict = configs

    def start(self):
        url = parse.urljoin(self.wallet_base_url, '/start')
        response = requests.post(url=url, headers=self.configs.get('headers'), data=self.configs.get('data'))
        
        return response.json()

    def status(self):
        url = parse.urljoin(self.wallet_base_url, '/wallet/status')
        response = requests.get(url=url, headers=self.configs.get('headers'), data=self.configs.get('data'))
        
        return response.json()

    def balance(self):
        url = parse.urljoin(self.wallet_base_url, '/wallet/balance')
        response = requests.get(url=url, headers=self.configs.get('headers'))
        
        return response.json()
            
    def stop(self):
        url = parse.urljoin(self.wallet_base_url, '/wallet/stop')
        response = requests.post(url=url, headers=self.configs.get('headers'))
        
        return response.json()
