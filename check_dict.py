import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

class AppDictionary(QWidget):
    choice_2=[]

    def __init__(self,items =['4','5''89']):
        super().__init__()
        self.items = items
        self.title = 'PyQt5 input dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.getChoice()

        self.show()


    def getChoice(self):
        global choice_2
        #items = ("1","2","3")
        item, okPressed = QInputDialog.getItem(self, "Get Dictionary","Dictionary:", self.items, 0, False)
        if okPressed and item:
            choice_2 = item
            #print(choice_2)

    def getChoiceValue(self):
        return choice_2



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
