import sqlite3
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QDialog,
    QMainWindow,
    QTableWidgetItem,
)


class AddEditCoffeeForm(QDialog):
    def __init__(self, coffee_id=None):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.coffee_id = coffee_id
        self.saveButton.clicked.connect(self.save_record)

        if self.coffee_id is not None:
            self.load_record()

    def load_record(self):
        connection = sqlite3.connect("coffee.sqlite")
        cursor = connection.cursor()
        row = cursor.execute(
            "SELECT sort_name, roast_degree, ground_or_beans, "
            "taste_description, price, package_volume "
            "FROM coffee WHERE id = ?",
            (self.coffee_id,),
        ).fetchone()
        connection.close()

        if row is not None:
            self.sortNameEdit.setText(str(row[0]))
            self.roastDegreeEdit.setText(str(row[1]))
            self.groundOrBeansEdit.setText(str(row[2]))
            self.tasteDescriptionEdit.setText(
                "" if row[3] is None else str(row[3])
            )
            self.priceSpinBox.setValue(float(row[4]))
            self.packageVolumeSpinBox.setValue(int(row[5]))

    def save_record(self):
        sort_name = self.sortNameEdit.text().strip()
        roast_degree = self.roastDegreeEdit.text().strip()
        ground_or_beans = self.groundOrBeansEdit.text().strip()
        taste_description = self.tasteDescriptionEdit.text().strip()
        price = self.priceSpinBox.value()
        package_volume = self.packageVolumeSpinBox.value()

        if not sort_name or not roast_degree or not ground_or_beans:
            return

        connection = sqlite3.connect("coffee.sqlite")
        cursor = connection.cursor()

        if self.coffee_id is None:
            cursor.execute(
                "INSERT INTO coffee (sort_name, roast_degree, "
                "ground_or_beans, taste_description, price, package_volume) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (
                    sort_name,
                    roast_degree,
                    ground_or_beans,
                    taste_description,
                    price,
                    package_volume,
                ),
            )
        else:
            cursor.execute(
                "UPDATE coffee SET sort_name = ?, roast_degree = ?, "
                "ground_or_beans = ?, taste_description = ?, price = ?, "
                "package_volume = ? WHERE id = ?",
                (
                    sort_name,
                    roast_degree,
                    ground_or_beans,
                    taste_description,
                    price,
                    package_volume,
                    self.coffee_id,
                ),
            )

        connection.commit()
        connection.close()
        self.accept()


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.tableWidget.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.tableWidget.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tableWidget.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.addButton.clicked.connect(self.add_coffee)
        self.editButton.clicked.connect(self.edit_coffee)
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

    def add_coffee(self):
        dialog = AddEditCoffeeForm()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_data()

    def edit_coffee(self):
        current_row = self.tableWidget.currentRow()
        if current_row < 0:
            self.statusBar().showMessage(
                "Выберите запись в таблице для редактирования"
            )
            return

        self.statusBar().clearMessage()
        coffee_id = int(self.tableWidget.item(current_row, 0).text())
        dialog = AddEditCoffeeForm(coffee_id)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CoffeeApp()
    ex.show()
    sys.exit(app.exec())