"""Module with different interface functions"""


from .const import CHOSED_MENU_BTN_STYLE, NORMAL_MENU_BTN_STYLE


class SwitchingQStackedWidget:
    """Class for toggle QStackedWidget"""
    def __init__(self, design_widgets):
        self.design = design_widgets
        self.checked_btn = self.design.menu_hash_encrypt

    def menu_hash_encrypt_btn(self):
        """
        Function for changing the current
        button to another menu button
        """
        self.design.stackedWidget.setCurrentIndex(0)
        self.design.menu_hash_encrypt.setStyleSheet(CHOSED_MENU_BTN_STYLE)

        if self.checked_btn != self.design.menu_hash_encrypt:
            self.checked_btn.setStyleSheet(NORMAL_MENU_BTN_STYLE)
            self.checked_btn = self.design.menu_hash_encrypt

    def menu_file_encrypt_btn(self):
        """
        Function for changing the current
        button to another menu button
        """
        self.design.stackedWidget.setCurrentIndex(1)
        self.design.menu_file_encrypt.setStyleSheet(CHOSED_MENU_BTN_STYLE)

        if self.checked_btn != self.design.menu_file_encrypt:
            self.checked_btn.setStyleSheet(NORMAL_MENU_BTN_STYLE)
            self.checked_btn = self.design.menu_file_encrypt

    def menu_file_decrypt_btn(self):
        """
        Function for changing the current
        button to another menu button
        """
        self.design.stackedWidget.setCurrentIndex(2)
        self.design.menu_file_decrypt.setStyleSheet(CHOSED_MENU_BTN_STYLE)

        if self.checked_btn != self.design.menu_file_decrypt:
            self.checked_btn.setStyleSheet(NORMAL_MENU_BTN_STYLE)
            self.checked_btn = self.design.menu_file_decrypt

    def about_application_btn(self):
        """
        Function for changing the current
        button to another menu button
        """
        self.design.stackedWidget.setCurrentIndex(3)
        self.design.about_application.setStyleSheet(CHOSED_MENU_BTN_STYLE)

        if self.checked_btn != self.design.about_application:
            self.checked_btn.setStyleSheet(NORMAL_MENU_BTN_STYLE)
            self.checked_btn = self.design.about_application
