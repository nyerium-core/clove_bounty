from clove.network.bitcoin import Bitcoin


class BlitzCash(Bitcoin):
    """
    Class with all the necessary BlitzCash (BLITZ) network information based on
    https://bitbucket.org/blitz-dev/blitz-public/src/7ccf18cfc03175a53d6402e4036eff3508f40bab/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'blitzcash'
    symbols = ('BLITZ', )
    seeds = ('blitz1.mooo.com', 'blitz2.mooo.com',
             'blitz3.mooo.com', 'blitz4.mooo.com', 'blitz5.mooo.com')
    port = 9627
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 115,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 243
    }

# no testnet
