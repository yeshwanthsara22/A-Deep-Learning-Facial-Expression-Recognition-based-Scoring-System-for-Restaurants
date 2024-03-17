

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from FaceExpRecog import Ui_FaceExpRecog
from Ratings import Ui_Ratings
class Ui_Main(object):

    def fer(self):
        try:
            self.fr = QtWidgets.QDialog()
            self.ui1 = Ui_FaceExpRecog()
            self.ui1.setupUi(self.fr)
            self.fr.show()

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def feedbk(self):
        try:
            self.fb = QtWidgets.QDialog()
            self.ui2 =  Ui_Ratings()
            self.ui2.setupUi(self.fb)
            self.ui2.score()
            self.fb.show()

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(646, 422)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 651, 431))
        self.label.setStyleSheet("image: url(../FER/images/fb.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 110, 261, 51))
        self.pushButton.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fer)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 230, 261, 51))
        self.pushButton_2.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.feedbk)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Facial Expression Recognition based Scoring System"))
        self.pushButton.setText(_translate("Dialog", "Facial Expression Recognition"))
        self.pushButton_2.setText(_translate("Dialog", "Feedback Scoring System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
