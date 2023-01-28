import pytest
from hathor_wallet.configs import Configs
from hathor_wallet.hathor_wallet import HathorWallet


class TestHathorWallet:
    @pytest.fixture
    def wallet(self):
        configs = Configs(
            wallet_base_url='https://hathor-wallet-headless-replit.mailsonnascin.repl.co/',
            x_api_key='fa38a4bad4c7a19c319ab7c0672002ca46499cb86d5910c535fb6731fdb775d2',
            wallet_id='mailson-nascin',
            seed='coral quarter dismiss notice sorry shoulder length sting marine arrange portion split spawn knee zone cover rebel ring code just version afford same fossil'
            ).setup()

        return HathorWallet(**configs)

    def test_start(self, wallet):
        # Test the start method
        response = wallet.start()
        assert response.get('success') == True

    def test_status(self, wallet):
        # Test the status method
        response = wallet.status()
        assert response.get('statusCode') == 3

    def test_balance(self, wallet):
        # Test the balance method
        response = wallet.balance()
        if list(response.keys()) == ['available', 'locked']:
            assert True
        else:
            assert False
    def test_current_address(self, wallet):
        # Test the current_address method
        response = wallet.current_address()
        if response.get('address'):
            assert True
        else:
            assert False

    def test_all_generated_addres(self, wallet):
        # Test the all_generated_addres method
        response = wallet.all_generated_addres()
        if type(response.get('addresses')) == list:
            assert True
        else:
            assert False

    def test_stop(self, wallet):
        # Test the stop method
        response = wallet.stop()
        assert response.get('success') == True
