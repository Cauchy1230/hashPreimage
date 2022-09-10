import hashlib
import os
import random
import string

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return

    source = string.ascii_letters + string.digits
    start = ""
    m = hashlib.sha256()
    while True:
        char = random.choice(source)
        start += char
        m.update(char.encode('utf-8'))
        new_hex = m.hexdigest()
        if same_bits(new_hex, target_string):
            break
    nonce = bytes(start, 'utf-8')
    return( nonce )

def same_bits(bit, bit_str):
    bit = int(bit, 16)
    bit = bin(bit)[2:]
    bit = bit[::-1]
    bit_str = bit_str[::-1]
    for i in range(min(len(bit), len(bit_str))):
        if bit[i] == bit_str[i]:
            continue
        else:
            return False
    return True


