# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textAddDialog.ui'
#
# Created: Wed Jun  3 08:30:58 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(305, 233)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textLineEdit = QtGui.QLineEdit(Dialog)
        self.textLineEdit.setObjectName("textLineEdit")
        self.horizontalLayout.addWidget(self.textLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(61, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.sizeLineEdit = QtGui.QLineEdit(Dialog)
        self.sizeLineEdit.setObjectName("sizeLineEdit")
        self.horizontalLayout_2.addWidget(self.sizeLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.doubleSpinBox_rotation = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_rotation.setDecimals(1)
        self.doubleSpinBox_rotation.setMinimum(-360.0)
        self.doubleSpinBox_rotation.setMaximum(360.0)
        self.doubleSpinBox_rotation.setSingleStep(15.0)
        self.doubleSpinBox_rotation.setObjectName("doubleSpinBox_rotation")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_rotation)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.colorLineEdit = QtGui.QLineEdit(Dialog)
        self.colorLineEdit.setObjectName("colorLineEdit")
        self.horizontalLayout_4.addWidget(self.colorLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.familyLineEdit = QtGui.QLineEdit(Dialog)
        self.familyLineEdit.setObjectName("familyLineEdit")
        self.horizontalLayout_5.addWidget(self.familyLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.placeButton = QtGui.QPushButton(Dialog)
        self.placeButton.setObjectName("placeButton")
        self.verticalLayout.addWidget(self.placeButton)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.placeButton, QtCore.SIGNAL("released()"), Dialog.accept)
        QtCore.QObject.connect(self.textLineEdit, QtCore.SIGNAL("returnPressed()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Add Text", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Text", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Font-size", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeLineEdit.setText(QtGui.QApplication.translate("Dialog", "4pt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Rotation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "°", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.colorLineEdit.setText(QtGui.QApplication.translate("Dialog", "rgb(255,0,0)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Family", None, QtGui.QApplication.UnicodeUTF8))
        self.familyLineEdit.setText(QtGui.QApplication.translate("Dialog", "Verdana", None, QtGui.QApplication.UnicodeUTF8))
        self.placeButton.setText(QtGui.QApplication.translate("Dialog", "Place Text", None, QtGui.QApplication.UnicodeUTF8))

