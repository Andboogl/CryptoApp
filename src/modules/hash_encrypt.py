"""Hash encryption module"""


import hashlib


def __sha1(value):
    return hashlib.sha1(value.encode('utf-16')).hexdigest()

def __sha224(value):
    return hashlib.sha224(value.encode('utf-16')).hexdigest()

def __sha256(value):
    return hashlib.sha256(value.encode('utf-16')).hexdigest()

def __sha384(value):
    return hashlib.sha384(value.encode('utf-16')).hexdigest()

def __sha512(value):
    return hashlib.sha512(value.encode('utf-16')).hexdigest()

def __md5(value):
    return hashlib.md5(value.encode('utf-16')).hexdigest()


def get_hash_sum(algorithm, value):
    """
    Get the hash sum using one
    of the available hashing algorithms
    """
    algorithm = algorithm.lower()

    if algorithm == 'sha1':
        return __sha1(value)

    elif algorithm == 'sha224':
        return __sha224(value)

    elif algorithm == 'sha256':
        return __sha256(value)

    elif algorithm == 'sha384':
        return __sha384(value)

    elif algorithm == 'sha512':
        return __sha512(value)

    elif algorithm == 'md5':
        return __md5(value)
