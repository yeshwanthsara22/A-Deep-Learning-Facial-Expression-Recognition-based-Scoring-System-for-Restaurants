
from PyQt5 import QtCore, QtGui, QtWidgets
from Camera import Ui_Camera

class Ui_FaceExpRecog(object):
    def __init__(self):
        self.foodlist = []
        self.foodlist.clear()

    def addItems(self):
        self.rname = self.comboBox_2.currentText();
        food = self.comboBox.currentText();
        self.foodlist.append(food)
        print(self.foodlist)

    def submit(self):
        try:
            self.cm = QtWidgets.QDialog()
            self.ui1 = Ui_Camera(self.foodlist,self.rname)
            self.ui1.setupUi(self.cm)
            self.cm.show()

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(784, 464)
        Dialog.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 731, 71))
        self.label.setStyleSheet("font: 16pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 240, 151, 41))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Garamond\";")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(280, 240, 221, 51))
        self.comboBox.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 330, 91, 31))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addItems)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 330, 101, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.submit)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 140, 151, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Garamond\";")
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 140, 221, 51))
        self.comboBox_2.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Facial Expression Recognition based Scoring System for Restaurants"))
        self.label_2.setText(_translate("Dialog", "Select Food Items"))
        self.comboBox.setItemText(0, _translate("Dialog", "Biryani"))
        self.comboBox.setItemText(1, _translate("Dialog", "VegBiryani"))
        self.comboBox.setItemText(2, _translate("Dialog", "Chicken Drumsticks"))
        self.comboBox.setItemText(3, _translate("Dialog", "Tandoori Chicken"))
        self.pushButton.setText(_translate("Dialog", "Add"))
        self.pushButton_2.setText(_translate("Dialog", "Submit"))
        self.label_3.setText(_translate("Dialog", "Select Restaurant"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Almas"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Spicy"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Rayalaseema Ruchulu"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Paradise"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
