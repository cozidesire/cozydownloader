import sys
from PySide6.QtWidgets import QApplication
from controlroom.maincontroller import MainController


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("Cozydownloader")
    app.setApplicationName("Cozydownloader")

    window = MainController()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()