from hathor_wallet.hathor_wallet import HathorWallet
from hathor_wallet.configs import Configs


configs = Configs(
    wallet_base_url='https://hathor-wallet-headless-replit.mailsonnascin.repl.co/',
    x_api_key='fa38a4bad4c7a19c319ab7c0672002ca46499cb86d5910c535fb6731fdb775d2',
    wallet_id='mailson-nascin',
    seed='coral quarter dismiss notice sorry shoulder length sting marine arrange portion split spawn knee zone cover rebel ring code just version afford same fossil'
    ).start()

wallet = HathorWallet(**configs)


#print(wallet.start())
#print(wallet.balance())
#print(wallet.status())
#print(wallet.current_address())
print(wallet.all_generated_addres())
#print(wallet.stop())

