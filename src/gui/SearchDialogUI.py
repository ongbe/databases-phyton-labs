# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchDialogUI.ui'
#
# Created: Sat Sep 29 23:49:17 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SearchDialog(object):
    def setupUi(self, SearchDialog):
        SearchDialog.setObjectName(_fromUtf8("SearchDialog"))
        SearchDialog.resize(296, 117)
        SearchDialog.setModal(False)
        self.keyEdit = QtGui.QLineEdit(SearchDialog)
        self.keyEdit.setGeometry(QtCore.QRect(80, 50, 201, 20))
        self.keyEdit.setObjectName(_fromUtf8("keyEdit"))
        self.pushButton = QtGui.QPushButton(SearchDialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 80, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.keyLabel = QtGui.QLabel(SearchDialog)
        self.keyLabel.setGeometry(QtCore.QRect(10, 50, 61, 20))
        self.keyLabel.setObjectName(_fromUtf8("keyLabel"))
        self.keyColumnCombo = QtGui.QComboBox(SearchDialog)
        self.keyColumnCombo.setGeometry(QtCore.QRect(80, 20, 201, 22))
        self.keyColumnCombo.setObjectName(_fromUtf8("keyColumnCombo"))
        self.columnLabel = QtGui.QLabel(SearchDialog)
        self.columnLabel.setGeometry(QtCore.QRect(10, 20, 46, 20))
        self.columnLabel.setObjectName(_fromUtf8("columnLabel"))

        self.retranslateUi(SearchDialog)
        QtCore.QMetaObject.connectSlotsByName(SearchDialog)

    def retranslateUi(self, SearchDialog):
        SearchDialog.setWindowTitle(QtGui.QApplication.translate("SearchDialog", "Search for...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("SearchDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.keyLabel.setText(QtGui.QApplication.translate("SearchDialog", "Search key:", None, QtGui.QApplication.UnicodeUTF8))
        self.columnLabel.setText(QtGui.QApplication.translate("SearchDialog", "Column:", None, QtGui.QApplication.UnicodeUTF8))

