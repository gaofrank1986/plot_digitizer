import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

class App(QWidget):
    numpoints =0
    top_val = 0
    top_val_conc = 0

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 input dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.getInteger()
        #self.getText()
        self.getDouble()
        self.getDouble2()
        #self.getChoice()

        self.show()

    def getInteger(self):
        global numpoints
        i, okPressed = QInputDialog.getInt(self, "Get No. of data points","Data points:", 4, 0, 1000, 1)
        if okPressed:
            numpoints = i

    def getNumpoints(self):
        return numpoints

    def getDouble(self):
        global top_val
        d, okPressed = QInputDialog.getDouble(self, "Top value viability","Top value:", 1, 0, 1000, .1)
        if okPressed:
            top_val = d

    def getTopVal(self):
        return top_val

    def getDouble2(self):
        global top_val_conc
        e, okPressed = QInputDialog.getDouble(self, "Top value concentration","Value:", 10.50, 0, 1000, 10)
        if okPressed:
            top_val_conc = e
    def getTopValConc(self):
        return top_val_conc

    #def getChoice(self):
    #    items = ("Red","Blue","Green")
    #    item, okPressed = QInputDialog.getItem(self, "Get item","Color:", items, 0, False)
    #    if okPressed and item:
    #        print(item)

    #def getText(self):
    #    text, okPressed = QInputDialog.getText(self, "Get text","Your name:", QLineEdit.Normal, "")
    #    if okPressed and text != '':
    #        print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
