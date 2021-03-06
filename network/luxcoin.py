from clove.network.bitcoin import Bitcoin


class LUXCoin(Bitcoin):
    """
    Class with all the necessary LUX network information based on
    https://github.com/216k155/lux/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'luxcoin'
    symbols = ('LUX', )
    seeds = ('luxseed1.luxcore.io', 'luxseed2.luxcore.io', 'luxseed3.luxcore.io', 'luxseed4.luxcore.io')
    port = 26868
    message_start = b'\xf9\x73\xc9\xa7'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 48,
        'SECRET_KEY': 155
    }


class LUXCoinTestNet(LUXCoin):
    """
    Class with all the necessary LUX testing network information based on
    https://github.com/216k155/lux/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-luxcoin'
    nodes = ('88.198.192.110', )
    seeds = ()
    port = 28333
    message_start = b'\x54\x67\x56\xab'
    base58_prefixes = {
        'PUBKEY_ADDR': 139,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
