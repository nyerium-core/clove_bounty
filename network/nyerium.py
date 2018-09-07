from clove.network.bitcoin import Bitcoin


class Nyerium(Bitcoin):
    """
    Class with all the necessary Nyerium network information based on
    https://github.com/nyerium-core/nyerium/blob/master/src/chainparams.cpp
    (date of access: 09/07/2018)
    """
    name = 'nyerium'
    symbols = ('NYEX', )
    seeds = ("35.154.221.49", )
    port = 57418
    message_start = b'\x6a\x4b\x4c\x5d'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 212
    }

class NyeriumTestNet(Nyerium):
    """
    Class with all the necessary Nyerium network information based on
    https://github.com/nyerium-core/nyerium/blob/master/src/chainparams.cpp
    (date of access: 09/07/2018)
    """
    name = 'test-nyerium'
    seeds = ()
    nodes = ("80.211.145.115", "13.127.26.220")
    port = 51434
    message_start = b'\x4f\x7e\x6d\xbc'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
