from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from ui.ui_add_category import Ui_Form
from db import manager

class CategoriesWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_save.clicked.connect(self.save_category)
        self.load_categories()

    def save_category(self):
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

    def clear_form(self):
        self.name_line_edit.clear()
        self.description_line_edit.clear()