# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_management.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserManagementDialog(object):
    def setupUi(self, UserManagementDialog):
        UserManagementDialog.setObjectName("UserManagementDialog")
        UserManagementDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(UserManagementDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.userListWidget = QtWidgets.QListWidget(UserManagementDialog)
        self.userListWidget.setObjectName("userListWidget")
        self.verticalLayout.addWidget(self.userListWidget)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.labelUsername = QtWidgets.QLabel(UserManagementDialog)
        self.labelUsername.setObjectName("labelUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelUsername)
        self.lineEditUsername = QtWidgets.QLineEdit(UserManagementDialog)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditUsername)
        self.labelPassword = QtWidgets.QLabel(UserManagementDialog)
        self.labelPassword.setObjectName("labelPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(UserManagementDialog)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditPassword)
        self.checkBoxSelect = QtWidgets.QCheckBox(UserManagementDialog)
        self.checkBoxSelect.setObjectName("checkBoxSelect")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkBoxSelect)
        self.checkBoxUpdate = QtWidgets.QCheckBox(UserManagementDialog)
        self.checkBoxUpdate.setObjectName("checkBoxUpdate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBoxUpdate)
        self.checkBoxDelete = QtWidgets.QCheckBox(UserManagementDialog)
        self.checkBoxDelete.setObjectName("checkBoxDelete")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.checkBoxDelete)
        self.checkBoxInsert = QtWidgets.QCheckBox(UserManagementDialog)
        self.checkBoxInsert.setObjectName("checkBoxInsert")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.checkBoxInsert)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addUserButton = QtWidgets.QPushButton(UserManagementDialog)
        self.addUserButton.setObjectName("addUserButton")
        self.horizontalLayout.addWidget(self.addUserButton)
        self.saveUserButton = QtWidgets.QPushButton(UserManagementDialog)
        self.saveUserButton.setObjectName("saveUserButton")
        self.horizontalLayout.addWidget(self.saveUserButton)
        self.deleteUserButton = QtWidgets.QPushButton(UserManagementDialog)
        self.deleteUserButton.setObjectName("deleteUserButton")
        self.horizontalLayout.addWidget(self.deleteUserButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(UserManagementDialog)
        QtCore.QMetaObject.connectSlotsByName(UserManagementDialog)

    def retranslateUi(self, UserManagementDialog):
        _translate = QtCore.QCoreApplication.translate
        UserManagementDialog.setWindowTitle(_translate("UserManagementDialog", "Gerenciamento de Usuários"))
        self.labelUsername.setText(_translate("UserManagementDialog", "Usuário:"))
        self.labelPassword.setText(_translate("UserManagementDialog", "Senha:"))
        self.checkBoxSelect.setText(_translate("UserManagementDialog", "Permitir SELECT"))
        self.checkBoxUpdate.setText(_translate("UserManagementDialog", "Permitir UPDATE"))
        self.checkBoxDelete.setText(_translate("UserManagementDialog", "Permitir DELETE"))
        self.checkBoxInsert.setText(_translate("UserManagementDialog", "Permitir INSERT"))
        self.addUserButton.setText(_translate("UserManagementDialog", "Adicionar Usuário"))
        self.saveUserButton.setText(_translate("UserManagementDialog", "Salvar Alterações"))
        self.deleteUserButton.setText(_translate("UserManagementDialog", "Excluir Usuário"))