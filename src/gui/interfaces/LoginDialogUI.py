# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginDialog.ui'
#
# Created: Sat Sep 29 21:06:02 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName(_fromUtf8("loginDialog"))
        loginDialog.resize(233, 127)
        loginDialog.setModal(True)
        self.loginEdit = QtGui.QLineEdit(loginDialog)
        self.loginEdit.setGeometry(QtCore.QRect(82, 20, 131, 20))
        self.loginEdit.setObjectName(_fromUtf8("loginEdit"))
        self.passwordEdit = QtGui.QLineEdit(loginDialog)
        self.passwordEdit.setGeometry(QtCore.QRect(82, 50, 131, 20))
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.loginLabel = QtGui.QLabel(loginDialog)
        self.loginLabel.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.loginLabel.setObjectName(_fromUtf8("loginLabel"))
        self.passwordLabel = QtGui.QLabel(loginDialog)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 50, 51, 20))
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.okButton = QtGui.QPushButton(loginDialog)
        self.okButton.setGeometry(QtCore.QRect(60, 90, 75, 23))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.cancelButton = QtGui.QPushButton(loginDialog)
        self.cancelButton.setGeometry(QtCore.QRect(140, 90, 75, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))

        self.retranslateUi(loginDialog)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle(QtGui.QApplication.translate("loginDialog", "User authentification", None, QtGui.QApplication.UnicodeUTF8))
        self.loginLabel.setText(QtGui.QApplication.translate("loginDialog", "Login:", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel.setText(QtGui.QApplication.translate("loginDialog", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("loginDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("loginDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

