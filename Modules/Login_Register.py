from PyQt5 import uic
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys
import os

from PyQt5.QtWidgets import QMessageBox

sys.path.append("..")
from Modules import *

class Login_Register_Window(qtw.QMainWindow):
    """
    class which contains Login Page and Register Page forms
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if getattr(sys, 'frozen', False):
            ui_path = os.path.dirname(sys.executable) + "/Gui/Login_RegisterForms.ui"
        elif __file__:
            ui_path = os.path.dirname((os.path.dirname(os.path.abspath(__file__))) )+ "/Gui/Login_RegisterForms.ui"
        self.ui = uic.loadUi(ui_path, self)
        self.setWindowFlags(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.Center()
        self.ui.stackedWidget.setCurrentIndex(0)

        #Login page command connect
        self.ui.btn_close.clicked.connect(self.Exit_command)
        self.ui.btn_minimise.clicked.connect(self.showMinimized)
        self.ui.RegisterBtn.clicked.connect(self.Register_command)

        #register page command connect
        self.ui.btn_close_2.clicked.connect(self.Exit_command)
        self.ui.btn_minimise_2.clicked.connect(self.showMinimized)
        self.ui.RegisterBtn_2.clicked.connect(self.RegisterNewUser_command)
        self.ui.CancelBtn.clicked.connect(self.Cancel_command)

    def Center(self):
        """
        function to center the entire gui at the center of your screen.
        """
        qr = self.frameGeometry()
        cp = qtw.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def RegisterNewUser_command(self):
        """
            function to register a new user to the system checks if user exists or not if not creats a new one
            else gives a massage according to the problem.
        """
        user_id = self.ui.IdLineEdit_2.text()
        user_name = self.ui.UserNameLineEdit_2.text()
        password1 = self.ui.PassLineEdit_2.text()
        password2 = self.ui.ConfirmPassLineEdit.text()
        full_name = self.ui.FullNameLineEdit.text()

        if(CheckRegistrationDetails(user_id, user_name, password1, password2,full_name)):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Registered Succefully")
            msg.setWindowTitle("Registered Succefully")
            msg.exec_()
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.UserNameLineEdit.clear()
            self.ui.IdLineEdit.clear()
            self.ui.PassLineEdit.clear()

    def Cancel_command(self):
        """
        a function to return to login page from register page with registaring a new user.
        """
        self.ui.UserNameLineEdit.clear()
        self.ui.IdLineEdit.clear()
        self.ui.PassLineEdit.clear()
        self.ui.stackedWidget.setCurrentIndex(0)


    def Exit_command(self):
        """
            closes the system completly upon pressing the x button.
        """
        self.close()


    def Register_command(self):
        """
            function to move from login page to register page.
        """
        self.RegisterPageClean()
        self.ui.stackedWidget.setCurrentIndex(1)


    def RegisterPageClean(self):
        """
        a function to clean all the fields in the register page.
        """
        self.ui.FullNameLineEdit.clear()
        self.ui.UserNameLineEdit_2.clear()
        self.ui.IdLineEdit_2.clear()
        self.ui.PassLineEdit_2.clear()
        self.ui.ConfirmPassLineEdit.clear()




if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    UiWindow = Login_Register_Window()
    UiWindow.show()
    app.exec_()