from PySide6.QtWidgets import QMainWindow
from ui.ui_main import Ui_MainWindow
from controllers.categories_controller import CategoriesWidget

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Mi Tienda')
        
        self.categories_widget = CategoriesWidget()
        self.stackedWidget.insertWidget(0, self.categories_widget)
        self.stackedWidget.setCurrentIndex(0)
        
        self.actionSalir.triggered.connect(self.close)
        self.actionCategorias.triggered.connect(self.show_categories_page)
        self.actionProductos.triggered.connect(self.show_products_page)

    def show_categories_page(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def show_products_page(self):
        self.stackedWidget.setCurrentIndex(1)
    