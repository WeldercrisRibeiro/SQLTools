# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_config_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ServerConfigDialog(object):
    def setupUi(self, ServerConfigDialog):
        ServerConfigDialog.setObjectName("ServerConfigDialog")
        ServerConfigDialog.resize(278, 167)
        self.verticalLayout = QtWidgets.QVBoxLayout(ServerConfigDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayoutWidget = QtWidgets.QWidget(ServerConfigDialog)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)

        self.formLayout.setObjectName("formLayout")
        self.labelServer = QtWidgets.QLabel(self.formLayoutWidget)


        self.labelServer.setObjectName("labelServer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelServer)
        self.server_entry = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.server_entry.setStyleSheet("color:white;font-weight: bold;")

        self.server_entry.setObjectName("server_entry")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.server_entry)
        self.labelDatabase = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelDatabase.setStyleSheet("font-weight: bold;color:black;")

        self.labelDatabase.setObjectName("labelDatabase")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelDatabase)
        self.database_entry = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.database_entry.setStyleSheet("color: white;font-weight: bold;")

        self.database_entry.setObjectName("database_entry")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.database_entry)
        self.labelUsername = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelUsername.setStyleSheet("color: black;font-weight: bold;")

        self.labelUsername.setObjectName("labelUsername")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelUsername)
        self.username_entry = QtWidgets.QLineEdit(self.formLayoutWidget)

        self.username_entry.setObjectName("username_entry")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.username_entry)
        self.labelPassword = QtWidgets.QLabel(self.formLayoutWidget)

        self.labelPassword.setObjectName("labelPassword")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelPassword)
        self.password_entry = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.Password)

        self.password_entry.setObjectName("password_entry")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.password_entry)
        self.verticalLayout.addWidget(self.formLayoutWidget)
        self.save_button = QtWidgets.QPushButton(ServerConfigDialog)
        self.save_button.setObjectName("save_button")
        self.verticalLayout.addWidget(self.save_button)

        self.retranslateUi(ServerConfigDialog)
        QtCore.QMetaObject.connectSlotsByName(ServerConfigDialog)

    def retranslateUi(self, ServerConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        ServerConfigDialog.setWindowTitle(_translate("ServerConfigDialog", "Configuração do Servidor"))
        self.labelServer.setText(_translate("ServerConfigDialog", "Servidor:"))
        self.labelDatabase.setText(_translate("ServerConfigDialog", "Banco de Dados:"))
        self.labelUsername.setText(_translate("ServerConfigDialog", "Usuário:"))
        self.labelPassword.setText(_translate("ServerConfigDialog", "Senha:"))
        self.save_button.setText(_translate("ServerConfigDialog", "Salvar Configurações"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ServerConfigDialog = QtWidgets.QDialog()
    ui = Ui_ServerConfigDialog()
    ui.setupUi(ServerConfigDialog)
    ServerConfigDialog.show()
    sys.exit(app.exec_())