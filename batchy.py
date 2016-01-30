from views.mainwindow_handler import *


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindowClass()
    mainWindow.show()
    app.exec_()
