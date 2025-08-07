# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_productiOfKeD.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_AddProductForm(object):
    def setupUi(self, AddProductForm):
        if not AddProductForm.objectName():
            AddProductForm.setObjectName(u"AddProductForm")
        AddProductForm.resize(877, 500)
        self.widget = QWidget(AddProductForm)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 50, 781, 402))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.id_line_edit = QLineEdit(self.widget)
        self.id_line_edit.setObjectName(u"id_line_edit")

        self.horizontalLayout.addWidget(self.id_line_edit)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.categories_combo = QComboBox(self.widget)
        self.categories_combo.setObjectName(u"categories_combo")

        self.horizontalLayout_2.addWidget(self.categories_combo)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.name_line_edit = QLineEdit(self.widget)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.horizontalLayout_3.addWidget(self.name_line_edit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.products_table = QTableWidget(self.widget)
        self.products_table.setObjectName(u"products_table")

        self.verticalLayout_5.addWidget(self.products_table)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.name_product_line = QLineEdit(self.widget)
        self.name_product_line.setObjectName(u"name_product_line")
        self.name_product_line.setReadOnly(True)

        self.verticalLayout.addWidget(self.name_product_line)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.description_product_line = QLineEdit(self.widget)
        self.description_product_line.setObjectName(u"description_product_line")
        self.description_product_line.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.description_product_line)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.cantity_product_spin = QSpinBox(self.widget)
        self.cantity_product_spin.setObjectName(u"cantity_product_spin")

        self.verticalLayout_3.addWidget(self.cantity_product_spin)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.price_product_spin = QDoubleSpinBox(self.widget)
        self.price_product_spin.setObjectName(u"price_product_spin")
        self.price_product_spin.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.price_product_spin)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.add_product_sale_button = QPushButton(self.widget)
        self.add_product_sale_button.setObjectName(u"add_product_sale_button")

        self.verticalLayout_5.addWidget(self.add_product_sale_button)


        self.retranslateUi(AddProductForm)

        QMetaObject.connectSlotsByName(AddProductForm)
    # setupUi

    def retranslateUi(self, AddProductForm):
        AddProductForm.setWindowTitle(QCoreApplication.translate("AddProductForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("AddProductForm", u"Buscar por Id", None))
        self.label_2.setText(QCoreApplication.translate("AddProductForm", u"Buscar por Categor\u00eda", None))
        self.label_3.setText(QCoreApplication.translate("AddProductForm", u"Buscar por Nombre", None))
        self.label_4.setText(QCoreApplication.translate("AddProductForm", u"Nombre", None))
        self.label_5.setText(QCoreApplication.translate("AddProductForm", u"Descripci\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("AddProductForm", u"Cantidad", None))
        self.label_7.setText(QCoreApplication.translate("AddProductForm", u"Precio", None))
        self.add_product_sale_button.setText(QCoreApplication.translate("AddProductForm", u"Agregar a Venta", None))
    # retranslateUi

