from PySide6.QtWidgets import QApplication
from controllers.main_controller import MainWindow
from qt_material import apply_stylesheet

if __name__ == '__main__':
    app = QApplication([])
    apply_stylesheet(app, theme='dark_purple.xml')
    window = MainWindow()
    window.show()
    app.exec()