from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt

from ui.ui_products_form import Ui_ProductsForm

from db import manager

class ProductsWidget(QWidget, Ui_ProductsForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ## Inicializa datos del widget, lista de productos, elementos de los combos
        ## id del producto
        self.product_id = None

        sql = 'SELECT products.id, products.name, products.description, products.stock, products.price, categories.category FROM products products JOIN categories ON products.category_id = categories.id'
        self.products = manager.fetch_all(sql)
        
        self.search_by_category_combo.setStatusTip('Selecciona una categoría para filtrar')
        self.search_by_id_line_edit.setStatusTip('Escribe el id a buscar y presiona Enter')
        self.search_by_name_line_edit.setStatusTip('Escribe el nombre a buscar y presiona Enter')
        
        self.category_combo_box.addItem('-----', -1)
        categories = manager.fetch_all('SELECT * FROM categories')
        for category in categories:
            self.category_combo_box.addItem(category['category'], category['id'])
            self.search_by_category_combo.addItem(category['category'], category['id'])

        ## Personaliza tabla con encabezados y ancho de las columnas
        headers = ["ID", "Nombre", "Descripción", "Stock", "Precio", "Categoría"]
        self.products_table.setColumnCount(len(headers))
        self.products_table.setHorizontalHeaderLabels(headers)
        
        self.products_table.setColumnWidth(0, 50)   # ID
        self.products_table.setColumnWidth(1, 150)  # Nombre
        self.products_table.setColumnWidth(2, 250)  # Descripción
        self.products_table.setColumnWidth(3, 70)   # Stock
        self.products_table.setColumnWidth(4, 90)   # Precio
        self.products_table.setColumnWidth(5, 120)  # Categoría
        self.products_table.setStatusTip('Para seleccionar da doble click')

        # carga inicial de productos
        self.load_products()
        self.products_stacked_widget.setCurrentIndex(1)

        ## Agrega los eventos a cada objeto del Widget
        self.save_button.clicked.connect(self.save_product)
        self.new_product_button.clicked.connect(self.show_new_products_form)
        self.button_view_products.clicked.connect(self.show_products_table)
        self.products_table.doubleClicked.connect(self.get_data_row)
        self.update_button.clicked.connect(self.update_product)
        self.delete_button.clicked.connect(self.delete_product)
        self.refresh_table_button.clicked.connect(self.refresh_table)
        self.search_by_category_combo.currentIndexChanged.connect(self.get_products_by_category)
        self.search_by_id_line_edit.returnPressed.connect(self.get_products_by_id)
        self.search_by_name_line_edit.returnPressed.connect(self.get_products_by_name)

    def save_product(self):
        name = self.name_line_edit.text()
        description = self.description_text_edit.toPlainText()
        stock = self.stock_spinbox.value()
        price = self.price_dspinbox.value()
        category_id = self.category_combo_box.currentData(Qt.UserRole)
        sql = "INSERT INTO products(name, description, stock, price, category_id) "
        sql += "VALUES( :name, :description, :stock, :price, :category_id)"
        values = {
            'name': name,
            'description': description,
            'stock': stock,
            'price': price,
            'category_id': category_id
        }
        result = manager.execute_query(sql, values)
        if result: 
            QMessageBox.information(self, "Éxito", "Producto guardado correctamente.")
            self.clear_form()
            self.products_stacked_widget.setCurrentIndex(1)

    def delete_product(self):
        if self.product_id:
            reply = QMessageBox.question(
                self,
                "Confirmar eliminación",
                "¿Estás seguro de que deseas eliminar este Producto?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                sql = "DELETE FROM products WHERE id = :id"
                manager.execute_query(sql, {'id': self.product_id})
                self.clear_form()
                self.products_stacked_widget.setCurrentIndex(1)

    def update_product(self):
        if self.product_id:
            name = self.name_line_edit.text()
            description = self.description_text_edit.toPlainText()
            stock = self.stock_spinbox.value()
            price = self.price_dspinbox.value()
            category_id = self.category_combo_box.currentData(Qt.UserRole)
            sql = 'UPDATE products SET name = :name, description = :description, stock = :stock, '
            sql += 'price = :price, category_id = :category_id WHERE id = :id'
            values = {
                'name': name,
                'description': description,
                'stock': stock,
                'price': price,
                'category_id': category_id,
                'id': self.product_id
            }
            result = manager.execute_query(sql, values)
            if result: 
                QMessageBox.information(self, "Éxito", "Producto Actualizado correctamente.")
                self.clear_form()
                self.products_stacked_widget.setCurrentIndex(1)

    def get_data_row(self):
        selected_row = self.products_table.currentRow()
        self.product_id = self.products_table.item(selected_row, 0).text()
        name = self.products_table.item(selected_row, 1).text()
        description = self.products_table.item(selected_row, 2).text()
        stock = self.products_table.item(selected_row, 3).text()
        price = self.products_table.item(selected_row, 4).text()
        category = self.products_table.item(selected_row, 5).text()
        self.name_line_edit.setText(name)
        self.description_text_edit.setText(description)
        self.stock_spinbox.setValue(int(stock))
        self.price_dspinbox.setValue(float(price))
        self.category_combo_box.setCurrentText(category)
        self.products_stacked_widget.setCurrentIndex(0)

    def clear_form(self):
        self.name_line_edit.clear()
        self.description_text_edit.clear()
        self.stock_spinbox.setValue(0)
        self.price_dspinbox.setValue(0.0)
        self.category_combo_box.setCurrentIndex(0)
        self.product_id = None

    def load_products(self):
        self.products_table.setRowCount(len(self.products))
        for row_idx, product in enumerate(self.products):
            self.products_table.setItem(row_idx, 0, QTableWidgetItem(str(product['id'])))
            self.products_table.setItem(row_idx, 1, QTableWidgetItem(product['name']))
            self.products_table.setItem(row_idx, 2, QTableWidgetItem(product['description']))
            self.products_table.setItem(row_idx, 3, QTableWidgetItem(str(product['stock'])))
            self.products_table.setItem(row_idx, 4, QTableWidgetItem(str(product['price'])))
            self.products_table.setItem(row_idx, 5, QTableWidgetItem(product['category']))

    def refresh_table(self):
        sql = 'SELECT products.id, products.name, products.description, products.stock, products.price, categories.category FROM products products JOIN categories ON products.category_id = categories.id'
        self.products = manager.fetch_all(sql)
        self.load_products()

    def get_products_by_id(self):
        sql = 'SELECT products.id, products.name, products.description, products.stock, products.price, categories.category FROM products products JOIN categories ON products.category_id = categories.id '
        sql += 'WHERE products.id = :id'
        self.products = manager.fetch_all(sql, {'id': self.search_by_id_line_edit.text()})
        self.load_products()

    def get_products_by_category(self):
        sql = 'SELECT products.id, products.name, products.description, products.stock, products.price, categories.category FROM products products JOIN categories ON products.category_id = categories.id '
        sql += 'WHERE products.category_id = :category_id'
        values = {
            'category_id': self.search_by_category_combo.currentData(Qt.UserRole)
        }
        self.products = manager.fetch_all(sql, values)
        self.load_products()

    def get_products_by_name(self):
        sql = 'SELECT products.id, products.name, products.description, products.stock, products.price, categories.category FROM products products JOIN categories ON products.category_id = categories.id '
        sql += 'WHERE products.name LIKE :name'
        values = {
            'name': f"%{self.search_by_name_line_edit.text()}%"
        }
        self.products = manager.fetch_all(sql,values)
        self.load_products()

    def show_new_products_form(self):
        self.clear_form()
        self.products_stacked_widget.setCurrentIndex(0)

    def show_products_table(self):
        self.products_stacked_widget.setCurrentIndex(1)
