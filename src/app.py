"""
The module is needed to create the main window
of the program and to process the interface
"""


from PyQt6 import QtWidgets
from design.ui import Ui_MainWindow
import modules


class Window(QtWidgets.QMainWindow):
    """Main window class"""
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        # Loading design
        self.design = Ui_MainWindow()
        self.design.setupUi(self)

        self.message_box_showing = modules.MessageBoxShowing(self)

        # Button pressing
        self.design.exit_out.clicked.connect(exit)
        self.design.hash_encrypt_encrypt.clicked.connect(self.hash_user_string)
        self.design.copy_hash_sum.clicked.connect(
            lambda: modules.copy_text_to_clipboard(self.design.hash_sum.text())
            )
        self.design.copy_encrypted_string.clicked.connect(
            lambda: modules.copy_text_to_clipboard(self.design.encrypted_with_data_string.text())
            )
        self.design.copy_data_to_decrypt_string.clicked.connect(
            lambda: modules.copy_text_to_clipboard(self.design.data_to_decrypt_encrypted.text())
            )
        self.design.copy_decrypted_string.clicked.connect(
            lambda: modules.copy_text_to_clipboard(self.design.decrypted_string.text())
        )
        self.design.decrypt_data.clicked.connect(self.decrypt_with_data)
        self.design.chose_file_to_encrypt.clicked.connect(self.chose_encrypt_file)
        self.design.encrypt_file.clicked.connect(self.encrypt_file)
        self.design.chose_file_to_decrypt.clicked.connect(self.chose_decrypt_file)
        self.design.decrypt_file.clicked.connect(self.decrypt_file)
        self.design.encrypt_with_data.clicked.connect(self.encrypt_with_data)

        # Switching QStackedWidget
        self.stacked_widget_switching = modules.SwitchingQStackedWidget(self.design)

        self.design.menu_hash_encrypt.clicked.connect(
            self.stacked_widget_switching.menu_hash_encrypt_btn)
        self.design.menu_file_encrypt.clicked.connect(
            self.stacked_widget_switching.menu_file_encrypt_btn)
        self.design.menu_file_decrypt.clicked.connect(
            self.stacked_widget_switching.menu_file_decrypt_btn)
        self.design.about_application.clicked.connect(
            self.stacked_widget_switching.about_application_btn)
        self.design.menu_encrypt_with_data.clicked.connect(
            self.stacked_widget_switching.menu_encrypt_with_data)
        self.design.menu_decrypt_with_data.clicked.connect(
            self.stacked_widget_switching.menu_decrypt_with_data)

        self.stacked_widget_switching.menu_hash_encrypt_btn()
        self.setFixedSize(*modules.WINDOW_SIZE)

    def encrypt_with_data(self):
        """Encrypt user string with data"""
        user_string = self.design.encrypt_with_data_string.text()

        if user_string.strip():
            encrypted = modules.encrypt_string_with_data(user_string) # (<ENCRYPTED>, <DATA_TO_DECRYPT>)
            self.design.encrypted_with_data_string.setText(encrypted[0])
            self.design.data_to_decrypt_encrypted.setText(str(encrypted[1]))

        else:
            self.message_box_showing.default('Введіть строку для шифрування')

    def decrypt_with_data(self):
        """Decrypt encrypted string with data"""
        encrypted = self.design.encrypted_string_decrypt_data.text()
        data_to_decrypt = self.design.data_to_decrypt_data.text()

        if encrypted.strip() and data_to_decrypt.strip():
            try:
                data_to_decrypt = data_to_decrypt.replace('(', '')
                data_to_decrypt = data_to_decrypt.replace(')', '')
                data_to_decrypt = tuple(int(i) for i in data_to_decrypt.split(','))

                decrypted = modules.decrypt_string_with_data(encrypted, data_to_decrypt)
                self.design.decrypted_string.setText(decrypted)

            except Exception as error:
                self.message_box_showing.error(
                    'Не вдалося розшифрувати строку. Перевірте що зашифрована строка та данні для розшифрування вірні.',
                    str(error)
                )

        else:
            self.message_box_showing.default('Введіть всі поля')

    def hash_user_string(self):
        """Hash the string that the user selected"""
        user_string = self.design.hash_encrypt_string.text()
        algorithm = self.design.hash_encrypt_algorithm.currentText()

        self.design.hash_sum.setText(modules.get_hash_sum(algorithm, user_string))

    def chose_encrypt_file(self):
        """Chose encrypt file path"""
        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Chose file', '/')[0]

        # If users didn't clicked "Cancel" button
        if file.strip():
            self.design.path_to_encrypt_file.setText(file)

    def chose_decrypt_file(self):
        """Chose decrypt file path"""
        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Chose file', '/')[0]

        # If users didn't clicked "Cancel" button
        if file.strip():
            self.design.file_to_decrypt_path.setText(file)

    def encrypt_file(self):
        """Encrypt user's file"""
        file_path = self.design.path_to_encrypt_file.text()
        password = self.design.file_to_encrypt_password.text()

        algorithm = self.design.file_to_encrypt_password_encrypt.currentText()

        if algorithm.lower() == 'нема':
            algorithm = None

        if file_path.strip():
            if password.strip():
                try:
                    result_path = modules.encrypt_file(file_path, password, algorithm)
                    self.message_box_showing.default(
                        f'Зашифрована версія створенна за шляхом {result_path}')

                except Exception as error:
                    text = modules.ENCRYPTION_ERROR_TEXT
                    self.message_box_showing.error(text, str(error))

            else:
                self.message_box_showing.default('Виберіть пароль')

        else:
            self.message_box_showing.default('Виберіть файл')

    def decrypt_file(self):
        """Encrypt user's file"""
        file_path = self.design.file_to_decrypt_path.text()
        password = self.design.decrypt_file_password.text()

        algorithm = self.design.decrypt_file_password_algorithm.currentText()

        if algorithm.lower() == 'нема':
            algorithm = None

        if file_path.strip():
            if password.strip():
                try:
                    result_path = modules.decrypt_file(file_path, password, algorithm)
                    self.message_box_showing.default(
                        f'Розшифрована версія створенна за шляхом {result_path}')

                except Exception as error:
                    text = modules.DECRYPTION_ERROR_TEXT
                    self.message_box_showing.error(text, str(error))

            else:
                self.message_box_showing.default('Введіть пароль')

        else:
            self.message_box_showing.default('Виберіть файл')
