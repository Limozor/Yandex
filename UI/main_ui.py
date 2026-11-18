from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QMenuBar,
    QPushButton,
    QStatusBar,
    QTableWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 500)
        MainWindow.setWindowTitle("Капучино")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")

        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.addButton.setText("Добавить")
        self.buttonLayout.addWidget(self.addButton)

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName("editButton")
        self.editButton.setText("Редактировать")
        self.buttonLayout.addWidget(self.editButton)

        self.verticalLayout.addLayout(self.buttonLayout)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 860, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)