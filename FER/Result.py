

from PyQt5 import QtCore, QtGui, QtWidgets

from DBConnection import DBConnection
import re
import sys
class Ui_Result(object):


    def feedback(self,result,rname):

        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            if result == "happy":
                rating="3"
            elif result == "neutral":
                rating = "2"
            else:
                rating="1"

            if result == "neutral":
                self.label.setStyleSheet("image: url(../FER/images/neutral.png);")
            else:
             self.label.setStyleSheet("image: url(../FER/images/neutral_blur.png);")

            if result == "sad":
                 self.label_2.setStyleSheet("image: url(../FER/images/sad.png);")
            else:
                self.label_2.setStyleSheet("image: url(../FER/images/sad_blur.png);")

            if result == "happy":
                self.label_3.setStyleSheet("image: url(../FER/images/happy.png);")
            else:
                self.label_3.setStyleSheet("image: url(../FER/images/happy_blur.png);")

            sql = "insert into feedback values(%s,%s)"
            values = (rname, rating)
            cursor.execute(sql,values)
            database.commit()
            self.showMessageBox("Information", "Feedback is : "+str(result))

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(631, 545)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.camera = QtWidgets.QLabel(Dialog)
        self.camera.setGeometry(QtCore.QRect(160, 60, 291, 191))
        self.camera.setStyleSheet("image: url(../FER/images/capture.jpg);")
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 360, 91, 51))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 360, 91, 51))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(450, 360, 91, 51))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FeedBack Results"))
        self.label.setText(_translate("Dialog", ""))
        self.label_2.setText(_translate("Dialog", ""))
        self.label_3.setText(_translate("Dialog", ""))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
