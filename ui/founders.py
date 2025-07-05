

from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_founders(object):
    def setupUi(self, founders):
        founders.setObjectName("founders")
        founders.resize(1020, 700)
        founders.setMaximumSize(QtCore.QSize(1020, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.get_image_path("founders_logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        founders.setWindowIcon(icon)
        founders.setStyleSheet("background-color: rgb(0, 37, 64);")

        self.label = QtWidgets.QLabel(founders)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 98))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(founders)
        self.label_2.setGeometry(QtCore.QRect(18, 130, 984, 440))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(founders)
        self.label_3.setGeometry(QtCore.QRect(80, 591, 876, 87))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(founders)
        self.label_4.setGeometry(QtCore.QRect(324, 42, 372, 48))
        self.label_4.setObjectName("label_4")

        # Add back button like in the first version
        self.back_btn = QtWidgets.QPushButton(founders)
        self.back_btn.setGeometry(QtCore.QRect(880, 10, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                    "border-radius: 11px;")
        self.back_btn.setObjectName("back_btn")

        self.retranslateUi(founders)
        QtCore.QMetaObject.connectSlotsByName(founders)

    def get_image_path(self, filename):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, "img", filename)

    def retranslateUi(self, founders):
        _translate = QtCore.QCoreApplication.translate
        founders.setWindowTitle(_translate("founders", "დამფუძნებლები"))

        # Use setPixmap instead of HTML with resource paths
        self.label.setPixmap(QtGui.QPixmap(self.get_image_path("founders_logo.png")))
        self.label_2.setPixmap(QtGui.QPixmap(self.get_image_path("founders.png")))
        self.label_3.setPixmap(QtGui.QPixmap(self.get_image_path("foundres_txt.png")))
        self.label_4.setPixmap(QtGui.QPixmap(self.get_image_path("title_founders.png")))

        self.back_btn.setText(_translate("founders", "უკან"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    founders = QtWidgets.QDialog()
    ui = Ui_founders()
    ui.setupUi(founders)
    founders.show()
    sys.exit(app.exec_())