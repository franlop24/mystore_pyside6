# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_categoryNKEJoM.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 500)
        self.table_categories = QTableWidget(Form)
        self.table_categories.setObjectName(u"table_categories")
        self.table_categories.setGeometry(QRect(110, 170, 581, 192))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(120, 0, 571, 157))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 20, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.name_line_edit = QLineEdit(self.layoutWidget)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.horizontalLayout.addWidget(self.name_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.description_line_edit = QLineEdit(self.layoutWidget)
        self.description_line_edit.setObjectName(u"description_line_edit")

        self.horizontalLayout_2.addWidget(self.description_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.button_save = QPushButton(self.layoutWidget)
        self.button_save.setObjectName(u"button_save")

        self.verticalLayout.addWidget(self.button_save)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_update = QPushButton(self.layoutWidget)
        self.button_update.setObjectName(u"button_update")

        self.horizontalLayout_3.addWidget(self.button_update)

        self.button_delete = QPushButton(self.layoutWidget)
        self.button_delete.setObjectName(u"button_delete")

        self.horizontalLayout_3.addWidget(self.button_delete)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Descripci\u00f3n", None))
        self.button_save.setText(QCoreApplication.translate("Form", u"Guardar", None))
        self.button_update.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.button_delete.setText(QCoreApplication.translate("Form", u"Eliminar", None))
    # retranslateUi

