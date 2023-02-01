from typing import List

import pytest

from hathor_wallet.configs import Configs
from hathor_wallet.hathor_wallet import HathorWallet


class TestHathorWallet:
    '''
    This class is a test suite for the HathorWallet class.
    It contains tests for all the methods in HathorWallet, including:
     
    start, 
    status, 
    balance, 
    current_address, 
    all_generated_addres, 
    stop, 
    simple_send_tx, 
    and tx_history.

    All test methods use the fixture wallet to create an instance of HathorWallet 
    with the specified configurations.
    '''
    @pytest.fixture
    def wallet(self):
        '''
        This fixture will be used in all test methods. 
        The fixture creates an instance of the HathorWallet class 
        with the configurations specified in the Configs().setup() method.
        '''
        configs = Configs(
            wallet_base_url='https://hathor-wallet-headless.mailsonnascin.repl.co/',
            x_api_key='fa38a4bad4c7a19c319ab7c0672002ca46499cb86d5910c535fb6731fdb775d2',
            wallet_id='', # Your wallet id
            seed='' # Your seeds
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

    def test_simple_send_tx(self, wallet):
        ''' Teste a send transaction'''
        response = wallet.simple_send_tx(address='HASa1UUGnWHaj62kwU3HzL4ptahdMAfPH7', value=1)
        assert type(response.get('success')) == bool

    def test_tx_history(self, wallet):
        ''' Teste get transactions'''
        response = wallet.tx_history()
        assert type(response) == dict