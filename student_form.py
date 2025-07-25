# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentForm(object):
    def setupUi(self, StudentForm):
        StudentForm.setObjectName("StudentForm")
        StudentForm.resize(800, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(StudentForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QHBoxLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLayout = QtWidgets.QVBoxLayout()
        self.nameLayout.setObjectName("nameLayout")
        self.labelName = QtWidgets.QLabel(StudentForm)
        self.labelName.setObjectName("labelName")
        self.nameLayout.addWidget(self.labelName)
        self.lineEditName = QtWidgets.QLineEdit(StudentForm)
        self.lineEditName.setObjectName("lineEditName")
        self.nameLayout.addWidget(self.lineEditName)
        self.formLayout.addLayout(self.nameLayout)
        self.rollLayout = QtWidgets.QVBoxLayout()
        self.rollLayout.setObjectName("rollLayout")
        self.labelRoll = QtWidgets.QLabel(StudentForm)
        self.labelRoll.setObjectName("labelRoll")
        self.rollLayout.addWidget(self.labelRoll)
        self.lineEditRoll = QtWidgets.QLineEdit(StudentForm)
        self.lineEditRoll.setObjectName("lineEditRoll")
        self.rollLayout.addWidget(self.lineEditRoll)
        self.formLayout.addLayout(self.rollLayout)
        self.branchLayout = QtWidgets.QVBoxLayout()
        self.branchLayout.setObjectName("branchLayout")
        self.labelBranch = QtWidgets.QLabel(StudentForm)
        self.labelBranch.setObjectName("labelBranch")
        self.branchLayout.addWidget(self.labelBranch)
        self.lineEditBranch = QtWidgets.QLineEdit(StudentForm)
        self.lineEditBranch.setObjectName("lineEditBranch")
        self.branchLayout.addWidget(self.lineEditBranch)
        self.formLayout.addLayout(self.branchLayout)
        self.phoneLayout = QtWidgets.QVBoxLayout()
        self.phoneLayout.setObjectName("phoneLayout")
        self.labelPhone = QtWidgets.QLabel(StudentForm)
        self.labelPhone.setObjectName("labelPhone")
        self.phoneLayout.addWidget(self.labelPhone)
        self.lineEditPhone = QtWidgets.QLineEdit(StudentForm)
        self.lineEditPhone.setObjectName("lineEditPhone")
        self.phoneLayout.addWidget(self.lineEditPhone)
        self.formLayout.addLayout(self.phoneLayout)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.btnAdd = QtWidgets.QPushButton(StudentForm)
        self.btnAdd.setObjectName("btnAdd")
        self.buttonLayout.addWidget(self.btnAdd)
        self.btnUpdate = QtWidgets.QPushButton(StudentForm)
        self.btnUpdate.setObjectName("btnUpdate")
        self.buttonLayout.addWidget(self.btnUpdate)
        self.btnDelete = QtWidgets.QPushButton(StudentForm)
        self.btnDelete.setObjectName("btnDelete")
        self.buttonLayout.addWidget(self.btnDelete)
        self.btnClear = QtWidgets.QPushButton(StudentForm)
        self.btnClear.setObjectName("btnClear")
        self.buttonLayout.addWidget(self.btnClear)
        self.verticalLayout.addLayout(self.buttonLayout)
        self.tableStudents = QtWidgets.QTableWidget(StudentForm)
        self.tableStudents.setObjectName("tableStudents")
        self.tableStudents.setColumnCount(5)
        self.tableStudents.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableStudents.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStudents.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStudents.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStudents.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStudents.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableStudents)

        self.retranslateUi(StudentForm)
        QtCore.QMetaObject.connectSlotsByName(StudentForm)

    def retranslateUi(self, StudentForm):
        _translate = QtCore.QCoreApplication.translate
        StudentForm.setWindowTitle(_translate("StudentForm", "Student Record Management"))
        self.labelName.setText(_translate("StudentForm", "Name"))
        self.labelRoll.setText(_translate("StudentForm", "Roll No"))
        self.labelBranch.setText(_translate("StudentForm", "Branch"))
        self.labelPhone.setText(_translate("StudentForm", "Phone"))
        self.btnAdd.setText(_translate("StudentForm", "Add"))
        self.btnUpdate.setText(_translate("StudentForm", "Update"))
        self.btnDelete.setText(_translate("StudentForm", "Delete"))
        self.btnClear.setText(_translate("StudentForm", "Clear"))
        item = self.tableStudents.horizontalHeaderItem(0)
        item.setText(_translate("StudentForm", "ID"))
        item = self.tableStudents.horizontalHeaderItem(1)
        item.setText(_translate("StudentForm", "Name"))
        item = self.tableStudents.horizontalHeaderItem(2)
        item.setText(_translate("StudentForm", "Roll No"))
        item = self.tableStudents.horizontalHeaderItem(3)
        item.setText(_translate("StudentForm", "Branch"))
        item = self.tableStudents.horizontalHeaderItem(4)
        item.setText(_translate("StudentForm", "Phone"))
