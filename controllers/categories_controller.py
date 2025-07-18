from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from ui.ui_add_category import Ui_Form
from db import manager

class CategoriesWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.table_categories.setStatusTip('Para seleccionar haz doble click sobre la fila')

        self.load_categories()
        self.category_id = None


        self.button_save.clicked.connect(self.save_category)
        self.button_update.clicked.connect(self.update_category)
        self.button_delete.clicked.connect(self.delete_category)
        self.table_categories.doubleClicked.connect(self.get_data_row)

    def save_category(self):
        if self.category_id is None:
            category = self.name_line_edit.text()
            description = self.description_line_edit.text()
            if category and description:
                sql = 'INSERT INTO categories(category, description) VALUES (:category, :description)'
                values = {'category': category, 'description': description}
                manager.execute_query(sql, values)
                self.clear_form()
                self.load_categories()
            else:
                QMessageBox.warning(self, "Campos requeridos", "Por favor, completa todos los campos.")

    def update_category(self):
        if self.category_id is not None:
            category = self.name_line_edit.text()
            description = self.description_line_edit.text()
            if category and description:
                sql = 'UPDATE categories SET category = :category, description = :description WHERE id = :id'
                values = {'category': category, 'description': description, 'id': self.category_id}
                manager.execute_query(sql, values)
                self.clear_form()
                self.load_categories()
            else:
                QMessageBox.warning(self, "Campos requeridos", "Por favor, completa todos los campos.")
        else:
            QMessageBox.warning(self, "Selección Requerida", "Por favor, selecciona una fila para actualizar.")

    def delete_category(self):
        if self.category_id is None:
            QMessageBox.warning(self, "Selección Requerida", "Por favor, selecciona una fila para eliminar.")
        else:
            reply = QMessageBox.question(
                self,
                "Confirmar eliminación",
                "¿Estás seguro de que deseas eliminar esta categoría?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                sql = "DELETE FROM categories WHERE id = :id"
                values = { 'id': self.category_id }
                manager.execute_query(sql, values)
                self.clear_form()
                self.load_categories()

    def load_categories(self):
        sql = 'SELECT * FROM categories'
        categories  = manager.fetch_all(sql)
        self.table_categories.setRowCount(0)
        self.table_categories.setColumnCount(3)
        self.table_categories.setHorizontalHeaderLabels(["ID", "Categoría", "Descripción"])
        self.table_categories.setColumnWidth(0, 60)
        self.table_categories.setColumnWidth(1, 180)
        self.table_categories.setColumnWidth(2, 300)
        for row_idx, cat in enumerate(categories):
            self.table_categories.insertRow(row_idx)
            self.table_categories.setItem(row_idx, 0, QTableWidgetItem(str(cat['id'])))
            self.table_categories.setItem(row_idx, 1, QTableWidgetItem(cat['category']))
            self.table_categories.setItem(row_idx, 2, QTableWidgetItem(cat['description']))

    def get_data_row(self):
        selected_row = self.table_categories.currentRow()
        self.category_id = self.table_categories.item(selected_row, 0).text()
        category_name = self.table_categories.item(selected_row, 1).text()
        category_description = self.table_categories.item(selected_row, 2).text()
        self.name_line_edit.setText(category_name)
        self.description_line_edit.setText(category_description)

    def clear_form(self):
        self.name_line_edit.clear()
        self.description_line_edit.clear()
        self.category_id = None