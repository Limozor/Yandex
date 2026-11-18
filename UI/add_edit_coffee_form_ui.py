from PyQt6.QtWidgets import (
    QDoubleSpinBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
)


class Ui_AddEditCoffeeForm:
    def setupUi(self, AddEditCoffeeForm):
        AddEditCoffeeForm.setObjectName("AddEditCoffeeForm")
        AddEditCoffeeForm.resize(420, 300)
        AddEditCoffeeForm.setWindowTitle("Добавить / редактировать запись")

        self.verticalLayout = QVBoxLayout(AddEditCoffeeForm)
        self.verticalLayout.setObjectName("verticalLayout")

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.labelSort = QLabel(AddEditCoffeeForm)
        self.labelSort.setObjectName("labelSort")
        self.labelSort.setText("Название сорта")
        self.formLayout.setWidget(
            0, QFormLayout.ItemRole.LabelRole, self.labelSort
        )

        self.sortNameEdit = QLineEdit(AddEditCoffeeForm)
        self.sortNameEdit.setObjectName("sortNameEdit")
        self.formLayout.setWidget(
            0, QFormLayout.ItemRole.FieldRole, self.sortNameEdit
        )

        self.labelRoast = QLabel(AddEditCoffeeForm)
        self.labelRoast.setObjectName("labelRoast")
        self.labelRoast.setText("Степень обжарки")
        self.formLayout.setWidget(
            1, QFormLayout.ItemRole.LabelRole, self.labelRoast
        )

        self.roastDegreeEdit = QLineEdit(AddEditCoffeeForm)
        self.roastDegreeEdit.setObjectName("roastDegreeEdit")
        self.formLayout.setWidget(
            1, QFormLayout.ItemRole.FieldRole, self.roastDegreeEdit
        )

        self.labelType = QLabel(AddEditCoffeeForm)
        self.labelType.setObjectName("labelType")
        self.labelType.setText("Молотый/в зернах")
        self.formLayout.setWidget(
            2, QFormLayout.ItemRole.LabelRole, self.labelType
        )

        self.groundOrBeansEdit = QLineEdit(AddEditCoffeeForm)
        self.groundOrBeansEdit.setObjectName("groundOrBeansEdit")
        self.formLayout.setWidget(
            2, QFormLayout.ItemRole.FieldRole, self.groundOrBeansEdit
        )

        self.labelTaste = QLabel(AddEditCoffeeForm)
        self.labelTaste.setObjectName("labelTaste")
        self.labelTaste.setText("Описание вкуса")
        self.formLayout.setWidget(
            3, QFormLayout.ItemRole.LabelRole, self.labelTaste
        )

        self.tasteDescriptionEdit = QLineEdit(AddEditCoffeeForm)
        self.tasteDescriptionEdit.setObjectName("tasteDescriptionEdit")
        self.formLayout.setWidget(
            3, QFormLayout.ItemRole.FieldRole, self.tasteDescriptionEdit
        )

        self.labelPrice = QLabel(AddEditCoffeeForm)
        self.labelPrice.setObjectName("labelPrice")
        self.labelPrice.setText("Цена")
        self.formLayout.setWidget(
            4, QFormLayout.ItemRole.LabelRole, self.labelPrice
        )

        self.priceSpinBox = QDoubleSpinBox(AddEditCoffeeForm)
        self.priceSpinBox.setObjectName("priceSpinBox")
        self.priceSpinBox.setMaximum(1000000.0)
        self.formLayout.setWidget(
            4, QFormLayout.ItemRole.FieldRole, self.priceSpinBox
        )

        self.labelVolume = QLabel(AddEditCoffeeForm)
        self.labelVolume.setObjectName("labelVolume")
        self.labelVolume.setText("Объем упаковки")
        self.formLayout.setWidget(
            5, QFormLayout.ItemRole.LabelRole, self.labelVolume
        )

        self.packageVolumeSpinBox = QSpinBox(AddEditCoffeeForm)
        self.packageVolumeSpinBox.setObjectName("packageVolumeSpinBox")
        self.packageVolumeSpinBox.setMaximum(1000000)
        self.formLayout.setWidget(
            5, QFormLayout.ItemRole.FieldRole, self.packageVolumeSpinBox
        )

        self.verticalLayout.addLayout(self.formLayout)

        self.saveButton = QPushButton(AddEditCoffeeForm)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setText("Сохранить")
        self.verticalLayout.addWidget(self.saveButton)