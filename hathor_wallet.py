import requests
from urllib import parse


wallet_id = 'wallet-mailson'
wallet_seed = 'borrow coast margin lunar unique sand typical manage gold century omit become wrong ride angle foil recycle over honey tobacco camp pistol ten grape'
wallet_base_url = 'https://hathor-wallet-headless.mailsonnascin.repl.co/'


def start_wallet():
    url = parse.urljoin(wallet_base_url, '/start')
    headers = {
    'X-API-KEY': 'KEY-MAILSON-NASCIN',
    }
    data = {
        'wallet-id': wallet_id,
        'seed': wallet_seed,
    }
    response = requests.post(url=url, headers=headers, data=data)
    print(response.json())


start_wallet()