import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFileDialog, QCheckBox
from PyQt5.QtGui import QIcon

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app = QApplication(sys.argv)


window = QWidget()
window.setWindowTitle('EASY FASTBOOT FLASHER')
window.setWindowIcon(QIcon(resource_path("image.png")))
window.setGeometry(400, 400, 300, 500)


label = QLabel('𝙀𝘼𝙎𝙔 𝙁𝘼𝙎𝙏𝘽𝙊𝙊𝙏 𝙁𝙇𝘼𝙎𝙃𝙀𝙍')
label.setStyleSheet('font-size: 20pt;')
label2 = QLabel('v0.5.1 (alpha)')
button = QPushButton('Start')
stage_1 = QLabel('1. Load system image')
stage_1.setStyleSheet('font-size: 14pt;')
stage_2 = QLabel('2. Advanced')
stage_2.setStyleSheet('font-size: 14pt;')
checkbox_avb_remove = QCheckBox('Disable AVB verification')
checkbox_factory_reset = QCheckBox('Perform factory reset')
stage_3 = QLabel('3. Start')
stage_3.setStyleSheet('font-size: 14pt;')
file_button = QPushButton('Select file...')
file_label = QLineEdit()
file_label.setFixedSize(300, 20)
label_debug = QLabel('')     

checkbox_avb_remove.setEnabled(False)

def on_file_button_clicked():
    filename, _ = QFileDialog.getOpenFileName(None, 'Select file...', '.', 'Android system image (*.img)') # открываем диалоговое окно выбора файла
    file_label.setText(filename)
    return filename

def on_button_clicked(filename):
    filename = file_label.text()
    button.setText('Processing... (see console for more info)')
    button.setEnabled(False)
    file_button.setEnabled(False)
    file_label.setEnabled(False)
    checkbox_factory_reset.setEnabled(False)
    app.processEvents()
    os.system('cls')
    os.system('cd '+resource_path("platform-tools")+' && fastboot erase system && fastboot flash system {}'.format(filename))
    if checkbox_factory_reset.isChecked():
        os.system('cd '+resource_path("platform-tools")+' && fastboot -w')
    os.system('cd '+resource_path("platform-tools")+' && fastboot reboot')
    button.setText('Done!')
    button.setEnabled(True)
    file_button.setEnabled(True)
    file_label.setEnabled(True)
    checkbox_factory_reset.setEnabled(True)
    app.processEvents()
        

button.clicked.connect(on_button_clicked)
file_button.clicked.connect(on_file_button_clicked)


layout = QVBoxLayout()

layout.addWidget(label)
layout.addWidget(label2)
layout.addWidget(stage_1)
layout.addWidget(file_button)
layout.addWidget(file_label)
layout.addWidget(stage_2)
layout.addWidget(checkbox_avb_remove)
layout.addWidget(checkbox_factory_reset)
layout.addWidget(stage_3)
layout.addWidget(button)

layout.setAlignment(label, QtCore.Qt.AlignCenter)
layout.setAlignment(label2, QtCore.Qt.AlignCenter)
layout.setAlignment(stage_1, QtCore.Qt.AlignCenter)
layout.setAlignment(stage_2, QtCore.Qt.AlignCenter)
layout.setAlignment(checkbox_avb_remove, QtCore.Qt.AlignCenter)
layout.setAlignment(checkbox_factory_reset, QtCore.Qt.AlignCenter)
layout.setAlignment(stage_3, QtCore.Qt.AlignCenter)
layout.setAlignment(file_button, QtCore.Qt.AlignCenter)
layout.setAlignment(file_label, QtCore.Qt.AlignCenter)
layout.setAlignment(button, QtCore.Qt.AlignCenter)


window.setLayout(layout)


window.show()
sys.exit(app.exec_())
