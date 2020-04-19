from os import urandom
from base58 import b58encode


def generate_slug():
    return b58encode(urandom(256))[:8][::-1].decode()
