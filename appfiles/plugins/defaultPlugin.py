from PyQt5.QtWidgets import (
    QWidget, QPushButton
)
from PyQt5.QtCore import(
    Qt, QRect
)


class plugin:
    def __init__(self, logger):
        self.logger = logger
        self.logger.debug("Default plugin init")

    def get_ui(self):
        widget = QWidget()
        title = "Default ui"

        button = QPushButton("Press to say hi", widget)
        button.setGeometry(QRect(0, 0, 100, 50))
        button.clicked.connect(lambda: self.logger.debug("Hi! "))

        return widget, title

    def ping(self):
        return "I'm up"
