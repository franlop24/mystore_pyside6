from PySide6.QtWidgets import QMainWindow, QLabel
from ui.ui_main import Ui_MainWindow
from controllers.categories_controller import CategoriesWidget
from controllers.products_controller import ProductsWidget
from pathlib import Path

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Mi Tienda')
        self.resize(960, 540)
        
        self.categories_widget = CategoriesWidget()
        self.stackedWidget.insertWidget(0, self.categories_widget)
        self.stackedWidget.setCurrentIndex(0)
        
        home_page = QLabel('Home Page')
        products_Page = ProductsWidget()
        ventas_page = QLabel('Ventas Nuevas Page')
        show_ventas_page = QLabel('Mostrar Ventas Page')
        
        self.stackedWidget.insertWidget(1, home_page)
        self.stackedWidget.insertWidget(2, products_Page)
        self.stackedWidget.insertWidget(3, ventas_page)
        self.stackedWidget.insertWidget(4, show_ventas_page)

        self.actionSalir.triggered.connect(self.close)
        self.actionCategorias.triggered.connect(self.show_categories_page)
        self.actionProductos.triggered.connect(self.show_products_page)
        self.actionAgregar_Venta.triggered.connect(self.show_ventas_add_page)
        self.actionMostrar_Ventas.triggered.connect(self.show_ventas_page)

    # cargamos los estilos del fichero
        self.cargarQSS("../qss/Ctor.qss")

    def cargarQSS(self, file):
        # guardamos la ruta absoluta al fichero
        path = absPath(file)
        # intentamos abrirlo y volcar el contenido
        try:
            with open(path) as styles:
                self.setStyleSheet(styles.read())
        # si hay algún fallo lo capturamos con una excepción genérica
        except:
            print("Error abriendo estilos", path)

    def show_categories_page(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def show_products_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def show_home_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def show_ventas_add_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def show_ventas_page(self):
        self.stackedWidget.setCurrentIndex(4)

    
    