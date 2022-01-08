from PyQt5.QtWidgets import (
    QWidget, QTabWidget
)
from PyQt5.QtCore import(
    Qt, QRect
)

import appfiles.utils.assets as assets
from appfiles.utils.constants import *


class window(QWidget):
    def __init__(self, logger, plugins):
        QWidget.__init__(self)

        self.logger = logger

        self.plugins = plugins

        self.init()
        self.initUi()
        self.setupPlugins()

    def init(self):
        # Inits the basic window
        # self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint)
        self.setFixedSize(WINDOW_SIZE[0], WINDOW_SIZE[1])
        self.setWindowTitle(WINDOW_TITLE)
        self.move(int((1920 / 2) - (WINDOW_SIZE[0] / 2)),
                  int((1080/2) - (WINDOW_SIZE[1] / 2)))

        self.clicked = False

    def initUi(self):
        # inits the window items
        # # add a quit button ?

        self.tab_widget = QTabWidget(self)
        self.tab_widget.setObjectName("tabWidget")
        self.tab_widget.tabBar().setObjectName("Window_TabWidget_TabBar")
        self.tab_widget.setGeometry(
            QRect(0, 0, WINDOW_SIZE[0], WINDOW_SIZE[1]))  # dragable top border as y value
        # self.tab_widget.addTab(QWidget(), "test")
        pass

    def setupPlugins(self):
        # Adding the ui part of the modules to the window
        for plugin in self.plugins:
            widget, title = plugin.get_ui()
            self.tab_widget.addTab(widget, title)

        pass

    def mousePressEvent(self, event):
        self.clicked = True
        self.old_pos = event.screenPos()

    def mouseReleaseEvent(self, event):
        self.clicked = False

    def mouseMoveEvent(self, event):
        if self.clicked:
            dx = self.old_pos.x() - event.screenPos().x()
            dy = self.old_pos.y() - event.screenPos().y()
            self.move(int(self.pos().x() - dx), int(self.pos().y() - dy))

        self.old_pos = event.screenPos()
        # self.clicked = True
        return QWidget.mouseMoveEvent(self, event)
