import sys
import socket
from threading import Thread

from PyQt6.QtWidgets import QApplication, QDialog

from layout import Ui_Dialog


class Window(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.exec()
	sys.exit(app.exec())