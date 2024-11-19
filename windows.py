from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QRadioButton, QButtonGroup

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('My first app')
my_win.move(900, 70)
my_win.resize(400, 200)
my_win.show()

line = QVBoxLayout()

radio_button_1 = QRadioButton('1')
radio_button_1.setChecked(True)
radio_button_2 = QRadioButton('2')
radio_button_3 = QRadioButton('3')

button_group = QButtonGroup()
button_group.addButton(radio_button_1, id=1)
button_group.addButton(radio_button_2, id=2)
button_group.addButton(radio_button_3, id=3)

line.addWidget(radio_button_1)
line.addWidget(radio_button_2)
line.addWidget(radio_button_3)

button = QPushButton('Check')
line.addWidget(button, alignment=Qt.AlignCenter)

title = QLabel()
line.addWidget(title, alignment=Qt.AlignCenter)
my_win.setLayout(line)

def radio_button_check():
    title.setText("Selected: button number " + str(button_group.checkedId()))

button.clicked.connect(radio_button_check)

app.exec_()