# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sale_widgetPPhAtr.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Sale_Form(object):
    def setupUi(self, Sale_Form):
        if not Sale_Form.objectName():
            Sale_Form.setObjectName(u"Sale_Form")
        Sale_Form.resize(523, 379)
        self.add_product_button = QPushButton(Sale_Form)
        self.add_product_button.setObjectName(u"add_product_button")
        self.add_product_button.setGeometry(QRect(30, 100, 151, 32))
        self.widget = QWidget(Sale_Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 451, 23))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.date_label = QLabel(self.widget)
        self.date_label.setObjectName(u"date_label")

        self.horizontalLayout.addWidget(self.date_label)

        self.widget1 = QWidget(Sale_Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 60, 451, 32))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.employees_combo = QComboBox(self.widget1)
        self.employees_combo.setObjectName(u"employees_combo")

        self.horizontalLayout_2.addWidget(self.employees_combo)

        self.widget2 = QWidget(Sale_Form)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(30, 140, 451, 151))
        self.verticalLayout = QVBoxLayout(self.widget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.detail_sale_table = QTableWidget(self.widget2)
        self.detail_sale_table.setObjectName(u"detail_sale_table")

        self.verticalLayout.addWidget(self.detail_sale_table)

        self.widget3 = QWidget(Sale_Form)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(290, 310, 191, 23))
        self.horizontalLayout_3 = QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.total_line_edit = QLineEdit(self.widget3)
        self.total_line_edit.setObjectName(u"total_line_edit")

        self.horizontalLayout_3.addWidget(self.total_line_edit)


        self.retranslateUi(Sale_Form)

        QMetaObject.connectSlotsByName(Sale_Form)
    # setupUi

    def retranslateUi(self, Sale_Form):
        Sale_Form.setWindowTitle(QCoreApplication.translate("Sale_Form", u"Form", None))
        self.add_product_button.setText(QCoreApplication.translate("Sale_Form", u"Agregar Producto", None))
        self.label.setText(QCoreApplication.translate("Sale_Form", u"Fecha", None))
        self.date_label.setText(QCoreApplication.translate("Sale_Form", u"hoy", None))
        self.label_2.setText(QCoreApplication.translate("Sale_Form", u"Empleado", None))
        self.label_3.setText(QCoreApplication.translate("Sale_Form", u"Art\u00edculos", None))
        self.label_4.setText(QCoreApplication.translate("Sale_Form", u"Total", None))
    # retranslateUi

