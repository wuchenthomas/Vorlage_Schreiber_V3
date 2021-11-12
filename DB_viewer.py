import sys

import pymysql
from PyQt5.QtWidgets import QApplication, QWidget, QHeaderView, QAbstractItemView, QPushButton, QTableWidget, \
    QTableWidgetItem, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

table_header = ["Sex", "FirstName", "LastName", "Name", "Address1", "Address2", "PostCode", "Country"]


class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__(1, 8)
        self.setHorizontalHeaderLabels(table_header)
        # self.verticalHeader().setDefaultSectionSize(50)
        # self.horizontalHeader().setDefaultSectionSize(250)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_db()

    def load_db(self):
        while self.rowCount() != 1:
            self._removeRow()
        connection = pymysql.connect(host='192.168.0.203',
                                     user="contact_addresses",
                                     password="H+9gV@3Ff2*s-Q",
                                     database='contao',
                                     cursorclass=pymysql.cursors.DictCursor,
                                     local_infile=True)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM rffe_contact_addresses ORDER BY FirstName"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                self.setItem(self.rowCount() - 1, 0, QTableWidgetItem(str(row['Sex'])))
                self.setItem(self.rowCount() - 1, 1, QTableWidgetItem(str(row["FirstName"])))
                self.setItem(self.rowCount() - 1, 2, QTableWidgetItem(str(row["LastName"])))
                self.setItem(self.rowCount() - 1, 3, QTableWidgetItem(str(row["Name"])))
                self.setItem(self.rowCount() - 1, 4, QTableWidgetItem(str(row["Address1"])))
                self.setItem(self.rowCount() - 1, 5, QTableWidgetItem(str(row["Address2"])))
                self.setItem(self.rowCount() - 1, 6, QTableWidgetItem(str(row["PostCode"])))
                self.setItem(self.rowCount() - 1, 7, QTableWidgetItem(str(row["Country"])))
                self.insertRow(self.rowCount())
            self._removeRow()

    def _addRow(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount)

    def _removeRow(self):
        if self.rowCount() > 0:
            self.removeRow(self.rowCount() - 1)

    def get_selected_row(self):
        # #selected cell value.
        row_info = []
        if self.selectionModel().hasSelection():
            sr = self.currentRow()  # selected row
            for i in range(self.columnCount()):
                row_info.append(self.item(sr, i).text())
        row_info = dict(zip(table_header, row_info))
        print(row_info)
        return row_info


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 600)

        mainLayout = QHBoxLayout()
        table = TableWidget()
        mainLayout.addWidget(table)
        buttonLayout = QVBoxLayout()

        button_reload = QPushButton('Reload')
        button_reload.clicked.connect(table.load_db)
        buttonLayout.addWidget(button_reload)

        # button_copy = QPushButton('Copy')
        # button_copy.clicked.connect(table._copyRow)
        # buttonLayout.addWidget(button_copy)

        button_select = QPushButton('Select')
        button_select.clicked.connect(table.get_selected_row)
        # buttonLayout.addWidget(button_remove, alignment=Qt.AlignTop)
        buttonLayout.addWidget(button_select)

        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)


app = QApplication(sys.argv)
app.setStyleSheet('QPushButton{font-size: 20px; width: 200px; height: 50px}')
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
