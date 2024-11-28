import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Button Example")
        self.setGeometry(300, 300, 400, 200)

        self.init_ui()

    def init_ui(self):
        # Create a QVBoxLayout for the main layout
        layout = QVBoxLayout(self)

        # Create a QLabel with initial text
        self.label = QLabel("Click the button", self)

        # Create a QPushButton
        button = QPushButton("Click Me!", self)
        button.clicked.connect(self.on_button_click)  # Connect the button click event to a method

        # Add the QLabel and QPushButton to the layout
        layout.addWidget(self.label)
        layout.addWidget(button)

        # Set the main layout for the window
        self.setLayout(layout)

    def on_button_click(self):
        # Change the text of the QLabel when the button is clicked
        self.label.setText("Button Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
