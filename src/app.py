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
        self.design.copy_hash_sum.clicked.connect(self.copy_hash_sum)
        self.design.chose_file_to_encrypt.clicked.connect(self.chose_encrypt_file)
        self.design.encrypt_file.clicked.connect(self.encrypt_file)
        self.design.chose_file_to_decrypt.clicked.connect(self.chose_decrypt_file)
        self.design.decrypt_file.clicked.connect(self.decrypt_file)

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

        self.stacked_widget_switching.menu_hash_encrypt_btn()
        self.setFixedSize(*modules.WINDOW_SIZE)

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

    def copy_hash_sum(self):
        """Copy hash-sum that generated application"""
        text = self.design.hash_sum.text()

        if text.strip():
            clipboard = QtWidgets.QApplication.clipboard()
            clipboard.setText(text)

            self.message_box_showing.default('Скопійовано')

        else:
            self.message_box_showing.default('Ви нічого не зашифрували')
