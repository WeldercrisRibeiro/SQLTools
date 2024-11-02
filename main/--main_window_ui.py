from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.query_entry = QtWidgets.QTextEdit(self.centralwidget)
        self.query_entry.setGeometry(QtCore.QRect(9, 9, 782, 154))
        self.query_entry.setStyleSheet("color: WHITE;\n""background-color: rgb(0, 0, 0);text-transform: uppercase;font-weight: bold;")
        self.query_entry.setObjectName("query_entry")
        self.result_text = QtWidgets.QTextEdit(self.centralwidget)
        self.result_text.setGeometry(QtCore.QRect(9, 198, 782, 155))
        self.result_text.setStyleSheet("color: green;\n""background-color: rgb(0, 0, 0);font-weight: bold;")
        self.result_text.setReadOnly(True)
        self.result_text.setObjectName("result_text")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(610, 360, 151, 30))
        self.exit_button.setMinimumSize(QtCore.QSize(100, 30))
        self.exit_button.setStyleSheet("background-color: red; color: white;")
        self.exit_button.setObjectName("exit_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(200, 360, 151, 30))
        self.clear_button.setMinimumSize(QtCore.QSize(100, 30))
        self.clear_button.setStyleSheet("background-color: yellow; color: black;")
        self.clear_button.setObjectName("clear_button")
        self.config_button = QtWidgets.QPushButton(self.centralwidget)
        self.config_button.setGeometry(QtCore.QRect(400, 360, 151, 30))
        self.config_button.setMinimumSize(QtCore.QSize(100, 30))
        self.config_button.setStyleSheet("background-color: blue; color: white;")
        self.config_button.setObjectName("config_button")
        self.execute_button = QtWidgets.QPushButton(self.centralwidget)
        self.execute_button.setGeometry(QtCore.QRect(10, 360, 151, 30))
        self.execute_button.setMinimumSize(QtCore.QSize(100, 30))
        self.execute_button.setStyleSheet("background-color: green; color: white;")
        self.execute_button.setObjectName("execute_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SQL Terminal"))
        self.exit_button.setText(_translate("MainWindow", "Sair - F10"))
        self.clear_button.setText(_translate("MainWindow", "Limpar - F6"))
        self.config_button.setText(_translate("MainWindow", "Configuração - F7"))
        self.execute_button.setText(_translate("MainWindow", "Executar - F5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
