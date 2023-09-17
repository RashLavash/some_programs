import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic




class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/registration_form.ui', self)

        self.button_save_user.clicked.connect(self.run_button)

    def save_info():
        pass

    


    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    m_widget = MyWidget()
    m_widget.show()
    sys.exit(app.exec_())