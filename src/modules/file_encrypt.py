"""Module to encrypt and decrypt files with password"""


import random
import os
from pyAesCrypt import encryptFile, decryptFile
from .hash_encrypt import get_hash_sum


def __get_encrypt_or_decrypt_file_path(path, path_format):
    """Get encrypt or decrypt file path"""
    path = os.path.join(os.path.dirname(path), f'{random.randint(1, 10_000)}.{path_format}')
    return path


def encrypt_file(path, password, algorithm=None):
    """Encrypt file using library pyAesCrypt"""
    if algorithm:
        password = get_hash_sum(algorithm, password)

    result_path = __get_encrypt_or_decrypt_file_path(path, 'aes')
    encryptFile(path, result_path, password)
    return result_path


def decrypt_file(path, password, algorithm=None):
    """Decrypt file using library pyAesCrypt"""
    if algorithm:
        password = get_hash_sum(algorithm, password)

    result_path = __get_encrypt_or_decrypt_file_path(path, 'txt')
    decryptFile(path, result_path, password)
    return result_path
