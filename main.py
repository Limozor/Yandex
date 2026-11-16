import sqlite3
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.load_data()

    def load_data(self):
        headers = [
            "ID",
            "Название сорта",
            "Степень обжарки",
            "Молотый/в зернах",
            "Описание вкуса",
            "Цена",
            "Объем упаковки",
        ]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        connection = sqlite3.connect("coffee.sqlite")
        cursor = connection.cursor()
        rows = cursor.execute(
            "SELECT id, sort_name, roast_degree, ground_or_beans, "
            "taste_description, price, package_volume FROM coffee"
        ).fetchall()
        connection.close()

        self.tableWidget.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, value in enumerate(row_data):
                self.tableWidget.setItem(
                    row_idx, col_idx, QTableWidgetItem(str(value))
                )
        self.tableWidget.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CoffeeApp()
    ex.show()
    sys.exit(app.exec())