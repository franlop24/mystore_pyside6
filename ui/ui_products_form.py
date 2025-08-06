# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'products_formVWOOca.ui'
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
    QSizePolicy, QSpinBox, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_ProductsForm(object):
    def setupUi(self, ProductsForm):
        if not ProductsForm.objectName():
            ProductsForm.setObjectName(u"ProductsForm")
        ProductsForm.resize(700, 400)
        self.products_stacked_widget = QStackedWidget(ProductsForm)
        self.products_stacked_widget.setObjectName(u"products_stacked_widget")
        self.products_stacked_widget.setGeometry(QRect(10, 10, 681, 381))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.layoutWidget = QWidget(self.page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 661, 361))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.description_text_edit = QTextEdit(self.layoutWidget)
        self.description_text_edit.setObjectName(u"description_text_edit")

        self.horizontalLayout_2.addWidget(self.description_text_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.stock_spinbox = QSpinBox(self.layoutWidget)
        self.stock_spinbox.setObjectName(u"stock_spinbox")
        self.stock_spinbox.setMaximum(999999)

        self.horizontalLayout_3.addWidget(self.stock_spinbox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.price_dspinbox = QDoubleSpinBox(self.layoutWidget)
        self.price_dspinbox.setObjectName(u"price_dspinbox")
        self.price_dspinbox.setMaximum(999999.989999999990687)

        self.horizontalLayout_4.addWidget(self.price_dspinbox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.category_combo_box = QComboBox(self.layoutWidget)
        self.category_combo_box.setObjectName(u"category_combo_box")

        self.horizontalLayout_5.addWidget(self.category_combo_box)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.save_button = QPushButton(self.layoutWidget)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_6.addWidget(self.save_button)

        self.update_button = QPushButton(self.layoutWidget)
        self.update_button.setObjectName(u"update_button")

        self.horizontalLayout_6.addWidget(self.update_button)

        self.delete_button = QPushButton(self.layoutWidget)
        self.delete_button.setObjectName(u"delete_button")

        self.horizontalLayout_6.addWidget(self.delete_button)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.button_view_products = QPushButton(self.layoutWidget)
        self.button_view_products.setObjectName(u"button_view_products")

        self.verticalLayout.addWidget(self.button_view_products)

        self.products_stacked_widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.layoutWidget1 = QWidget(self.page_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(38, 20, 611, 341))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.search_by_id_line_edit = QLineEdit(self.layoutWidget1)
        self.search_by_id_line_edit.setObjectName(u"search_by_id_line_edit")

        self.horizontalLayout_7.addWidget(self.search_by_id_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.search_by_category_combo = QComboBox(self.layoutWidget1)
        self.search_by_category_combo.setObjectName(u"search_by_category_combo")

        self.horizontalLayout_8.addWidget(self.search_by_category_combo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.search_by_name_line_edit = QLineEdit(self.layoutWidget1)
        self.search_by_name_line_edit.setObjectName(u"search_by_name_line_edit")

        self.horizontalLayout_9.addWidget(self.search_by_name_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.refresh_table_button = QPushButton(self.layoutWidget1)
        self.refresh_table_button.setObjectName(u"refresh_table_button")

        self.horizontalLayout_10.addWidget(self.refresh_table_button)

        self.new_product_button = QPushButton(self.layoutWidget1)
        self.new_product_button.setObjectName(u"new_product_button")

        self.horizontalLayout_10.addWidget(self.new_product_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.products_table = QTableWidget(self.layoutWidget1)
        self.products_table.setObjectName(u"products_table")

        self.verticalLayout_2.addWidget(self.products_table)

        self.products_stacked_widget.addWidget(self.page_2)

        self.retranslateUi(ProductsForm)

        self.products_stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(ProductsForm)
    # setupUi

    def retranslateUi(self, ProductsForm):
        ProductsForm.setWindowTitle(QCoreApplication.translate("ProductsForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("ProductsForm", u"Nombre:", None))
        self.label_2.setText(QCoreApplication.translate("ProductsForm", u"Descripci\u00f3n:", None))
        self.label_3.setText(QCoreApplication.translate("ProductsForm", u"Cantidad:", None))
        self.label_4.setText(QCoreApplication.translate("ProductsForm", u"Precio:", None))
        self.label_5.setText(QCoreApplication.translate("ProductsForm", u"Categor\u00eda:", None))
        self.save_button.setText(QCoreApplication.translate("ProductsForm", u"Guardar", None))
        self.update_button.setText(QCoreApplication.translate("ProductsForm", u"Actualizar", None))
        self.delete_button.setText(QCoreApplication.translate("ProductsForm", u"Eliminar", None))
        self.button_view_products.setText(QCoreApplication.translate("ProductsForm", u"Ver productos", None))
        self.label_6.setText(QCoreApplication.translate("ProductsForm", u"Id:", None))
        self.label_7.setText(QCoreApplication.translate("ProductsForm", u"Categor\u00eda:", None))
        self.label_8.setText(QCoreApplication.translate("ProductsForm", u"Nombre:", None))
        self.refresh_table_button.setText(QCoreApplication.translate("ProductsForm", u"Recargar Tabla", None))
        self.new_product_button.setText(QCoreApplication.translate("ProductsForm", u"Agregar Producto", None))
    # retranslateUi

