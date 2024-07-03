from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 683)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/my_ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background: #aff57a;\n"
                                 "background: linear-gradient(0deg,#aff57a 4%, #54d169 80%);\n"
                                 "background: -webkit-linear-gradient(0deg,#aff57a 4%, #54d169 80%);\n"
                                 "background: -moz-linear-gradient(0deg,#aff57a 4%, #54d169 80%);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("color: #000")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0.506, y1:1, x2:0.352, y2:0.108, stop:0 rgba(144, 214, 190, 255), stop:0.414773 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 255))")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header_frame = QtWidgets.QFrame(self.widget)
        self.header_frame.setMaximumSize(QtCore.QSize(16777215, 112))
        self.header_frame.setStyleSheet("border-bottom-right-radius: 70px;\n"
                                        "border-bottom-left-radius: 70px;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.506, y1:1, x2:0.352, y2:0.108, stop:0 rgba(255, 255, 255, 255), stop:0.414773 rgba(255, 255, 255, 50), stop:1 rgba(144, 214, 190, 255));\n"
                                        "\n"
                                        "")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.header_frame)
        self.verticalLayout_3.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.header_frame)
        self.frame_5.setMaximumSize(QtCore.QSize(80, 26))
        self.frame_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_5.setStyleSheet("QFrame{background: none;}\n"
                                   "QPushButton{\n"
                                   "border-radius: 5px;\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "padding: 5px;\n"
                                   "}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(0, 0, 7, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.close_window_button = QtWidgets.QPushButton(self.frame_5)
        self.close_window_button.setMinimumSize(QtCore.QSize(25, 25))
        self.close_window_button.setMaximumSize(QtCore.QSize(25, 25))
        self.close_window_button.setStyleSheet("background: none;\n"
                                               "border-image: url(:/icons/icons/close.ico);")
        self.close_window_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/close.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_window_button.setIcon(icon1)
        self.close_window_button.setIconSize(QtCore.QSize(25, 25))
        self.close_window_button.setObjectName("close_window_button")
        self.horizontalLayout.addWidget(self.close_window_button)
        self.minimize_window_button = QtWidgets.QPushButton(self.frame_5)
        self.minimize_window_button.setMinimumSize(QtCore.QSize(25, 25))
        self.minimize_window_button.setMaximumSize(QtCore.QSize(25, 25))
        self.minimize_window_button.setStyleSheet("background: none;\n"
                                                  "border-image: url(:/icons/icons/collapse.ico);")
        self.minimize_window_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/collapse.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_window_button.setIcon(icon2)
        self.minimize_window_button.setIconSize(QtCore.QSize(25, 25))
        self.minimize_window_button.setObjectName("minimize_window_button")
        self.horizontalLayout.addWidget(self.minimize_window_button)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame = QtWidgets.QFrame(self.header_frame)
        self.frame.setMinimumSize(QtCore.QSize(0, 36))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 87))
        self.frame.setStyleSheet("background: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setMinimumSize(QtCore.QSize(178, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(52, 16777215))
        self.frame_6.setStyleSheet("QFrame{\n"
                                   "border-bottom-right-radius: 30px;\n"
                                   "border-bottom-left-radius: 30px;\n"
                                   "border-top-right-radius: 30px;\n"
                                   "border-top-left-radius: 30px;\n"
                                   "border-bottom: 2px  dashed #22222e;\n"
                                   "border-top: 2px  dashed #22222e;\n"
                                   "}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_chat = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_chat.setFont(font)
        self.label_chat.setStyleSheet("color: #5a5a5a;\n"
                                      "border: none;")
        self.label_chat.setAlignment(QtCore.Qt.AlignCenter)
        self.label_chat.setObjectName("label_chat")
        self.verticalLayout_4.addWidget(self.label_chat, 0, QtCore.Qt.AlignTop)
        self.label_model = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_model.setFont(font)
        self.label_model.setStyleSheet("color: #5a5a5a;\n"
                                       "border: none;")
        self.label_model.setAlignment(QtCore.Qt.AlignCenter)
        self.label_model.setObjectName("label_model")
        self.verticalLayout_4.addWidget(self.label_model)
        self.horizontalLayout_3.addWidget(self.frame_6)
        spacerItem1 = QtWidgets.QSpacerItem(359, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.header_frame)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setStyleSheet("background:none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2_output_text = QtWidgets.QTextBrowser(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2_output_text.setFont(font)
        self.label_2_output_text.setStyleSheet("QTextBrowser {\n"
                                               "    border:none;\n"
                                               "    color: #22222e;\n"
                                               "    padding: 7px;\n"
                                               "    background-color: rgba(255, 255, 255, 0);    \n"
                                               "}")
        self.label_2_output_text.setObjectName("label_2_output_text")
        self.verticalLayout_5.addWidget(self.label_2_output_text)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 74))
        self.frame_3.setStyleSheet("background: none;\n"
                                   "")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setMaximumSize(QtCore.QSize(72, 45))
        self.frame_7.setStyleSheet("")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.speaker_button = QtWidgets.QPushButton(self.frame_7)
        self.speaker_button.setMaximumSize(QtCore.QSize(25, 25))
        self.speaker_button.setStyleSheet("border: none;\n"
                                          "border-image: url(:/icons/icons/speaker.ico);")
        self.speaker_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/speaker.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speaker_button.setIcon(icon3)
        self.speaker_button.setIconSize(QtCore.QSize(25, 25))
        self.speaker_button.setObjectName("speaker_button")
        self.horizontalLayout_4.addWidget(self.speaker_button)
        self.keyboard_button = QtWidgets.QPushButton(self.frame_7)
        self.keyboard_button.setMaximumSize(QtCore.QSize(25, 25))
        self.keyboard_button.setStyleSheet("border: none;\n"
                                           "border-image: url(:/icons/icons/keyboard.ico);")
        self.keyboard_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/keyboard.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.keyboard_button.setIcon(icon4)
        self.keyboard_button.setIconSize(QtCore.QSize(25, 25))
        self.keyboard_button.setObjectName("keyboard_button")
        self.horizontalLayout_4.addWidget(self.keyboard_button)
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.lineEdit_question = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_question.setMaximumSize(QtCore.QSize(16777215, 57))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_question.setFont(font)
        self.lineEdit_question.setStyleSheet("QLineEdit {\n"
                                             "    border: none;\n"
                                             "    border-bottom: 1px solid transparent;    \n"
                                             "    background:none;\n"
                                             "    border-bottom-left-radius: 10px;\n"
                                             "    border-bottom-right-radius: 10px;\n"
                                             "    border: 2px dashed #4ac497;\n"
                                             "    background-color: #d8ebe5;\n"
                                             "    padding-left: 10px;\n"
                                             "}\n"
                                             "")
        self.lineEdit_question.setObjectName("lineEdit_question")
        self.horizontalLayout_5.addWidget(self.lineEdit_question)
        self.question_button = QtWidgets.QPushButton(self.frame_3)
        self.question_button.setStyleSheet("QPushButton {    \n"
                                           "    border-image: url(:/icons/icons/play.ico);\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton {\n"
                                           "    cursor: pointing-hand;\n"
                                           "}")
        self.question_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/play.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.question_button.setIcon(icon5)
        self.question_button.setIconSize(QtCore.QSize(36, 36))
        self.question_button.setObjectName("question_button")
        self.horizontalLayout_5.addWidget(self.question_button)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.widget)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 36))
        self.frame_4.setStyleSheet("background: none;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_my_name = QtWidgets.QLabel(self.frame_4)
        self.label_my_name.setEnabled(True)
        self.label_my_name.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(10)
        self.label_my_name.setFont(font)
        self.label_my_name.setMouseTracking(False)
        self.label_my_name.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_my_name.setWhatsThis("")
        self.label_my_name.setStyleSheet("color: #5a5a5a;")
        self.label_my_name.setText("by Victor Krupeichenko Ⓒ 2024")
        self.label_my_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_my_name.setObjectName("label_my_name")
        self.horizontalLayout_2.addWidget(self.label_my_name)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GPT CHAT"))
        self.label_chat.setText(_translate("MainWindow", "GPT CHAT"))
        self.label_model.setText(_translate("MainWindow", "model: gpt 3.5-turbo"))
        self.lineEdit_question.setPlaceholderText(_translate("MainWindow", "Введите запрос..."))


import gpt_qrc_rc
