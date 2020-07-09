# User has random value sk - spending key
# https://zips.z.cash/zip-0032

from hashlib import blake2b

def BLAKE2b512(personalisation_string: bytes, data: bytes):
    resp = blake2b(data=data, person=personalisation_string)
    assert len(resp)==32 and isinstance(resp, bytes)
    return resp


S = bytes(b'   ')
assert len(S)>=32

I = BLAKE2b512(b'ZcashIPSapling', S)
assert len(I) == 64
I_l = I[:32]    # sk_m -master spending key
I_r = I[-32:]   # c_m  -master chain code

