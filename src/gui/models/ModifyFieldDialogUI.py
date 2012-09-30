# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifyFieldDialogUI.ui'
#
# Created: Sun Sep 30 17:01:59 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(228, 102)
        self.okButton = QtGui.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(60, 60, 75, 23))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.valueEdit = QtGui.QLineEdit(Dialog)
        self.valueEdit.setGeometry(QtCore.QRect(10, 30, 201, 20))
        self.valueEdit.setObjectName(_fromUtf8("valueEdit"))
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(140, 60, 75, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Modifying field...", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "New value:", None, QtGui.QApplication.UnicodeUTF8))

