"""
Main module (entry point). Runs the program
"""


from sys import argv
from PyQt6.QtWidgets import QApplication
from app import Window


def main():
    """Function runs the program"""
    app = QApplication(argv)
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
