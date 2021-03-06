from clove.network.bitcoin import Bitcoin


class Spots(Bitcoin):
    """
    Class with all the necessary Spots network information based on
    https://github.com/thespt/spots2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'spots'
    symbols = ('SPT', )
    seeds = ("spots.dnsseed.crypto2.net", )
    port = 4588
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 178
    }


class SpotsTestNet(Spots):
    """
    Class with all the necessary Spots testing network information based on
    https://github.com/thespt/spots2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-spots'
    seeds = ("dstest.theSPT.com", )
    port = 15588
    message_start = b'\xfd\xc2\xb8\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 26,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 154
    }
