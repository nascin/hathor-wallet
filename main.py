from hathor_wallet.hathor_wallet import HathorWallet
from hathor_wallet.configs import configs


wallet = HathorWallet(**configs)


#print(wallet.start())
#print(wallet.balance())
print(wallet.stop())
