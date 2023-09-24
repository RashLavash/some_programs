import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5 .QtCore import QDate

import datetime




class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/registration_form.ui', self)

        self.con = sqlite3.connect('db/users.db')
        self.cursor = self.con.cursor()

        self.context = {}
        self.current_date = datetime.datetime.now()
        self.button_save_user.clicked.connect(self.save_info)
        self.button_clean.clicked.connect(self.reset_fields)

    def create_users_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_fio TEXT,
                user_bio TEXT,
                user_edq TEXT,
                user_birth TEXT,
                user_reg_date TEXT               
            );

        ''')
        self.con.commit()

    def save_info(self):
        self.create_users_table()
        self.get_data()
        self.save_to_db()
        self.button_save_user.setText('Пользователь сохранен')
        self.button_save_user.setStyleSheet("background-color: green")


    def get_data(self):
        self.context = {
            'user_fio': self.user_fio.text(),
            'user_bio': self.user_bio.toPlainText(),
            'user_edq': self.user_edq.currentText(),
            'user_birth': self.user_birth.dateTime().toString('dd.MM.yyyy'),
            'user_reg_date': self.current_date.strftime('%d.%m.%Y %H:%M:%S')
        }

    def save_to_db(self):
        query = (''' 
            INSERT INTO users(
                 user_fio, 
                 user_bio,
                 user_edq,
                 user_birth,
                 user_reg_date
            )
            VALUES(?, ?, ?, ?, ?);
        ''')
        user_data = (
            self.context['user_fio'],
            self.context['user_bio'],
            self.context['user_edq'],
            self.context['user_birth'],
            self.context['user_reg_date']
        )
        self.cursor.execute(query, user_data)
        self.con.commit()

    def reset_fields(self):
        self.user_fio.clear()
        self.user_bio.clear()
        self.user_edq.setCurrentIndex(0)
        self.user_birth.setDate(QDate.fromString('01.01.2000', 'dd.MM.yyyy'))
        self.button_save_user.setText('Сохранить пользователя')
        self.button_save_user.setStyleSheet("background-color: white")

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    m_widget = MyWidget()
    m_widget.show()
    sys.exit(app.exec_())