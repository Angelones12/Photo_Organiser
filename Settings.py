import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QTextEdit, QPushButton, QDialog, QLabel, QLineEdit, QDialogButtonBox
from PyQt5.QtCore import Qt

class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ustawienia")
        self.setGeometry(100, 100, 300, 150)

        # Tworzymy layout w oknie ustawień
        layout = QVBoxLayout()

        # Dodajemy etykiety i pola do wpisania
        self.label = QLabel("Nazwa użytkownika:")
        self.username_input = QLineEdit()

        # Tworzymy przyciski zatwierdzenia i anulowania
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        layout.addWidget(self.label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.button_box)

        self.setLayout(layout)