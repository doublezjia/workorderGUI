# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WorkorderGUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import workorderQRC_rc

class Ui_workorderForm(object):
    def setupUi(self, workorderForm):
        if not workorderForm.objectName():
            workorderForm.setObjectName(u"workorderForm")
        workorderForm.setWindowModality(Qt.NonModal)
        workorderForm.resize(630, 517)
        workorderForm.setMinimumSize(QSize(0, 0))
        workorderForm.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u"lion.ico", QSize(), QIcon.Normal, QIcon.Off)
        workorderForm.setWindowIcon(icon)
        self.layoutWidget = QWidget(workorderForm)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 581, 451))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.subjectLabel = QLabel(self.layoutWidget)
        self.subjectLabel.setObjectName(u"subjectLabel")

        self.gridLayout.addWidget(self.subjectLabel, 6, 0, 1, 1)

        self.partselectComboBox = QComboBox(self.layoutWidget)
        self.partselectComboBox.setObjectName(u"partselectComboBox")

        self.gridLayout.addWidget(self.partselectComboBox, 0, 4, 1, 1)

        self.handleComboBox = QComboBox(self.layoutWidget)
        self.handleComboBox.addItem("")
        self.handleComboBox.addItem("")
        self.handleComboBox.setObjectName(u"handleComboBox")

        self.gridLayout.addWidget(self.handleComboBox, 3, 4, 1, 1)

        self.datasourceComboBox = QComboBox(self.layoutWidget)
        self.datasourceComboBox.addItem("")
        self.datasourceComboBox.addItem("")
        self.datasourceComboBox.setObjectName(u"datasourceComboBox")

        self.gridLayout.addWidget(self.datasourceComboBox, 2, 1, 1, 1)

        self.enameLabel = QLabel(self.layoutWidget)
        self.enameLabel.setObjectName(u"enameLabel")

        self.gridLayout.addWidget(self.enameLabel, 1, 3, 1, 1)

        self.emailLineEdit = QLineEdit(self.layoutWidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.gridLayout.addWidget(self.emailLineEdit, 5, 1, 1, 1)

        self.evennumberSpinBox = QSpinBox(self.layoutWidget)
        self.evennumberSpinBox.setObjectName(u"evennumberSpinBox")
        self.evennumberSpinBox.setValue(1)

        self.gridLayout.addWidget(self.evennumberSpinBox, 4, 4, 1, 1)

        self.handleLabel = QLabel(self.layoutWidget)
        self.handleLabel.setObjectName(u"handleLabel")

        self.gridLayout.addWidget(self.handleLabel, 3, 3, 1, 1)

        self.officeComboBox = QComboBox(self.layoutWidget)
        self.officeComboBox.setObjectName(u"officeComboBox")

        self.gridLayout.addWidget(self.officeComboBox, 4, 1, 1, 1)

        self.datasourceLabel = QLabel(self.layoutWidget)
        self.datasourceLabel.setObjectName(u"datasourceLabel")

        self.gridLayout.addWidget(self.datasourceLabel, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 2, 1, 1)

        self.emailLabel = QLabel(self.layoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.gridLayout.addWidget(self.emailLabel, 5, 0, 1, 1)

        self.exigenciesComboBox = QComboBox(self.layoutWidget)
        self.exigenciesComboBox.addItem("")
        self.exigenciesComboBox.addItem("")
        self.exigenciesComboBox.setObjectName(u"exigenciesComboBox")

        self.gridLayout.addWidget(self.exigenciesComboBox, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 8, 3, 1, 1)

        self.exigenciesLabel = QLabel(self.layoutWidget)
        self.exigenciesLabel.setObjectName(u"exigenciesLabel")

        self.gridLayout.addWidget(self.exigenciesLabel, 3, 0, 1, 1)

        self.eventtypeLabel = QLabel(self.layoutWidget)
        self.eventtypeLabel.setObjectName(u"eventtypeLabel")

        self.gridLayout.addWidget(self.eventtypeLabel, 1, 0, 1, 1)

        self.officeLabel = QLabel(self.layoutWidget)
        self.officeLabel.setObjectName(u"officeLabel")

        self.gridLayout.addWidget(self.officeLabel, 4, 0, 1, 1)

        self.partselectLabel = QLabel(self.layoutWidget)
        self.partselectLabel.setObjectName(u"partselectLabel")

        self.gridLayout.addWidget(self.partselectLabel, 0, 3, 1, 1)

        self.subjectLineEdit = QLineEdit(self.layoutWidget)
        self.subjectLineEdit.setObjectName(u"subjectLineEdit")

        self.gridLayout.addWidget(self.subjectLineEdit, 6, 1, 1, 1)

        self.falutLabel = QLabel(self.layoutWidget)
        self.falutLabel.setObjectName(u"falutLabel")

        self.gridLayout.addWidget(self.falutLabel, 7, 0, 1, 1)

        self.enameComboBox = QComboBox(self.layoutWidget)
        self.enameComboBox.setObjectName(u"enameComboBox")

        self.gridLayout.addWidget(self.enameComboBox, 1, 4, 1, 1)

        self.currentstatusLabel = QLabel(self.layoutWidget)
        self.currentstatusLabel.setObjectName(u"currentstatusLabel")

        self.gridLayout.addWidget(self.currentstatusLabel, 2, 3, 1, 1)

        self.currentstatusComboBox = QComboBox(self.layoutWidget)
        self.currentstatusComboBox.addItem("")
        self.currentstatusComboBox.addItem("")
        self.currentstatusComboBox.addItem("")
        self.currentstatusComboBox.setObjectName(u"currentstatusComboBox")

        self.gridLayout.addWidget(self.currentstatusComboBox, 2, 4, 1, 1)

        self.sitenoLineEdit = QLineEdit(self.layoutWidget)
        self.sitenoLineEdit.setObjectName(u"sitenoLineEdit")

        self.gridLayout.addWidget(self.sitenoLineEdit, 5, 4, 1, 1)

        self.falutTextEdit = QTextEdit(self.layoutWidget)
        self.falutTextEdit.setObjectName(u"falutTextEdit")

        self.gridLayout.addWidget(self.falutTextEdit, 7, 1, 1, 4)

        self.evennumberLabel = QLabel(self.layoutWidget)
        self.evennumberLabel.setObjectName(u"evennumberLabel")

        self.gridLayout.addWidget(self.evennumberLabel, 4, 3, 1, 1)

        self.submitButton = QPushButton(self.layoutWidget)
        self.submitButton.setObjectName(u"submitButton")

        self.gridLayout.addWidget(self.submitButton, 9, 2, 1, 1)

        self.eventtypeComboBox = QComboBox(self.layoutWidget)
        self.eventtypeComboBox.addItem("")
        self.eventtypeComboBox.addItem("")
        self.eventtypeComboBox.setObjectName(u"eventtypeComboBox")

        self.gridLayout.addWidget(self.eventtypeComboBox, 1, 1, 1, 1)

        self.partLabel = QLabel(self.layoutWidget)
        self.partLabel.setObjectName(u"partLabel")
        self.partLabel.setMinimumSize(QSize(0, 0))
        self.partLabel.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.partLabel, 0, 0, 1, 1)

        self.partComboBox = QComboBox(self.layoutWidget)
        self.partComboBox.setObjectName(u"partComboBox")

        self.gridLayout.addWidget(self.partComboBox, 0, 1, 1, 1)

        self.sitenoLabel = QLabel(self.layoutWidget)
        self.sitenoLabel.setObjectName(u"sitenoLabel")

        self.gridLayout.addWidget(self.sitenoLabel, 5, 3, 1, 1)

        self.resetButton = QPushButton(self.layoutWidget)
        self.resetButton.setObjectName(u"resetButton")

        self.gridLayout.addWidget(self.resetButton, 9, 3, 1, 1)

        self.tipLabel = QLabel(workorderForm)
        self.tipLabel.setObjectName(u"tipLabel")
        self.tipLabel.setGeometry(QRect(60, 490, 498, 12))
        self.tipLabel.setStyleSheet(u"color: rgb(255, 29, 8);")

        self.retranslateUi(workorderForm)

        QMetaObject.connectSlotsByName(workorderForm)
    # setupUi

    def retranslateUi(self, workorderForm):
        workorderForm.setWindowTitle(QCoreApplication.translate("workorderForm", u"\u5de5\u5355\u8bb0\u5f55\u5de5\u5177", None))
        self.subjectLabel.setText(QCoreApplication.translate("workorderForm", u"\u4e8b\u4ef6\u6807\u9898\uff1a", None))
        self.handleComboBox.setItemText(0, QCoreApplication.translate("workorderForm", u"\u73b0\u573a", None))
        self.handleComboBox.setItemText(1, QCoreApplication.translate("workorderForm", u"\u8fdc\u7a0b", None))

        self.datasourceComboBox.setItemText(0, QCoreApplication.translate("workorderForm", u"\u7535\u8bdd\u62a5\u969c", None))
        self.datasourceComboBox.setItemText(1, QCoreApplication.translate("workorderForm", u"\u90ae\u4ef6\u62a5\u969c", None))

        self.enameLabel.setText(QCoreApplication.translate("workorderForm", u"\u9009\u62e9\u5de5\u7a0b\u5e08\uff1a", None))
        self.handleLabel.setText(QCoreApplication.translate("workorderForm", u"\u5904\u7406\u65b9\u5f0f\uff1a", None))
        self.datasourceLabel.setText(QCoreApplication.translate("workorderForm", u"\u62a5\u969c\u6765\u6e90\uff1a", None))
        self.emailLabel.setText(QCoreApplication.translate("workorderForm", u"\u62a5\u969c\u4eba\u90ae\u7bb1\uff1a", None))
        self.exigenciesComboBox.setItemText(0, QCoreApplication.translate("workorderForm", u"\u666e\u901a", None))
        self.exigenciesComboBox.setItemText(1, QCoreApplication.translate("workorderForm", u"\u7d27\u6025", None))

        self.exigenciesLabel.setText(QCoreApplication.translate("workorderForm", u"\u7d27\u6025\u7a0b\u5ea6\uff1a", None))
        self.eventtypeLabel.setText(QCoreApplication.translate("workorderForm", u"\u4e8b\u4ef6\u7c7b\u578b\uff1a", None))
        self.officeLabel.setText(QCoreApplication.translate("workorderForm", u"\u529e\u516c\u533a\uff1a", None))
        self.partselectLabel.setText(QCoreApplication.translate("workorderForm", u"\u4e8b\u4ef6\u5b50\u7c7b\uff1a", None))
        self.falutLabel.setText(QCoreApplication.translate("workorderForm", u"\u8be6\u7ec6\u63cf\u8ff0\uff1a", None))
        self.currentstatusLabel.setText(QCoreApplication.translate("workorderForm", u"\u5f53\u524d\u72b6\u6001\uff1a", None))
        self.currentstatusComboBox.setItemText(0, QCoreApplication.translate("workorderForm", u"\u5904\u7406\u4e2d", None))
        self.currentstatusComboBox.setItemText(1, QCoreApplication.translate("workorderForm", u"\u5df2\u89e3\u51b3", None))
        self.currentstatusComboBox.setItemText(2, QCoreApplication.translate("workorderForm", u"\u672a\u89e3\u51b3", None))

        self.evennumberLabel.setText(QCoreApplication.translate("workorderForm", u"\u5de5\u5355\u91cf\uff1a", None))
        self.submitButton.setText(QCoreApplication.translate("workorderForm", u"\u63d0 \u4ea4", None))
        self.eventtypeComboBox.setItemText(0, QCoreApplication.translate("workorderForm", u"\u684c\u9762\u7c7b\u4e8b\u4ef6", None))
        self.eventtypeComboBox.setItemText(1, QCoreApplication.translate("workorderForm", u"\u5176\u4ed6\u4e8b\u4ef6", None))

        self.partLabel.setText(QCoreApplication.translate("workorderForm", u"\u4e8b\u4ef6\u603b\u7c7b\uff1a", None))
        self.sitenoLabel.setText(QCoreApplication.translate("workorderForm", u"\u5de5\u4f4d\u53f7\uff1a", None))
        self.resetButton.setText(QCoreApplication.translate("workorderForm", u"\u91cd \u7f6e", None))
        self.tipLabel.setText(QCoreApplication.translate("workorderForm", u"\u63d0\u4ea4\u540e\u7684\u6570\u636e\u4fdd\u5b58\u5230csv_tables\u6587\u4ef6\u5939\u4e2d\u7684csv\u8868\uff0c\u52fe\u9009post\u63d0\u4ea4\uff0c\u6570\u636e\u540c\u65f6\u53d1\u9001\u5230\u670d\u52a1\u5668\u4e0a\u3002", None))
    # retranslateUi

