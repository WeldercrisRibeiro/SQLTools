from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 485)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.query_entry = QtWidgets.QTextEdit(self.centralwidget)
        self.query_entry.setGeometry(QtCore.QRect(9, 112, 782, 101))
        self.query_entry.setStyleSheet("color: white;\n"
"background-color: rgb(0, 0, 0);\n"
"text-transform: uppercase;\n"
"font-weight: bold;\n"
"\n"
"/*font: 75 8pt \"Cascadia Code\";*/")
        self.query_entry.setObjectName("query_entry")
        
        self.result_text = QtWidgets.QTextEdit(self.centralwidget)
        self.result_text.setGeometry(QtCore.QRect(9, 262, 782, 151))
        self.result_text.setStyleSheet("color: white;\n"
"background-color: rgb(0, 0, 0);\n"
"text-transform: uppercase;\n"
"font-weight: bold;\n"
"")
        self.result_text.setReadOnly(True)
        self.result_text.setObjectName("result_text")


        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(620, 440, 151, 30))
        self.exit_button.setMinimumSize(QtCore.QSize(100, 30))
        self.exit_button.setStyleSheet("""#exit_button {
                                          background-color: white;
                                          color: black;
                                          text-transform: uppercase;
                                          font-weight: bold;
                                          border-radius: 10px
                                        }
                                        #exit_button:hover {
                                          background-color: blue;
                                          color: white;
                                             
                                        }
                                          
                                        #exit_button:pressed {
                                          background-color: aqua;
                                          color: white;
                                          }""")
        self.exit_button.setObjectName("exit_button")

        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(210, 440, 151, 30))
        self.clear_button.setMinimumSize(QtCore.QSize(100, 30))
        self.clear_button.setStyleSheet("""#clear_button {
                                          background-color: white;
                                          color: black;
                                          text-transform: uppercase;
                                          font-weight: bold;
                                          border-radius: 10px
                                        }
                                        #clear_button:hover {
                                          background-color: blue;
                                          color: white;
                                             
                                        }
                                          
                                        #clear_button:pressed {
                                          background-color: aqua;
                                          color: white;
                                          }""")
        self.clear_button.setObjectName("clear_button")


        self.config_button = QtWidgets.QPushButton(self.centralwidget)
        self.config_button.setGeometry(QtCore.QRect(410, 440, 151, 30))
        self.config_button.setMinimumSize(QtCore.QSize(100, 30))
        self.config_button.setStyleSheet("""#config_button {
                                          background-color: white;
                                          color: black;
                                          text-transform: uppercase;
                                          font-weight: bold;
                                          border-radius: 10px
                                        }
                                        #config_button:hover {
                                          background-color: blue;
                                          color: white;
                                             
                                        }
                                          
                                        #config_button:pressed {
                                          background-color: aqua;
                                          color: white;
                                          }""")
        self.config_button.setObjectName("config_button")

        #config botão executar F5
        self.execute_button = QtWidgets.QPushButton(self.centralwidget)
        self.execute_button.setGeometry(QtCore.QRect(20, 440, 151, 30))
        self.execute_button.setMinimumSize(QtCore.QSize(100, 30))
        self.execute_button.setStyleSheet("""
                                        #execute_button {
                                          background-color: white;
                                          color: black;
                                          text-transform: uppercase;
                                          font-weight: bold;
                                          border-radius: 10px
                                        }
                                        #execute_button:hover {
                                          background-color: blue;
                                          color: white;
                                             
                                        }
                                          
                                        #execute_button:pressed {
                                          background-color: aqua;
                                          color: white;
                                          }


                                          """)
        self.execute_button.setObjectName("execute_button")

        #titulo consulta da tela antes do input das consultas
        self.label_consulta = QtWidgets.QLabel(self.centralwidget)
        self.label_consulta.setGeometry(QtCore.QRect(10, 80, 781, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_consulta.setFont(font)
        self.label_consulta.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(0, 0, 0);\n"
                                             "\n"
                                             "text-transform: uppercase;\n"
                                             "font-weight: bold;\n"
                                                "")
        self.label_consulta.setObjectName("label_consulta")


        self.label_icomac = QtWidgets.QLabel(self.centralwidget)
        self.label_icomac.setGeometry(QtCore.QRect(730, 10, 51, 31))
        self.label_icomac.setText("")
        self.label_icomac.setPixmap(QtGui.QPixmap("src/img/mac.png"))
        self.label_icomac.setScaledContents(True)
        self.label_icomac.setObjectName("label_icomac")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(10, 230, 781, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_resultado.setFont(font)
        self.label_resultado.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"text-transform: uppercase;\n"
"font-weight: bold;\n"
"")
        self.label_resultado.setObjectName("label_resultado")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 161, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("src/img/sqltoolsLogo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.query_entry.raise_()
        self.result_text.raise_()
        self.exit_button.raise_()
        self.clear_button.raise_()
        self.config_button.raise_()
        self.execute_button.raise_()
        self.label_icomac.raise_()
        self.label_consulta.raise_()
        self.label_resultado.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SQLTools"))
        self.exit_button.setText(_translate("MainWindow", "Sair - F10"))
        self.clear_button.setText(_translate("MainWindow", "Limpar - F6"))
        self.config_button.setText(_translate("MainWindow", "Configuração - F7"))
        self.execute_button.setText(_translate("MainWindow", "Executar - F5"))
        self.label_consulta.setText(_translate("MainWindow", " Consulta:"))
        self.label_resultado.setText(_translate("MainWindow", "Resultado:"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
