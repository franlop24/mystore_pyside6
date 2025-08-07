from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout
from datetime import datetime

from db import manager

from ui.ui_sale_widget import Ui_Sale_Form

class SalesWidget(QWidget, Ui_Sale_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.data = ''

        ## Personaliza tabla con encabezados y ancho de las columnas
        headers = ["ID", "Producto", "Descripción", "Cantidad", "Precio Unitario", "Subtotal"]
        self.detail_sale_table.setColumnCount(len(headers))
        self.detail_sale_table.setHorizontalHeaderLabels(headers)
        
        self.detail_sale_table.setColumnWidth(0, 50)   # ID
        self.detail_sale_table.setColumnWidth(1, 150)  # Nombre
        self.detail_sale_table.setColumnWidth(2, 250)  # Descripción
        self.detail_sale_table.setColumnWidth(3, 70)   # Stock
        self.detail_sale_table.setColumnWidth(4, 90)   # Precio
        self.detail_sale_table.setColumnWidth(5, 120)  # Categoría

        self.date_label.setText(str(datetime.now()))

        employees = manager.fetch_all('select id, nombre from empleado')
        for employee in employees:
            self.employees_combo.addItem(employee['nombre'], employee['id'])