from PyQt5 import QtCore, QtGui, QtWidgets

from input_dialog2 import App
from excel import App_excel
from check_dict import AppDictionary
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import xlsxwriter
import pyexcel as p
import argparse

import cv2

import pyscreenshot as ImageGrab


coords = []
calib =[]
values =[]
values_log = []
values_con = []
topvalue = 0
name_excel = []
choice_ = [""]

topvalue_conc = 0
Data_graph = {}
iii = 0
numpoints = 1

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(181, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 141, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 130, 141, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 30, 141, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 280, 141, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 230, 141, 25))
        self.pushButton_5.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.printMessage)
        self.pushButton_2.clicked.connect(self.click_crop)
        self.pushButton_3.clicked.connect(self.excel)
        self.pushButton_4.clicked.connect(self.printStatus)
        self.pushButton_5.clicked.connect(self.printDictionary)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plot Digitizer"))
        self.pushButton.setText(_translate("MainWindow", "Input Data"))
        self.pushButton_2.setText(_translate("MainWindow", "Crop image"))
        self.pushButton_3.setText(_translate("MainWindow", "Create Excel"))
        self.pushButton_4.setText(_translate("MainWindow", "Check Input data"))
        self.pushButton_5.setText(_translate("MainWindow", "Check Dictionary"))

    def excel(self):

        global name_excel
        app_2 = App_excel()
        name_excel = app_2.getExcel()
        workbook = xlsxwriter.Workbook('{}.xlsx'.format(name_excel))
        worksheet = workbook.add_worksheet()
        print('Created excel sheet: {}.xlsx'.format(name_excel))

    def printDictionary(self):
        #global choice_
        #print(choice_)

        app_3 = AppDictionary(items=choice_)

        if (choice_ != [""]):
            single_choice = app_3.getChoiceValue()

            if single_choice != [""]:

                print("\n")
                print("\n")
                print("****************************************************************************")
                print("****************************************************************************")
                print("Graph Number: {}".format(single_choice))
                print("\n")
                print('Log x value: {}'.format(Data_graph['Data_{}'.format(int(single_choice))][0]))
                print('X value:     {}'.format(Data_graph['Data_{}'.format(int(single_choice))][1]))
                print('Y Value:     {}'.format(Data_graph['Data_{}'.format(int(single_choice))][2]))
                print("\n")
                print("****************************************************************************")
                print("****************************************************************************")

    def printMessage(self):
        app_ = App()
        global topvalue
        global topvalue_conc
        global numpoints
        topvalue = app_.getTopVal()
        print("\n")
        print("\n")
        print("****************************************************************************")
        print("****************************************************************************")
        print("Y axis top value:   {}".format(topvalue))
        topvalue_conc = app_.getTopValConc()
        print("X axis top value:   {}".format(topvalue_conc))
        numpoints = app_.getNumpoints()
        print("No. of data points: {}".format(numpoints))
        print("****************************************************************************")
        print("****************************************************************************")


    def printStatus(self):
        print("\n")
        print("****************************************************************************")
        print("****************************************************************************")
        print("\n")
        print('Current top Y value:             {}'.format(topvalue))
        print('Current top X value :            {}'.format(topvalue_conc))
        print('Current number of data inputs:   {}'.format(numpoints))
        print('Current excel sheet:             {}.xlsx'.format(name_excel))
        print("\n")
        print("****************************************************************************")
        print("****************************************************************************")
        #print('current iii:{}'.format(iii))
        #print('current coords: {}'.format(coords))

    def click_crop(self,event):
        global coords
        global calib
        global values
        global values_log
        global values_conc

        values =[]
        values_log = []
        values_con = []
        calib =[]
        coords = []


        im = ImageGrab.grab()
        im.save('screenshot224.jpg')
        print ("Saved image!")
        global choice_
        global iii
        iii+=1
        choice_.append('{}'.format(iii))

        def click_and_crop(event, x, y, flags, param):
            # grab references to the global variables
            global refPt, cropping

            # if the left mouse button was clicked, record the starting
            # (x, y) coordinates and indicate that cropping is being
            # performed
            if event == cv2.EVENT_LBUTTONDOWN:
                refPt = [(x, y)]
                cropping = True

            # check to see if the left mouse button was released
            elif event == cv2.EVENT_LBUTTONUP:
                # record the ending (x, y) coordinates and indicate that
                # the cropping operation is finished
                refPt.append((x, y))
                cropping = False

                # draw a rectangle around the region of interest
                cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
                cv2.imshow("image", image)

        #m = ImageGrab.grab()
        #m.save('screenshot224.jpg')
        #rint ("Saved image!")
        #
        image = cv2.imread('screenshot224.jpg')
        print('image is gotten')
        clone = image.copy()
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", click_and_crop)

        # keep looping until the 'q' key is pressed
        while True:
            # display the image and wait for a keypress
            cv2.imshow("image", image)
            key = cv2.waitKey(1) & 0xFF

            # if the 'r' key is pressed, reset the cropping region
            if key == ord("r"):
                image = clone.copy()

            # if the 'c' key is pressed, break from the loop
            elif key == ord("c"):
                break

        # if there are two reference points, then crop the region of interest
        # from teh image and display it


        if len(refPt) == 2:
            roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
            #cv2.imshow("ROI", roi)
            cv2.imwrite("roi.jpg",roi)
            cv2.waitKey(0)

            img = mpimg.imread("roi.jpg")
            fig = plt.figure()
            plt.imshow(img)



            def onclick(event):

                global calib
                global coords
                global ix, iy


                ix, iy = event.xdata, event.ydata
                #y1cal,y2cal = event.y1caldata,event.y2caldata
                print('x = %d, y = %d'%(ix, iy))
                if len(coords)<4:
                    plt.scatter(event.xdata, event.ydata, s=70,marker="X",color='white',edgecolor='black')
                    fig.canvas.draw()
                else:
                    plt.scatter(event.xdata, event.ydata, s=50,marker="x",color='r')
                    fig.canvas.draw()


                #global calib
                #global coords


                if len(coords) < 4: #because you have to indicate first 2 points for y axis and 2 for the x axis
                    calib.append((ix,iy))


                coords.append((ix, iy))

                if len(coords) == numpoints +4:
                    for i in range(0,len(coords)-4):
                        distance = np.abs(calib[0][1]-calib[1][1])
                        distance_conc = np.abs(calib[2][0]-calib[3][0])
                        values.append((topvalue/distance) * (np.abs(coords[i+4][1]-calib[0][1])))
                        values_log.append(10**(((np.log10(topvalue_conc))/distance_conc) * (np.abs(coords[i+4][0] - calib[2][0]))))
                        values_con.append((topvalue_conc/distance_conc) * (np.abs(coords[i+4][0] - calib[2][0])))
                    #print(distance_conc)
                    #print(np.abs(coords[i+4][0] - calib[2][0]))
                    print("****************************************************************************")
                    print("****************************************************************************")
                    print("Extracted Data")
                    print("\n")
                    print('Log x value: {}'.format(values_log))
                    print('X value:     {}'.format(values_con))
                    print('Y Value:     {}'.format(values))
                    print("\n")
                    print("****************************************************************************")
                    print("****************************************************************************")

                    #print(topvalue_conc)
                    #print(values_log)
                    #print(values_con)
                    #print(values)
                    #print(calib)
                    fig.canvas.mpl_disconnect(cid)


                    Data_graph['Data_{}'.format(iii)]= [values_log,values_con,values]
                    p.save_book_as(bookdict=Data_graph, dest_file_name="{}.xlsx".format(name_excel))
                    #p.save_as(array = Data_graph, dest_file_name = 'demo2.xlsx')


                #if len(coords) >= 2:
                    #values.append(coords)
                #if len(calib)>=2:

                    #for i in range(0,len(coords)-2):
                        #distance = np.abs(calib[0][1]-calib[1][1])
                        #values.append((0.25/distance) * (np.abs(coords[i+2][1]-calib[0][1])))

                return coords
                return values
                return values_con

                #global Data_graph
                #Data_graph = [values_con,values]

                #p.save_as(array = Data_graph, dest_file_name = 'demo2.xlsx')

            #print(values)
            cid = fig.canvas.mpl_connect('button_press_event', onclick)
            #print(values)



            plt.axis('off')
            plt.show()


        # close all open windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
