# Hathor Wallet
Hathor Wallet is a python library that allows you to interact with the [hathor-wallet-headless](https://github.com/HathorNetwork/hathor-wallet-headless) API. To test, you can use the headless wallet running at https://hathor-wallet-headless.mailsonnascin.repl.co/. Or use one running locally, [**here**](https://github.com/HathorNetwork/hathor-wallet-headless) you can get all the instructions to install.

# Installation
To install Hathor Wallet, simply use pip: `pip install hathor-wallet`

# Usage
First, import the library and create an instance of the Configs and HathorWallet class:
```
from hathor_wallet.hathor_wallet import HathorWallet
from hathor_wallet.configs import Configs

configs = Configs(
    wallet_base_url='https://hathor-wallet-headless.mailsonnascin.repl.co/',
    x_api_key='fa38a4bad4c7a19c319ab7c0672002ca46499cb86d5910c535fb6731fdb775d2',
    wallet_id='<your wallet id>',
    seed='<wallet seeds you want to start>' 
    ).start()

wallet = HathorWallet(**configs)
```

# Available methods
- `wallet.start()`: Starts the wallet
- `wallet.status()`: Returns the status of the wallet
- `wallet.balance()`: Returns the balance of the wallet
- `wallet.current_address(mark_as_used=None)`: Returns the current address of the wallet, it is possible to pass as a parameter if you want to mark the address as used.
- `wallet.all_generated_addres()`: Returns all addresses generated by the wallet.
- `simple_send_tx`: Performs a simple transaction to another address.
- `tx_history`: Returns the transaction history of the Hathor wallet.
- `wallet.stop()`: Stops the wallet

# Contributions
All contributions are welcome!
