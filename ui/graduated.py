


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys


class Ui_graduate_window(object):
    def setupUi(self, graduate_window):
        graduate_window.setObjectName("graduate_window")
        graduate_window.resize(1020, 700)
        graduate_window.setMaximumSize(QtCore.QSize(1020, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.get_image_path("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        graduate_window.setWindowIcon(icon)
        graduate_window.setStyleSheet("background-color: rgb(0, 37, 64);")

        self.label = QtWidgets.QLabel(graduate_window)
        self.label.setGeometry(QtCore.QRect(0, 0, 1020, 181))
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap(self.get_image_path("graduated.png")))
        self.label.setScaledContents(True)

        self.label_2 = QtWidgets.QLabel(graduate_window)
        self.label_2.setGeometry(QtCore.QRect(300, 30, 431, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(239, 170, 79);\n"
                                   "")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")

        self.raodenoba_stud = QtWidgets.QLabel(graduate_window)
        self.raodenoba_stud.setGeometry(QtCore.QRect(290, 147, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.raodenoba_stud.setFont(font)
        self.raodenoba_stud.setStyleSheet("background-color: none;\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "")
        self.raodenoba_stud.setAlignment(QtCore.Qt.AlignCenter)
        self.raodenoba_stud.setIndent(0)
        self.raodenoba_stud.setObjectName("raodenoba_stud")

        self.label_4 = QtWidgets.QLabel(graduate_window)
        self.label_4.setGeometry(QtCore.QRect(780, 50, 229, 344))
        self.label_4.setStyleSheet("background-color: none;")
        self.label_4.setObjectName("label_4")
        self.label_4.setPixmap(QtGui.QPixmap(self.get_image_path("hah.png")))
        self.label_4.setScaledContents(True)

        self.back_btn = QtWidgets.QPushButton(graduate_window)
        self.back_btn.setGeometry(QtCore.QRect(20, 160, 108, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.back_btn.setFont(font)
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn.setStyleSheet("color: rgb(223, 220, 214);\n"
                                    "background-color: rgb(239, 170, 79);\n"
                                    "border-radius:10px;\n"
                                    "border-color: rgb(223, 220, 214);")
        self.back_btn.setObjectName("back_btn")

        self.label_3 = QtWidgets.QLabel(graduate_window)
        self.label_3.setGeometry(QtCore.QRect(240, 210, 541, 57))
        self.label_3.setObjectName("label_3")
        self.label_3.setPixmap(QtGui.QPixmap(self.get_image_path("Rectangle 4.png")))
        self.label_3.setScaledContents(True)

        self.label_5 = QtWidgets.QLabel(graduate_window)
        self.label_5.setGeometry(QtCore.QRect(275, 224, 489, 29))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: none;\n"
                                   "color: rgb(185, 99, 36);")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(graduate_window)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 1001, 390))
        self.label_6.setObjectName("label_6")
        self.label_6.setPixmap(QtGui.QPixmap(self.get_image_path("gela.png")))
        self.label_6.setScaledContents(True)

        self.retranslateUi(graduate_window)
        QtCore.QMetaObject.connectSlotsByName(graduate_window)

    def get_image_path(self, filename):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, "img", filename)

    def retranslateUi(self, graduate_window):
        _translate = QtCore.QCoreApplication.translate
        graduate_window.setWindowTitle(_translate("graduate_window", "კურსდამთავრებულები"))
        self.label_2.setText(_translate("graduate_window", "“მთავარია კაცობაში არ\nჩაიჭრა თორე უმაღლესის ...”"))
        self.raodenoba_stud.setText(_translate("graduate_window", " დაამთავრა 286927 სტუდენტმა."))
        self.back_btn.setText(_translate("graduate_window", "უკან"))
        self.label_5.setText(_translate("graduate_window", "წარჩინებული სტუდენტები"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    graduate_window = QtWidgets.QDialog()
    ui = Ui_graduate_window()
    ui.setupUi(graduate_window)
    graduate_window.show()
    sys.exit(app.exec_())