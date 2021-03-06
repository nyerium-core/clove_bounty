from clove.network.bitcoin import Bitcoin


class Theresamaycoin(Bitcoin):
    """
    Class with all the necessary Theresa May Coin (MAY) network information based on
    https://github.com/zulufourm1ke/theresamaycoin-v1.0.1.0/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'theresamaycoin'
    symbols = ('MAY', )
    nodes = ('86.53.121.36', )
    port = 35010
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 178
    }


class TheresamaycoinTestNet(Theresamaycoin):
    """
    Class with all the necessary Theresa May Coin (MAY) testing network information based on
    https://github.com/zulufourm1ke/theresamaycoin-v1.0.1.0/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-theresamaycoin'
    seeds = ()
    port = 25714
    message_start = b'\xad\xf1\xc2\xaf'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
