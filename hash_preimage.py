import hashlib
import os
import random
import string

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return

    source = string.ascii_letters + string.digits
    random_number = random.randint(1, 10)
    ran_str = ""
    i = 0
    while i < random_number:
        char = random.choice(source)
        ran_str += char
        i += 1
    result = hashlib.sha256(ran_str.encode('utf-8')).hexdigest()
    same = count_trailing_same(result, target_string)
    nonce = same
    return( nonce )

def count_trailing_same(bit, bit_str):
    bit = int(bit, 16)
    bit = bin(bit)[2:]
    bit = bit[::-1]
    bit_str = bit_str[::-1]
    same = 0
    for i in range(min(len(bit), len(bit_str))):
        if bit[i] == bit_str[i]:
            same += 1
        else:
            break
    return same

