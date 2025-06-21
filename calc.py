from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(300, 400)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
            }
            QLineEdit {
                background-color: #3d3d3d;
                color: white;
                border: none;
                padding: 15px;
                font-size: 24px;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #4d4d4d;
                color: white;
                border: none;
                font-size: 18px;
                border-radius: 5px;
                padding: 15px;
            }
            QPushButton:hover {
                background-color: #5d5d5d;
            }
            QPushButton:pressed {
                background-color: #3d3d3d;
            }
            QPushButton#equals {
                background-color: #ff9500;
            }
            QPushButton#equals:hover {
                background-color: #ffaa33;
            }
            QPushButton#equals:pressed {
                background-color: #cc7700;
            }
            QPushButton#clear {
                background-color: #ff3b30;
            }
            QPushButton#clear:hover {
                background-color: #ff5e54;
            }
            QPushButton#clear:pressed {
                background-color: #cc2c24;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

        buttons_layout = QGridLayout()

        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
            ("C", 4, 0, 1, 4)
        ]

        for btn_text, row, col, *span in buttons:
            button = QPushButton(btn_text)
            if btn_text == "=":
                button.setObjectName("equals")
                button.clicked.connect(self.calculate)
            elif btn_text == "C":
                button.setObjectName("clear")
                button.clicked.connect(self.clear)
                buttons_layout.addWidget(button, row, col, 1, 4)
                continue
            else:
                button.clicked.connect(lambda _, x=btn_text: self.append_to_display(x))
            buttons_layout.addWidget(button, row, col, *span)

        layout.addLayout(buttons_layout)

    def append_to_display(self, text):
        self.display.setText(self.display.text() + text)

    def calculate(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except:
            self.display.setText("Ошибка")

    def clear(self):
        self.display.clear()

if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()
