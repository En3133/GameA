import sys
from PyQt5.QtWidgets import QApplication, QtWidgets, Qlabel

class Scene(QtWidget):
   def __init__(self, x=600, y=400, speed=30, title="My Game"):
    super().__init__()

  self.setGeometry(50,50, x, y);