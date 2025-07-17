# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainzQzNao.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStackedWidget, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionCategorias = QAction(MainWindow)
        self.actionCategorias.setObjectName(u"actionCategorias")
        self.actionProductos = QAction(MainWindow)
        self.actionProductos.setObjectName(u"actionProductos")
        self.actionAgregar_Venta = QAction(MainWindow)
        self.actionAgregar_Venta.setObjectName(u"actionAgregar_Venta")
        self.actionMostrar_Ventas = QAction(MainWindow)
        self.actionMostrar_Ventas.setObjectName(u"actionMostrar_Ventas")
        self.actionAyuda = QAction(MainWindow)
        self.actionAyuda.setObjectName(u"actionAyuda")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 9, 701, 541))
        self.page01 = QWidget()
        self.page01.setObjectName(u"page01")
        self.stackedWidget.addWidget(self.page01)
        self.page02 = QWidget()
        self.page02.setObjectName(u"page02")
        self.stackedWidget.addWidget(self.page02)
        self.page03 = QWidget()
        self.page03.setObjectName(u"page03")
        self.stackedWidget.addWidget(self.page03)
        self.page04 = QWidget()
        self.page04.setObjectName(u"page04")
        self.stackedWidget.addWidget(self.page04)
        self.page05 = QWidget()
        self.page05.setObjectName(u"page05")
        self.stackedWidget.addWidget(self.page05)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuProductos = QMenu(self.menubar)
        self.menuProductos.setObjectName(u"menuProductos")
        self.menuVentas = QMenu(self.menubar)
        self.menuVentas.setObjectName(u"menuVentas")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuProductos.menuAction())
        self.menubar.addAction(self.menuVentas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionSalir)
        self.menuProductos.addAction(self.actionCategorias)
        self.menuProductos.addAction(self.actionProductos)
        self.menuVentas.addAction(self.actionAgregar_Venta)
        self.menuVentas.addAction(self.actionMostrar_Ventas)
        self.menuAyuda.addAction(self.actionAyuda)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionCategorias.setText(QCoreApplication.translate("MainWindow", u"Categorias", None))
        self.actionProductos.setText(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.actionAgregar_Venta.setText(QCoreApplication.translate("MainWindow", u"Agregar Venta", None))
        self.actionMostrar_Ventas.setText(QCoreApplication.translate("MainWindow", u"Mostrar Ventas", None))
        self.actionAyuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuProductos.setTitle(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.menuVentas.setTitle(QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

