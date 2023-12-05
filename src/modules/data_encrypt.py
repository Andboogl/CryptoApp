"""Module to encrypt and decrypt strings with data"""


import random


def encrypt_string_with_data(string: str):
    """
    Args:
        string (str): string to encrypt

    Returns tuple
    Tuple[0] it's encrypted string, and Tuple[1] it's data to decrypt string
    Whithout this data you can't decrypt string
    """
    encrypted = ''
    data_to_decrypt = []

    for element in string:
        number = random.randint(1, 10_000)
        encrypted += str(ord(element) + number) + random.choice(['D', 'T', 'L', 'M'])
        data_to_decrypt.append(number)

    return encrypted[0:-1], tuple(data_to_decrypt)


def decrypt_string_with_data(encrypted: str, data_to_decrypt):
    """Decrypt encrypted string

    Args:
        encrypted (str): encrypted string
        data_to_decrypt (tuple or list): data to decrypt

    Returns:
        str: decrypted string
    """
    new_encrypted = []
    counter = 0
    last_num = 0

    for i in encrypted:
        if i in ('D', 'T', 'L', 'M'):
            new_encrypted.append(encrypted[last_num:counter])
            last_num = counter + 1

        else:
            if counter + 1 == len(encrypted):
                new_encrypted.append(encrypted[last_num:])

        counter += 1

    encrypted = new_encrypted.copy()

    decrypted = ''
    symbols_and_data = list(zip(encrypted, data_to_decrypt))
    counter = 0

    for i in encrypted:
        decrypted += chr(int(i) - symbols_and_data[counter][1])
        counter += 1

    return decrypted


if __name__ == '__main__':
    string = input()
    encrypted = encrypt_string_with_data(string)
    decrypted = decrypt_string_with_data(encrypted[0], encrypted[1])
    print(encrypted)
    print(decrypted)
