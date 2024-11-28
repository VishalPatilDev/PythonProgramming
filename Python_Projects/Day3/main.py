import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create a QLabel with the text "Hello, PyQt!"
        label = QLabel("Hello, PyQt!", self)
        label.setAlignment(Qt.AlignCenter)  # Align text to the center

        # Add the QLabel to the layout
        layout.addWidget(label)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

        # Set the main window properties
        self.setWindowTitle("PyQt Hello World")
        self.setGeometry(100, 100, 400, 200)  # Set window position and size

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())
