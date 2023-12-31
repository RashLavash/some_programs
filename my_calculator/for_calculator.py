# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(309, 415)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(151, 161, 168);\n"
"color: rgb(255, 255, 255);")
        self.label_result.setObjectName("label_result")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(0, 320, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.button_0.setFont(font)
        self.button_0.setStyleSheet("background-color: rgb(104, 184, 111);")
        self.button_0.setObjectName("button_0")
        self.button_equals = QtWidgets.QPushButton(self.centralwidget)
        self.button_equals.setGeometry(QtCore.QRect(120, 320, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.button_equals.setFont(font)
        self.button_equals.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.button_equals.setObjectName("button_equals")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(0, 50, 81, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_7.setFont(font)
        self.button_7.setStyleSheet("background-color: rgb(156, 255, 248);\n"
"")
        self.button_7.setObjectName("button_7")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(80, 50, 81, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_8.setFont(font)
        self.button_8.setStyleSheet("background-color: rgb(156, 255, 248);\n"
"")
        self.button_8.setObjectName("button_8")
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(160, 50, 81, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_9.setFont(font)
        self.button_9.setStyleSheet("background-color: rgb(156, 255, 248);")
        self.button_9.setObjectName("button_9")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(0, 140, 81, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_4.setFont(font)
        self.button_4.setStyleSheet("background-color: rgb(156, 255, 248);")
        self.button_4.setObjectName("button_4")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(80, 140, 81, 91))
        self.button_5.setStyleSheet("background-color: rgb(156, 255, 248);")
        self.button_5.setObjectName("button_5")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(160, 140, 81, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_6.setFont(font)
        self.button_6.setStyleSheet("background-color: rgb(156, 255, 248);")
        self.button_6.setObjectName("button_6")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(0, 230, 81, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_1.setFont(font)
        self.button_1.setStyleSheet("background-color: rgb(156, 255, 248);")
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(80, 230, 81, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_2.setFont(font)
        self.button_2.setStyleSheet("background-color: rgb(156, 255, 248);")
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(160, 230, 81, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_3.setFont(font)
        self.button_3.setStyleSheet("background-color: rgb(156, 255, 248);")
        self.button_3.setObjectName("button_3")
        self.button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.button_plus.setGeometry(QtCore.QRect(240, 50, 61, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_plus.setFont(font)
        self.button_plus.setStyleSheet("background-color: rgb(156, 255, 248);")
        self.button_plus.setObjectName("button_plus")
        self.button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.button_minus.setGeometry(QtCore.QRect(240, 140, 61, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_minus.setFont(font)
        self.button_minus.setStyleSheet("background-color: rgb(156, 255, 248);")
        self.button_minus.setObjectName("button_minus")
        self.button_mult = QtWidgets.QPushButton(self.centralwidget)
        self.button_mult.setGeometry(QtCore.QRect(240, 230, 61, 91))
        self.button_mult.setStyleSheet("background-color: rgb(156, 255, 248);")
        self.button_mult.setObjectName("button_mult")
        self.button_division = QtWidgets.QPushButton(self.centralwidget)
        self.button_division.setGeometry(QtCore.QRect(240, 320, 61, 81))
        self.button_division.setStyleSheet("background-color: rgb(156, 255, 248);")
        self.button_division.setObjectName("button_division")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

        self.is_equal = False


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_equals.setText(_translate("MainWindow", "="))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_mult.setText(_translate("MainWindow", "*"))
        self.button_division.setText(_translate("MainWindow", "/"))

    def add_function(self):
        # Обращаемся к кнопкам, обрабатываем их на "клик", и в conntct указываем
        # через lambda, какой метод и какой кнопке будем передавать
        self.button_0.clicked.connect(lambda: self.write_number(self.button_0.text()))
        self.button_1.clicked.connect(lambda: self.write_number(self.button_1.text()))
        self.button_2.clicked.connect(lambda: self.write_number(self.button_2.text()))
        self.button_3.clicked.connect(lambda: self.write_number(self.button_3.text()))
        self.button_4.clicked.connect(lambda: self.write_number(self.button_4.text()))
        self.button_5.clicked.connect(lambda: self.write_number(self.button_5.text()))
        self.button_6.clicked.connect(lambda: self.write_number(self.button_6.text()))
        self.button_7.clicked.connect(lambda: self.write_number(self.button_7.text()))
        self.button_8.clicked.connect(lambda: self.write_number(self.button_8.text()))
        self.button_9.clicked.connect(lambda: self.write_number(self.button_9.text()))
        self.button_plus.clicked.connect(lambda: self.write_number(self.button_plus.text()))
        self.button_minus.clicked.connect(lambda: self.write_number(self.button_minus.text()))
        self.button_mult.clicked.connect(lambda: self.write_number(self.button_mult.text()))
        self.button_division.clicked.connect(lambda: self.write_number(self.button_division.text()))

        self.button_equals.clicked.connect(self.results)

    def write_number(self, number):
        if self.label_result.text() == '0' or self.is_equal:
            self.label_result.setText(number)
            self.is_equal = False
        else:
            self.label_result.setText(self.label_result.text() + number)
    
    def results(self):
        res = eval(self.label_result.text())
        self.label_result.setText('Результат: ' + str(res))
        self.is_equal = True





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
