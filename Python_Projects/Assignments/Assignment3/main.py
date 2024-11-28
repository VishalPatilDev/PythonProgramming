import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction, QLabel

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Menu Example")
        self.setGeometry(300, 300, 400, 200)

        self.init_ui()

    def init_ui(self):
        # Create a menu bar
        menubar = self.menuBar()

        # Create two menus
        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Edit')

        # Create actions for the "File" menu
        new_action = QAction('New', self)
        new_action.triggered.connect(self.show_message("New File Created!"))
        file_menu.addAction(new_action)

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.show_message("File Opened!"))
        file_menu.addAction(open_action)

        # Add a separator between actions in the "File" menu
        file_menu.addSeparator()

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Create actions for the "Edit" menu
        cut_action = QAction('Cut', self)
        cut_action.triggered.connect(self.show_message("Text Cut!"))
        edit_menu.addAction(cut_action)

        copy_action = QAction('Copy', self)
        copy_action.triggered.connect(self.show_message("Text Copied!"))
        edit_menu.addAction(copy_action)

        paste_action = QAction('Paste', self)
        paste_action.triggered.connect(self.show_message("Text Pasted!"))
        edit_menu.addAction(paste_action)

    def show_message(self, message):
        # Function to display messages in a QLabel
        label = QLabel(message, self)
        self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())
