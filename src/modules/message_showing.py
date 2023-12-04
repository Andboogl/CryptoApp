"""Module for displaying different messages in QMessageBox"""


from PyQt6.QtWidgets import QMessageBox


class MessageBoxShowing:
    """Class for displaying different messages in QMessageBox"""
    def __init__(self, main_window):
        self.main_window = main_window

    def default(self, text):
        """Show default type of QMessageBox"""
        message_box = QMessageBox()
        message_box.setText(text)
        message_box.exec()

    def error(self, text, detailed_text):
        """Show error QMessageBox"""
        message_box = QMessageBox()
        message_box.setText(text)
        message_box.setDetailedText(detailed_text)
        message_box.exec()
