from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QFile, QTextStream
import globalVariables as GB
import subprocess

def loadStyle(filename):
    file = QFile(filename)
    
    if not file.open(QFile.OpenModeFlag.ReadOnly):
        return ""

    stream = QTextStream(file)
    return stream.readAll()

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.coffee = None # variabile che conterrà il subprocess che terrà sveglio il mac

        self.setFixedSize(650, 200)
        self.setWindowTitle(GB._APP_NAME_)

        self.chk_display = QCheckBox(self)
        self.chk_display.setObjectName("chk_display")
        self.chk_display.setStyleSheet(loadStyle("style.css"))
        
        self.lbl_display = QLabel(self)
        self.lbl_display.setText("Keep Display On")
        self.lbl_display.setObjectName("lbl_display")
        self.lbl_display.setStyleSheet(loadStyle("style.css"))
        
        self.btn_activate = QPushButton(self)
        self.btn_activate.setText("Keep Me Awake!")
        self.btn_activate.clicked.connect(self.activateClicked)
        self.btn_activate.setObjectName("btn_activate")
        self.btn_activate.setStyleSheet(loadStyle("style.css"))

        self.btn_deactivate = QPushButton(self)
        self.btn_deactivate.setText("Let Me Sleep!")
        self.btn_deactivate.clicked.connect(self.deactivateClicked)
        self.btn_deactivate.setObjectName("btn_deactivate")
        self.btn_deactivate.setStyleSheet(loadStyle("style.css"))
        self.btn_deactivate.hide()
        
        # ===== LAYOUTS =====
        self.mainVerticalLayout = QVBoxLayout(self)
        
        self.displayLayout = QHBoxLayout()
        self.displayLayout.addWidget(self.chk_display)
        self.displayLayout.addWidget(self.lbl_display)
        self.mainVerticalLayout.addLayout(self.displayLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.btn_activate)
        self.buttonLayout.addWidget(self.btn_deactivate)
        self.mainVerticalLayout.addLayout(self.buttonLayout)

    def activateClicked(self):
        try:
            if not self.coffee:
                if self.chk_display.isChecked():
                    self.coffee = subprocess.Popen(["caffeinate", "-d"])    # l'opzione -d mantiene attivo il display
                else:
                    self.coffee = subprocess.Popen(["caffeinate", "-i"])    # l'opzione -i semplicemente non manda in stop il mac
        except:
            msg = QMessageBox()
            msg.setText("Error!")
            msg.exec()
            return
        
        self.btn_activate.hide()
        self.btn_deactivate.show()
        self.chk_display.setEnabled(False)
        

    def deactivateClicked(self):
        try:
            if self.coffee:
                self.coffee.terminate()
                self.coffee = None
        except:
            msg = QMessageBox()
            msg.setText("Error!")
            msg.exec()
            return

        self.btn_activate.show()
        self.btn_deactivate.hide()
        self.chk_display.setEnabled(True)
        

    def closeEvent(self, event):
        if self.coffee:
            self.coffee.terminate()
        event.accept()