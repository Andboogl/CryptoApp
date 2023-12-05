# Form implementation generated from reading ui file '/Users/andreykovalskiy/Documents/Python/Projects/CryptoApp/src/design/ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 685)
        MainWindow.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QFrame(parent=self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 831, 691))
        self.background.setStyleSheet("background: #430073;")
        self.background.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.background.setObjectName("background")
        self.frame = QtWidgets.QFrame(parent=self.background)
        self.frame.setGeometry(QtCore.QRect(10, 10, 271, 661))
        self.frame.setStyleSheet("background: #5e00a1;\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(20, 0, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(80)
        font.setBold(True)
        # font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #f0f0f0;")
        self.label.setObjectName("label")
        self.menu_hash_encrypt = QtWidgets.QPushButton(parent=self.frame)
        self.menu_hash_encrypt.setGeometry(QtCore.QRect(10, 90, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.menu_hash_encrypt.setFont(font)
        self.menu_hash_encrypt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menu_hash_encrypt.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/hash.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menu_hash_encrypt.setIcon(icon)
        self.menu_hash_encrypt.setIconSize(QtCore.QSize(60, 60))
        self.menu_hash_encrypt.setCheckable(False)
        self.menu_hash_encrypt.setObjectName("menu_hash_encrypt")
        self.menu_file_encrypt = QtWidgets.QPushButton(parent=self.frame)
        self.menu_file_encrypt.setGeometry(QtCore.QRect(10, 170, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.menu_file_encrypt.setFont(font)
        self.menu_file_encrypt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menu_file_encrypt.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menu_file_encrypt.setIcon(icon1)
        self.menu_file_encrypt.setIconSize(QtCore.QSize(60, 60))
        self.menu_file_encrypt.setCheckable(False)
        self.menu_file_encrypt.setObjectName("menu_file_encrypt")
        self.about_application = QtWidgets.QPushButton(parent=self.frame)
        self.about_application.setGeometry(QtCore.QRect(10, 500, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.about_application.setFont(font)
        self.about_application.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.about_application.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/dandruff.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.about_application.setIcon(icon2)
        self.about_application.setIconSize(QtCore.QSize(60, 60))
        self.about_application.setCheckable(False)
        self.about_application.setObjectName("about_application")
        self.exit_out = QtWidgets.QPushButton(parent=self.frame)
        self.exit_out.setGeometry(QtCore.QRect(10, 580, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.exit_out.setFont(font)
        self.exit_out.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.exit_out.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exit_out.setIcon(icon3)
        self.exit_out.setIconSize(QtCore.QSize(60, 60))
        self.exit_out.setCheckable(False)
        self.exit_out.setObjectName("exit_out")
        self.menu_file_decrypt = QtWidgets.QPushButton(parent=self.frame)
        self.menu_file_decrypt.setGeometry(QtCore.QRect(10, 250, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.menu_file_decrypt.setFont(font)
        self.menu_file_decrypt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menu_file_decrypt.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/decrypt.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menu_file_decrypt.setIcon(icon4)
        self.menu_file_decrypt.setIconSize(QtCore.QSize(50, 60))
        self.menu_file_decrypt.setCheckable(False)
        self.menu_file_decrypt.setObjectName("menu_file_decrypt")
        self.menu_encrypt_with_data = QtWidgets.QPushButton(parent=self.frame)
        self.menu_encrypt_with_data.setGeometry(QtCore.QRect(10, 330, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.menu_encrypt_with_data.setFont(font)
        self.menu_encrypt_with_data.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menu_encrypt_with_data.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/data_encrypt.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menu_encrypt_with_data.setIcon(icon5)
        self.menu_encrypt_with_data.setIconSize(QtCore.QSize(50, 60))
        self.menu_encrypt_with_data.setCheckable(False)
        self.menu_encrypt_with_data.setObjectName("menu_encrypt_with_data")
        self.menu_decrypt_with_data = QtWidgets.QPushButton(parent=self.frame)
        self.menu_decrypt_with_data.setGeometry(QtCore.QRect(10, 410, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.menu_decrypt_with_data.setFont(font)
        self.menu_decrypt_with_data.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menu_decrypt_with_data.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        self.menu_decrypt_with_data.setIcon(icon5)
        self.menu_decrypt_with_data.setIconSize(QtCore.QSize(50, 60))
        self.menu_decrypt_with_data.setCheckable(False)
        self.menu_decrypt_with_data.setObjectName("menu_decrypt_with_data")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.background)
        self.stackedWidget.setGeometry(QtCore.QRect(290, 20, 511, 641))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(parent=self.page)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        # font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #f0f0f0;")
        self.label_2.setObjectName("label_2")
        self.hash_encrypt_string = QtWidgets.QLineEdit(parent=self.page)
        self.hash_encrypt_string.setGeometry(QtCore.QRect(10, 80, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.hash_encrypt_string.setFont(font)
        self.hash_encrypt_string.setStyleSheet("color: #000000;\n"
"background-color: #f0f0f0;\n"
"border-radius: 10px;\n"
"padding-left: 10px;")
        self.hash_encrypt_string.setObjectName("hash_encrypt_string")
        self.hash_encrypt_algorithm = QtWidgets.QComboBox(parent=self.page)
        self.hash_encrypt_algorithm.setGeometry(QtCore.QRect(10, 140, 104, 26))
        self.hash_encrypt_algorithm.setStyleSheet("background: none;")
        self.hash_encrypt_algorithm.setObjectName("hash_encrypt_algorithm")
        self.hash_encrypt_algorithm.addItem("")
        self.hash_encrypt_algorithm.addItem("")
        self.hash_encrypt_algorithm.addItem("")
        self.hash_encrypt_algorithm.addItem("")
        self.hash_encrypt_algorithm.addItem("")
        self.hash_encrypt_algorithm.addItem("")
        self.lineEdit_2 = QtWidgets.QLabel(parent=self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 140, 151, 21))
        font = QtGui.QFont()
        font.setBold(False)
        # font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: #f0f0f0;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.hash_encrypt_encrypt = QtWidgets.QPushButton(parent=self.page)
        self.hash_encrypt_encrypt.setGeometry(QtCore.QRect(10, 180, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hash_encrypt_encrypt.setFont(font)
        self.hash_encrypt_encrypt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.hash_encrypt_encrypt.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        self.hash_encrypt_encrypt.setIconSize(QtCore.QSize(60, 60))
        self.hash_encrypt_encrypt.setCheckable(False)
        self.hash_encrypt_encrypt.setObjectName("hash_encrypt_encrypt")
        self.label_3 = QtWidgets.QLabel(parent=self.page)
        self.label_3.setGeometry(QtCore.QRect(180, 260, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        # font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #f0f0f0;")
        self.label_3.setObjectName("label_3")
        self.hash_sum = QtWidgets.QLineEdit(parent=self.page)
        self.hash_sum.setGeometry(QtCore.QRect(10, 310, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.hash_sum.setFont(font)
        self.hash_sum.setStyleSheet("color: #000000;\n"
"background-color: #f0f0f0;\n"
"border-radius: 10px;\n"
"padding-left: 10px;")
        self.hash_sum.setReadOnly(True)
        self.hash_sum.setObjectName("hash_sum")
        self.copy_hash_sum = QtWidgets.QPushButton(parent=self.page)
        self.copy_hash_sum.setGeometry(QtCore.QRect(10, 370, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.copy_hash_sum.setFont(font)
        self.copy_hash_sum.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.copy_hash_sum.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        self.copy_hash_sum.setIconSize(QtCore.QSize(60, 60))
        self.copy_hash_sum.setCheckable(False)
        self.copy_hash_sum.setObjectName("copy_hash_sum")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_4 = QtWidgets.QLabel(parent=self.page_2)
        self.label_4.setGeometry(QtCore.QRect(30, 0, 441, 71))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        # font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #f0f0f0;")
        self.label_4.setObjectName("label_4")
        self.path_to_encrypt_file = QtWidgets.QLineEdit(parent=self.page_2)
        self.path_to_encrypt_file.setGeometry(QtCore.QRect(10, 80, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.path_to_encrypt_file.setFont(font)
        self.path_to_encrypt_file.setStyleSheet("color: #000000;\n"
"background-color: #f0f0f0;\n"
"border-radius: 10px;\n"
"padding-left: 10px;")
        self.path_to_encrypt_file.setReadOnly(True)
        self.path_to_encrypt_file.setObjectName("path_to_encrypt_file")
        self.chose_file_to_encrypt = QtWidgets.QPushButton(parent=self.page_2)
        self.chose_file_to_encrypt.setGeometry(QtCore.QRect(10, 140, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chose_file_to_encrypt.setFont(font)
        self.chose_file_to_encrypt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.chose_file_to_encrypt.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        self.chose_file_to_encrypt.setIconSize(QtCore.QSize(60, 60))
        self.chose_file_to_encrypt.setCheckable(False)
        self.chose_file_to_encrypt.setObjectName("chose_file_to_encrypt")
        self.file_to_encrypt_password_encrypt = QtWidgets.QComboBox(parent=self.page_2)
        self.file_to_encrypt_password_encrypt.setGeometry(QtCore.QRect(10, 280, 104, 26))
        self.file_to_encrypt_password_encrypt.setStyleSheet("background: none;")
        self.file_to_encrypt_password_encrypt.setObjectName("file_to_encrypt_password_encrypt")
        self.file_to_encrypt_password_encrypt.addItem("")
        self.file_to_encrypt_password_encrypt.addItem("")
        self.file_to_encrypt_password_encrypt.addItem("")
        self.file_to_encrypt_password_encrypt.addItem("")
        self.file_to_encrypt_password_encrypt.addItem("")
        self.file_to_encrypt_password_encrypt.addItem("")
        self.file_to_encrypt_password_encrypt.addItem("")
        self.label_5 = QtWidgets.QLabel(parent=self.page_2)
        self.label_5.setGeometry(QtCore.QRect(120, 283, 151, 16))
        font = QtGui.QFont()
        font.setBold(False)
        # font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #f0f0f0;")
        self.label_5.setObjectName("label_5")
        self.encrypt_file = QtWidgets.QPushButton(parent=self.page_2)
        self.encrypt_file.setGeometry(QtCore.QRect(10, 320, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.encrypt_file.setFont(font)
        self.encrypt_file.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.encrypt_file.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        self.encrypt_file.setIconSize(QtCore.QSize(60, 60))
        self.encrypt_file.setCheckable(False)
        self.encrypt_file.setObjectName("encrypt_file")
        self.label_7 = QtWidgets.QLabel(parent=self.page_2)
        self.label_7.setGeometry(QtCore.QRect(70, 390, 351, 16))
        self.label_7.setStyleSheet("color: #f0f0f0;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.page_2)
        self.label_8.setGeometry(QtCore.QRect(10, 410, 481, 16))
        self.label_8.setStyleSheet("color: #f0f0f0;")
        self.label_8.setObjectName("label_8")
        self.file_to_encrypt_password = QtWidgets.QLineEdit(parent=self.page_2)
        self.file_to_encrypt_password.setGeometry(QtCore.QRect(10, 220, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.file_to_encrypt_password.setFont(font)
        self.file_to_encrypt_password.setStyleSheet("color: #000000;\n"
"background-color: #f0f0f0;\n"
"border-radius: 10px;\n"
"padding-left: 10px;")
        self.file_to_encrypt_password.setReadOnly(False)
        self.file_to_encrypt_password.setObjectName("file_to_encrypt_password")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_6 = QtWidgets.QLabel(parent=self.page_3)
        self.label_6.setGeometry(QtCore.QRect(30, 0, 461, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        # font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #f0f0f0;")
        self.label_6.setObjectName("label_6")
        self.file_to_decrypt_path = QtWidgets.QLineEdit(parent=self.page_3)
        self.file_to_decrypt_path.setGeometry(QtCore.QRect(10, 70, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.file_to_decrypt_path.setFont(font)
        self.file_to_decrypt_path.setStyleSheet("color: #000000;\n"
"background-color: #f0f0f0;\n"
"border-radius: 10px;\n"
"padding-left: 10px;")
        self.file_to_decrypt_path.setReadOnly(True)
        self.file_to_decrypt_path.setObjectName("file_to_decrypt_path")
        self.chose_file_to_decrypt = QtWidgets.QPushButton(parent=self.page_3)
        self.chose_file_to_decrypt.setGeometry(QtCore.QRect(10, 130, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chose_file_to_decrypt.setFont(font)
        self.chose_file_to_decrypt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.chose_file_to_decrypt.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        self.chose_file_to_decrypt.setIconSize(QtCore.QSize(60, 60))
        self.chose_file_to_decrypt.setCheckable(False)
        self.chose_file_to_decrypt.setObjectName("chose_file_to_decrypt")
        self.decrypt_file_password = QtWidgets.QLineEdit(parent=self.page_3)
        self.decrypt_file_password.setGeometry(QtCore.QRect(10, 210, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.decrypt_file_password.setFont(font)
        self.decrypt_file_password.setStyleSheet("color: #000000;\n"
"background-color: #f0f0f0;\n"
"border-radius: 10px;\n"
"padding-left: 10px;")
        self.decrypt_file_password.setReadOnly(False)
        self.decrypt_file_password.setObjectName("decrypt_file_password")
        self.decrypt_file_password_algorithm = QtWidgets.QComboBox(parent=self.page_3)
        self.decrypt_file_password_algorithm.setGeometry(QtCore.QRect(10, 270, 104, 26))
        self.decrypt_file_password_algorithm.setStyleSheet("background: none;")
        self.decrypt_file_password_algorithm.setObjectName("decrypt_file_password_algorithm")
        self.decrypt_file_password_algorithm.addItem("")
        self.decrypt_file_password_algorithm.addItem("")
        self.decrypt_file_password_algorithm.addItem("")
        self.decrypt_file_password_algorithm.addItem("")
        self.decrypt_file_password_algorithm.addItem("")
        self.decrypt_file_password_algorithm.addItem("")
        self.decrypt_file_password_algorithm.addItem("")
        self.label_9 = QtWidgets.QLabel(parent=self.page_3)
        self.label_9.setGeometry(QtCore.QRect(120, 273, 151, 16))
        font = QtGui.QFont()
        font.setBold(False)
        # font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #f0f0f0;")
        self.label_9.setObjectName("label_9")
        self.decrypt_file = QtWidgets.QPushButton(parent=self.page_3)
        self.decrypt_file.setGeometry(QtCore.QRect(10, 300, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.decrypt_file.setFont(font)
        self.decrypt_file.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.decrypt_file.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        self.decrypt_file.setIconSize(QtCore.QSize(60, 60))
        self.decrypt_file.setCheckable(False)
        self.decrypt_file.setObjectName("decrypt_file")
        self.label_10 = QtWidgets.QLabel(parent=self.page_3)
        self.label_10.setGeometry(QtCore.QRect(70, 370, 381, 16))
        self.label_10.setStyleSheet("color: #f0f0f0;")
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.page_3)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_15 = QtWidgets.QLabel(parent=self.page_5)
        self.label_15.setGeometry(QtCore.QRect(20, 10, 471, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        # font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: #f0f0f0;")
        self.label_15.setObjectName("label_15")
        self.encrypt_with_data_string = QtWidgets.QLineEdit(parent=self.page_5)
        self.encrypt_with_data_string.setGeometry(QtCore.QRect(10, 90, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.encrypt_with_data_string.setFont(font)
        self.encrypt_with_data_string.setStyleSheet("color: #000000;\n"
"background-color: #f0f0f0;\n"
"border-radius: 10px;\n"
"padding-left: 10px;")
        self.encrypt_with_data_string.setReadOnly(False)
        self.encrypt_with_data_string.setObjectName("encrypt_with_data_string")
        self.encrypt_with_data = QtWidgets.QPushButton(parent=self.page_5)
        self.encrypt_with_data.setGeometry(QtCore.QRect(10, 150, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.encrypt_with_data.setFont(font)
        self.encrypt_with_data.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.encrypt_with_data.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        self.encrypt_with_data.setIconSize(QtCore.QSize(60, 60))
        self.encrypt_with_data.setCheckable(False)
        self.encrypt_with_data.setObjectName("encrypt_with_data")
        self.encrypted_with_data_string = QtWidgets.QLineEdit(parent=self.page_5)
        self.encrypted_with_data_string.setGeometry(QtCore.QRect(10, 230, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.encrypted_with_data_string.setFont(font)
        self.encrypted_with_data_string.setStyleSheet("color: #000000;\n"
"background-color: #f0f0f0;\n"
"border-radius: 10px;\n"
"padding-left: 10px;")
        self.encrypted_with_data_string.setReadOnly(True)
        self.encrypted_with_data_string.setObjectName("encrypted_with_data_string")
        self.data_to_decrypt_encrypted = QtWidgets.QLineEdit(parent=self.page_5)
        self.data_to_decrypt_encrypted.setGeometry(QtCore.QRect(10, 290, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.data_to_decrypt_encrypted.setFont(font)
        self.data_to_decrypt_encrypted.setStyleSheet("color: #000000;\n"
"background-color: #f0f0f0;\n"
"border-radius: 10px;\n"
"padding-left: 10px;")
        self.data_to_decrypt_encrypted.setReadOnly(True)
        self.data_to_decrypt_encrypted.setObjectName("data_to_decrypt_encrypted")
        self.copy_encrypted_string = QtWidgets.QPushButton(parent=self.page_5)
        self.copy_encrypted_string.setGeometry(QtCore.QRect(10, 350, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.copy_encrypted_string.setFont(font)
        self.copy_encrypted_string.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.copy_encrypted_string.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        self.copy_encrypted_string.setIconSize(QtCore.QSize(60, 60))
        self.copy_encrypted_string.setCheckable(False)
        self.copy_encrypted_string.setObjectName("copy_encrypted_string")
        self.copy_data_to_decrypt_string = QtWidgets.QPushButton(parent=self.page_5)
        self.copy_data_to_decrypt_string.setGeometry(QtCore.QRect(10, 420, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.copy_data_to_decrypt_string.setFont(font)
        self.copy_data_to_decrypt_string.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.copy_data_to_decrypt_string.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        self.copy_data_to_decrypt_string.setIconSize(QtCore.QSize(60, 60))
        self.copy_data_to_decrypt_string.setCheckable(False)
        self.copy_data_to_decrypt_string.setObjectName("copy_data_to_decrypt_string")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_16 = QtWidgets.QLabel(parent=self.page_6)
        self.label_16.setGeometry(QtCore.QRect(10, 0, 501, 71))
        font = QtGui.QFont()
        font.setPointSize(37)
        font.setBold(True)
        # font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: #f0f0f0;")
        self.label_16.setObjectName("label_16")
        self.encrypted_string_decrypt_data = QtWidgets.QLineEdit(parent=self.page_6)
        self.encrypted_string_decrypt_data.setGeometry(QtCore.QRect(10, 80, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.encrypted_string_decrypt_data.setFont(font)
        self.encrypted_string_decrypt_data.setStyleSheet("color: #000000;\n"
"background-color: #f0f0f0;\n"
"border-radius: 10px;\n"
"padding-left: 10px;")
        self.encrypted_string_decrypt_data.setReadOnly(False)
        self.encrypted_string_decrypt_data.setObjectName("encrypted_string_decrypt_data")
        self.data_to_decrypt_data = QtWidgets.QLineEdit(parent=self.page_6)
        self.data_to_decrypt_data.setGeometry(QtCore.QRect(10, 140, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.data_to_decrypt_data.setFont(font)
        self.data_to_decrypt_data.setStyleSheet("color: #000000;\n"
"background-color: #f0f0f0;\n"
"border-radius: 10px;\n"
"padding-left: 10px;")
        self.data_to_decrypt_data.setReadOnly(False)
        self.data_to_decrypt_data.setObjectName("data_to_decrypt_data")
        self.decrypt_data = QtWidgets.QPushButton(parent=self.page_6)
        self.decrypt_data.setGeometry(QtCore.QRect(10, 200, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.decrypt_data.setFont(font)
        self.decrypt_data.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.decrypt_data.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        self.decrypt_data.setIconSize(QtCore.QSize(60, 60))
        self.decrypt_data.setCheckable(False)
        self.decrypt_data.setObjectName("decrypt_data")
        self.decrypted_string = QtWidgets.QLineEdit(parent=self.page_6)
        self.decrypted_string.setGeometry(QtCore.QRect(10, 290, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.decrypted_string.setFont(font)
        self.decrypted_string.setStyleSheet("color: #000000;\n"
"background-color: #f0f0f0;\n"
"border-radius: 10px;\n"
"padding-left: 10px;")
        self.decrypted_string.setReadOnly(True)
        self.decrypted_string.setObjectName("decrypted_string")
        self.copy_decrypted_string = QtWidgets.QPushButton(parent=self.page_6)
        self.copy_decrypted_string.setGeometry(QtCore.QRect(10, 350, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.copy_decrypted_string.setFont(font)
        self.copy_decrypted_string.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.copy_decrypted_string.setStyleSheet("QPushButton {\n"
"    background: #6900bf;\n"
"    border-radius: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #6800ad;\n"
"}")
        self.copy_decrypted_string.setIconSize(QtCore.QSize(60, 60))
        self.copy_decrypted_string.setCheckable(False)
        self.copy_decrypted_string.setObjectName("copy_decrypted_string")
        self.stackedWidget.addWidget(self.page_6)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_11 = QtWidgets.QLabel(parent=self.page_4)
        self.label_11.setGeometry(QtCore.QRect(100, 0, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        # font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #f0f0f0;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.page_4)
        self.label_12.setGeometry(QtCore.QRect(150, 80, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        # font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #f0f0f0;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.page_4)
        self.label_13.setGeometry(QtCore.QRect(120, 210, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        # font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: #f0f0f0;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.page_4)
        self.label_14.setGeometry(QtCore.QRect(80, 120, 371, 381))
        self.label_14.setStyleSheet("background: none;")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("icons/author_logo.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CryptoApp"))
        self.label.setText(_translate("MainWindow", "Меню"))
        self.menu_hash_encrypt.setText(_translate("MainWindow", " Hash-шифрування"))
        self.menu_file_encrypt.setText(_translate("MainWindow", " Шифрування файлу"))
        self.about_application.setText(_translate("MainWindow", " Про программу"))
        self.exit_out.setText(_translate("MainWindow", " Вийти"))
        self.menu_file_decrypt.setText(_translate("MainWindow", " Розшифрування файлу"))
        self.menu_encrypt_with_data.setText(_translate("MainWindow", "Шифрування з данними"))
        self.menu_decrypt_with_data.setText(_translate("MainWindow", "Розшифрування з данними"))
        self.label_2.setText(_translate("MainWindow", "Hash-шифрування"))
        self.hash_encrypt_string.setPlaceholderText(_translate("MainWindow", "Введіть сюди сторку, яку хочете зашифрувати"))
        self.hash_encrypt_algorithm.setItemText(0, _translate("MainWindow", "Sha1"))
        self.hash_encrypt_algorithm.setItemText(1, _translate("MainWindow", "Sha224"))
        self.hash_encrypt_algorithm.setItemText(2, _translate("MainWindow", "Sha256"))
        self.hash_encrypt_algorithm.setItemText(3, _translate("MainWindow", "Sha384"))
        self.hash_encrypt_algorithm.setItemText(4, _translate("MainWindow", "Sha512"))
        self.hash_encrypt_algorithm.setItemText(5, _translate("MainWindow", "md5"))
        self.lineEdit_2.setText(_translate("MainWindow", "Алгоритм шифрування"))
        self.hash_encrypt_encrypt.setText(_translate("MainWindow", "Шифрувати"))
        self.label_3.setText(_translate("MainWindow", "Результат:"))
        self.hash_sum.setPlaceholderText(_translate("MainWindow", "Тут буде результат хешування (хеш-сума)"))
        self.copy_hash_sum.setText(_translate("MainWindow", "Копіювати результат"))
        self.label_4.setText(_translate("MainWindow", "Шифрування файлу"))
        self.path_to_encrypt_file.setPlaceholderText(_translate("MainWindow", "Шлях до файлу"))
        self.chose_file_to_encrypt.setText(_translate("MainWindow", "Вибрати..."))
        self.file_to_encrypt_password_encrypt.setItemText(0, _translate("MainWindow", "Нема"))
        self.file_to_encrypt_password_encrypt.setItemText(1, _translate("MainWindow", "Sha1"))
        self.file_to_encrypt_password_encrypt.setItemText(2, _translate("MainWindow", "Sha224"))
        self.file_to_encrypt_password_encrypt.setItemText(3, _translate("MainWindow", "Sha256"))
        self.file_to_encrypt_password_encrypt.setItemText(4, _translate("MainWindow", "Sha384"))
        self.file_to_encrypt_password_encrypt.setItemText(5, _translate("MainWindow", "Sha512"))
        self.file_to_encrypt_password_encrypt.setItemText(6, _translate("MainWindow", "md5"))
        self.label_5.setText(_translate("MainWindow", "Шифрування паролю"))
        self.encrypt_file.setText(_translate("MainWindow", "Шифрувати"))
        self.label_7.setText(_translate("MainWindow", "Увага! Формат файлу при шифруванні не зберігається"))
        self.label_8.setText(_translate("MainWindow", "Якщо ви втратите пароль або шифрування паролю, файл буде втраченим"))
        self.file_to_encrypt_password.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.label_6.setText(_translate("MainWindow", "Розшифрування файлу"))
        self.file_to_decrypt_path.setPlaceholderText(_translate("MainWindow", "Шлях до файлу"))
        self.chose_file_to_decrypt.setText(_translate("MainWindow", "Вибрати..."))
        self.decrypt_file_password.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.decrypt_file_password_algorithm.setItemText(0, _translate("MainWindow", "Нема"))
        self.decrypt_file_password_algorithm.setItemText(1, _translate("MainWindow", "Sha1"))
        self.decrypt_file_password_algorithm.setItemText(2, _translate("MainWindow", "Sha224"))
        self.decrypt_file_password_algorithm.setItemText(3, _translate("MainWindow", "Sha256"))
        self.decrypt_file_password_algorithm.setItemText(4, _translate("MainWindow", "Sha384"))
        self.decrypt_file_password_algorithm.setItemText(5, _translate("MainWindow", "Sha512"))
        self.decrypt_file_password_algorithm.setItemText(6, _translate("MainWindow", "md5"))
        self.label_9.setText(_translate("MainWindow", "Шифрування паролю"))
        self.decrypt_file.setText(_translate("MainWindow", "Розшифрувати"))
        self.label_10.setText(_translate("MainWindow", "За замовчюванням файл розшифровується з форматом .txt"))
        self.label_15.setText(_translate("MainWindow", "Шифрування з данними"))
        self.encrypt_with_data_string.setPlaceholderText(_translate("MainWindow", "Строка"))
        self.encrypt_with_data.setText(_translate("MainWindow", "Шифрувати"))
        self.encrypted_with_data_string.setPlaceholderText(_translate("MainWindow", "Зашифрована строка"))
        self.data_to_decrypt_encrypted.setPlaceholderText(_translate("MainWindow", "Данні для розшифрування"))
        self.copy_encrypted_string.setText(_translate("MainWindow", "Копіювати зашифровану строку"))
        self.copy_data_to_decrypt_string.setText(_translate("MainWindow", "Копіювати данні для розшифрування"))
        self.label_16.setText(_translate("MainWindow", "Розшифрування з данними"))
        self.encrypted_string_decrypt_data.setPlaceholderText(_translate("MainWindow", "Зашифрована строка"))
        self.data_to_decrypt_data.setPlaceholderText(_translate("MainWindow", "Данні для розшифрування"))
        self.decrypt_data.setText(_translate("MainWindow", "Розшифрувати"))
        self.decrypted_string.setPlaceholderText(_translate("MainWindow", "Розшифрована строка"))
        self.copy_decrypted_string.setText(_translate("MainWindow", "Скопіювати"))
        self.label_11.setText(_translate("MainWindow", "CryptoApp"))
        self.label_12.setText(_translate("MainWindow", "Версія 1.1.0"))
        self.label_13.setText(_translate("MainWindow", "App created by"))
