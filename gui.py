from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ComboBoxes
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 100, 441, 31))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)

        self.comboBox_3 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout.addWidget(self.comboBox_3)

        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)

        # Labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 80, 81, 21))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 80, 55, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 80, 55, 16))
        self.label_3.setObjectName("label_3")


        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(120, 130, 661, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 660, 421, 16))
        self.label_4.setObjectName("label_4")


        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(130, 769, 661, 31))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(130, 750, 661, 20))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)

        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 820, 191, 28))
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1403, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.fill_combobox(self.comboBox_2, "category", "კატეგორია")
        self.fill_combobox(self.comboBox_3, "date", "თარიღი")
        self.fill_combobox(self.comboBox, "time", "დრო")


        self.comboBox_2.currentIndexChanged.connect(self.apply_filters)
        self.comboBox_3.currentIndexChanged.connect(self.apply_filters)
        self.comboBox.currentIndexChanged.connect(self.apply_filters)
        self.pushButton.clicked.connect(self.insert)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "კატეგორია"))
        self.label_2.setText(_translate("MainWindow", "თარიღი"))
        self.label_3.setText(_translate("MainWindow", "დრო"))
        self.label_4.setText(_translate("MainWindow", "განცხადების განთავსება"))
        self.label_10.setText(_translate("MainWindow", "კატეგორია"))
        self.label_9.setText(_translate("MainWindow", "სახელი"))
        self.label_8.setText(_translate("MainWindow", "თარიღი"))
        self.label_7.setText(_translate("MainWindow", "დრო"))
        self.label_6.setText(_translate("MainWindow", "ფასი"))
        self.label_5.setText(_translate("MainWindow", "პაროლი"))
        self.pushButton.setText(_translate("MainWindow", "განცხადების განთავსება"))

    def fill_combobox(self, combobox, column_name, skip_value):
        conn = sqlite3.connect("mysql.sqlite3")
        cursor = conn.cursor()
        cursor.execute(f"SELECT DISTINCT {column_name} FROM mysql")
        values = [row[0] for row in cursor.fetchall()]
        conn.close()
        if skip_value in values:
            values.remove(skip_value)
        values.sort()
        values.insert(0, "ნებისმიერი")
        combobox.addItems(values)

    def load_data_to_table(self, data):
        self.tableWidget.setRowCount(0)
        if data:
            column_count = len(data[0])
            self.tableWidget.setColumnCount(column_count)
            self.tableWidget.setRowCount(len(data))
            for row_idx, row_data in enumerate(data):
                for col_idx, value in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row_idx, col_idx, item)

    def apply_filters(self):
        category = self.comboBox_2.currentText()
        date = self.comboBox_3.currentText()
        time = self.comboBox.currentText()

        query = "SELECT id, category, description, date, time, price FROM mysql WHERE 1=1"
        params = []

        if category != "ნებისმიერი":
            query += " AND category=?"
            params.append(category)
        if date != "ნებისმიერი":
            query += " AND date=?"
            params.append(date)
        if time != "ნებისმიერი":
            query += " AND time=?"
            params.append(time)

        conn = sqlite3.connect("mysql.sqlite3")
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        self.load_data_to_table(results)
    def insert(self):
        conn = sqlite3.connect("mysql.sqlite3")
        cursor = conn.cursor()
        a=cursor.execute("SELECT * FROM mysql")
        a=a.fetchall()
        a=len(a)
        id=a
        category = self.lineEdit_4.text()
        description = self.lineEdit_5.text()
        date = self.lineEdit_3.text()
        time = self.lineEdit_2.text()
        price = self.lineEdit_6.text()
        password = self.lineEdit.text()
        cursor.execute("INSERT INTO mysql VALUES (?,?,?,?,?,?,?)", (id, category, description, date, time, price, password))
        conn.commit()
        cursor.execute("SELECT * FROM mysql")
        results = cursor.fetchall()
        self.load_data_to_table(results)
        cursor.execute("DELETE FROM mysql WHERE id = ?", (id,))
        conn.commit()
        conn.close()
#4532


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.insert()
    conn = sqlite3.connect("mysql.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT id, category, description, date, time, price FROM mysql")

    data = cursor.fetchall()
    conn.close()

    ui.load_data_to_table(data)

    MainWindow.show()
    sys.exit(app.exec_())