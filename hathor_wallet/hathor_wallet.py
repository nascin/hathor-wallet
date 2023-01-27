from typing import Optional, List

from hathor_wallet.exception import HathorWalletError

import requests
from urllib import parse


class HathorWallet:

    def __init__(
        self, 
        wallet_base_url: str = 'https://hathor-wallet-headless-replit.mailsonnascin.repl.co/', 
        **configs
        ):
        self.wallet_base_url: str = wallet_base_url
        self.configs: dict = configs

    def start(self):
        try:
            url = parse.urljoin(self.wallet_base_url, '/start')
            response = requests.post(url=url, headers=self.configs.get('headers'), data=self.configs.get('data'))
            
            if response.status_code != 200:
                raise HathorWalletError('Erro stating wallet.')

            return response.json()

        except:
            raise HathorWalletError('Error in the request.')

    def status(self):
        try:
            url = parse.urljoin(self.wallet_base_url, '/wallet/status')
            response = requests.get(url=url, headers=self.configs.get('headers'), data=self.configs.get('data'))
            
            if response.status_code != 200:
                raise HathorWalletError('Error getting wallet status.')

            return response.json()
        except:
            raise HathorWalletError('Error in the request.')

    def balance(self):
        # Not implemented other UID.
        try:
            url = parse.urljoin(self.wallet_base_url, '/wallet/balance')
            response = requests.get(url=url, headers=self.configs.get('headers'))
            
            if response.status_code != 200:
                raise HathorWalletError('Error getting wallet balance.')

            return response.json()

        except:
            raise HathorWalletError('Error in the request.')
            
    def stop(self):
        try:
            url = parse.urljoin(self.wallet_base_url, '/wallet/stop')
            response = requests.post(url=url, headers=self.configs.get('headers'))
            
            if response.status_code != 200:
                raise HathorWalletError('Error stop wallet.')

            return response.json()
            
        except:
            raise HathorWalletError('Error in the request.')
