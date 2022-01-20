import sqlite3
from functools import partial
import qdarkstyle
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtUiTools import  QUiLoader


class ContactList(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = []
        loader = QUiLoader()
        self.ui = loader.load("Design.ui")
        self.ui.show()
        self.conn = sqlite3.connect("Contacts.db")
        self.my_cursor = self.conn.cursor()
        self.ui.remove.clicked.connect(partial(self.remove_contact))
        self.ui.remove_all.clicked.connect(partial(self.remove_all_contacts))
        self.ui.add_contact.clicked.connect(partial(self.add_contact))
        self.ui.checkBox.clicked.connect(partial(self.dark_mode))
        self.load_data()


    def load_data(self):
        self.my_cursor.execute("SELECT * FROM Persons")
        self.db = self.my_cursor.fetchall()  
        self.update_table()

    def remove_contact(self):
        selected = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(selected)
        self.my_cursor.execute(f"DELETE FROM Persons WHERE name ='{self.db[selected][1]}';")
        self.conn.commit()
        self.db.pop(selected)

    def remove_all_contacts(self):
        self.ui.tableWidget.setRowCount(0)
        self.db = []
        self.my_cursor.execute(f"DELETE FROM Persons;")
        self.conn.commit()          

    def add_contact(self):
        if self.ui.name.text() != '' or self.ui.family.text() !='' or self.ui.mobile.text() !='' or self.ui.home.text() !='' or self.ui.email.text() !='':
            new_contact = (0,self.ui.name.text(),self.ui.family.text(),self.ui.mobile.text(),self.ui.home.text(),self.ui.email.text())
            self.db.append(new_contact)
            self.my_cursor.execute(f"INSERT INTO Persons (name,family,mobile,home,email)VALUES ('{self.ui.name.text()}', '{self.ui.family.text()}', '{self.ui.mobile.text()}','{self.ui.home.text()}','{self.ui.email.text()}');")
            self.conn.commit()
            self.update_table()
            self.ui.name.setText("")
            self.ui.family.setText("")
            self.ui.mobile.setText("")
            self.ui.home.setText("")
            self.ui.email.setText("")

    def update_table(self):
        self.ui.tableWidget.setColumnCount(5)  
        self.ui.tableWidget.setRowCount(len(self.db))
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSortingEnabled(True)  
        headers = ['Name' , 'Family' , 'Mobile' , 'Home' , 'Email']
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)       

        for i in range(0,len(self.db)):
            for j in range (1,6):             
                self.ui.tableWidget.setItem(i,j-1, QTableWidgetItem(self.db[i][j]))   
    
    def dark_mode(self):
        if self.ui.checkBox.isChecked():
            app.setStyleSheet(qdarkstyle.load_stylesheet())
        else:
            app.setStyleSheet(None)   


app = QApplication()
contacts = ContactList()
app.exec()