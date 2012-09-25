# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InsertNewDialogUI.ui'
#
# Created: Sat Sep 29 23:48:20 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_InsertNewDialog(object):
    def setupUi(self, InsertNewDialog):
        InsertNewDialog.setObjectName(_fromUtf8("InsertNewDialog"))
        InsertNewDialog.resize(292, 295)
        InsertNewDialog.setModal(False)
        self.okButton = QtGui.QPushButton(InsertNewDialog)
        self.okButton.setGeometry(QtCore.QRect(130, 260, 75, 23))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.cancelButton = QtGui.QPushButton(InsertNewDialog)
        self.cancelButton.setGeometry(QtCore.QRect(210, 260, 75, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.scrollArea = QtGui.QScrollArea(InsertNewDialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 271, 241))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 269, 239))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(InsertNewDialog)
        QtCore.QMetaObject.connectSlotsByName(InsertNewDialog)

    def retranslateUi(self, InsertNewDialog):
        InsertNewDialog.setWindowTitle(QtGui.QApplication.translate("InsertNewDialog", "Insert new...", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("InsertNewDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("InsertNewDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

