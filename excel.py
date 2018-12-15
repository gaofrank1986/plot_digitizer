import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
import xlsxwriter
class App_excel(QWidget):
    name_excel = []

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
        self.getText()
        self.show()

    def getText(self):
        global name_excel
        text, okPressed = QInputDialog.getText(self, "Excel name","Enter excelsheet name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            name_excel = text
        else:
            name_excel = 'change_name'
            #workbook = xlsxwriter.Workbook('{}.xlsx'.format(name_excel))
            #worksheet = workbook.add_worksheet()
            #print('created excel sheet')


    def getExcel(self):
        return name_excel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App_excel()
    sys.exit(app.exec_())
