"""Module with different attributes and program values"""


WINDOW_SIZE = 824, 690

# Menu buttons styles
# ---------------------------------------------------
NORMAL_MENU_BTN_STYLE = """
QPushButton {
    background: #6900bf;
    border-radius: 10px;
    color: #f0f0f0;
}

QPushButton::hover {
    background: #6800ad;
}
"""

CHOSED_MENU_BTN_STYLE = """
QPushButton {
    background: #570091;
    border-radius: 10px;
    color: #f0f0f0;
}
"""
# ---------------------------------------------------

# Errors texts
# ---------------------------------------------------
ENCRYPTION_ERROR_TEXT = """
Не вдалося зашифрувати файл
Можливі причини:
    - Программа створює зашифрований файл за шляхом розшифрованого. У такому випадку спробуйте зашифрувати файл ще раз
    - Це системний файл
"""

DECRYPTION_ERROR_TEXT = """
Не вдалося розшифрувати файл
Можливі причини:
    - Невірний пароль або алгоритм шифрування паролю
    - Файл пошкодженний
    - Це системний файл
"""
# ---------------------------------------------------
