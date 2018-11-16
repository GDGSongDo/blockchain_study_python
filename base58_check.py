"""
# SITE: BitCoin.it/Wiki
# URL: https://en.bitcoin.it/wiki/Base58Check_encoding
# The Base58 symbol chart used in Bitcoin is specific to the Bitcoin project
# and is not intended to be the same as any other Base58 implementation used
# outside the context of Bitcoin (the characters excluded are: 0, O, I, and l).
# -----------------------------------------------
#
# code_string = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
# x = convert_bytes_to_big_integer(hash_result)
## output_string = ""
#
# while(x > 0) {
#         (x, remainder) = divide(x, 58)
#         output_string.append(code_string[remainder])
#     }
#
# repeat(number_of_leading_zero_bytes_in_hash)  {
#     output_string.append(code_string[0]);
#     }
#
# output_string.reverse();
#
"""
# print(__doc__)
import base64

def show_base64_len(string):
    _a = base64.b64encode(string.encode())
    print(_a, len(_a),"bits")


strings = [
    "hello~ world!",
    "outside the context of Bitcoin (the characters excluded are: 0, O, I, and l).",
    "9d55e1f7058e9a79725974caa41d1ba09d693c5d3e365ea03985758e8e612f06",
    "b29cbbbbc2ce5f0c7968b8be355b6d953b4fa0bd04cf513faa290b67a6c51b55",
    "ff73868b0024599a5dd6b2417d3ee6d2556f19545fbf573ba0db39a27f790691",
    "0000000000f1ef4222b5c36c10001e4bea9811f1bdaa7265b194fe88b53a2220",
    "2174b1310a4360b9e1aaa80d110c60f1b1aae515f98a2b2de9b699",
    "c2a02c51118ee54745ae3e79d500619bf3d533e98ecc",
    "8b2efd253555667e564eb47f683ac6dfa1",
    "3a4c345ba49d6c484764c2bca",
    "d3ee6d251",

    "1",
    "0",
    "2",
    "3",

    "a",
    "A",

    "b",
    "B",
    ]

for string in strings:
    show_base64_len(string)
