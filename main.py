import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMessageBox, QTableWidgetItem
)
from student_form import Ui_StudentForm
from Student_db import fetch_students, insert_student, update_student, delete_student

class StudentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StudentForm()
        self.ui.setupUi(self)
        self.selected_id = None

        self.ui.btnAdd.clicked.connect(self.add_record)
        self.ui.btnUpdate.clicked.connect(self.update_record)
        self.ui.btnDelete.clicked.connect(self.delete_record)
        self.ui.btnClear.clicked.connect(self.clear_form)
        self.ui.tableStudents.cellClicked.connect(self.load_record)

        self.load_data()

    def load_data(self):
        records = fetch_students()
        self.ui.tableStudents.setRowCount(len(records))
        self.ui.tableStudents.setColumnCount(5)
        self.ui.tableStudents.setHorizontalHeaderLabels(["ID", "Name", "Roll No", "Branch", "Phone"])

        for row, record in enumerate(records):
            for col, value in enumerate(record):
                self.ui.tableStudents.setItem(row, col, QTableWidgetItem(str(value)))

    def clear_form(self):
        self.selected_id = None
        self.ui.lineEditName.clear()
        self.ui.lineEditRoll.clear()
        self.ui.lineEditBranch.clear()
        self.ui.lineEditPhone.clear()

    def load_record(self, row, _):
        self.selected_id = int(self.ui.tableStudents.item(row, 0).text())
        self.ui.lineEditName.setText(self.ui.tableStudents.item(row, 1).text())
        self.ui.lineEditRoll.setText(self.ui.tableStudents.item(row, 2).text())
        self.ui.lineEditBranch.setText(self.ui.tableStudents.item(row, 3).text())
        self.ui.lineEditPhone.setText(self.ui.tableStudents.item(row, 4).text())

    def add_record(self):
        name = self.ui.lineEditName.text()
        roll = self.ui.lineEditRoll.text()
        branch = self.ui.lineEditBranch.text()
        phone = self.ui.lineEditPhone.text()

        if name and roll:
            insert_student(name, roll, branch, phone)
            self.load_data()
            self.clear_form()
        else:
            QMessageBox.warning(self, "Input Error", "Name and Roll No are required.")

    def update_record(self):
        if self.selected_id:
            update_student(
                self.selected_id,
                self.ui.lineEditName.text(),
                self.ui.lineEditRoll.text(),
                self.ui.lineEditBranch.text(),
                self.ui.lineEditPhone.text()
            )
            self.load_data()
            self.clear_form()
        else:
            QMessageBox.warning(self, "No Record", "Please select a record to update.")

    def delete_record(self):
                if self.selected_id:
                    delete_student(self.selected_id)
                    self.load_data()
                    self.clear_form()
                else:
                    QMessageBox.warning(self, "No Record", "Please select a record to delete.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentApp()
    window.show()
    sys.exit(app.exec_())
