import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot	

app = QApplication(sys.argv)

window = QWidget()

window.setGeomerty(50, 50, 320, 200)
window.setWindowTitle("PyQt5 Example")

# ian's label
LabelIan = QLabel(window)
LabelIan.setText("Spiderman")
LabelIan.move(110,85)

# amy's lable
LableAmy = QLabel(window)
LableAmy.setText("Ironman")
LableAmy.move(20,35)

#iris' label
LabelIris = QLabel(window)
LabelIris.setText("Hulk")
LabelIris.move(140,50)

#tyrone's Lable
LableTyrone = QLabel(window)
LableTyrone.setText("Venom")
LableTyrone.move(100,80)



window.show()

sys.exit(app.exec_())