"""Module to copy data to user clipboard"""


from PyQt6.QtWidgets import QApplication


def copy_text_to_clipboard(string):
    """Copy string to user clipboard"""
    clipboard = QApplication.clipboard()
    clipboard.setText(string)
