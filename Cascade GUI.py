from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtGui import QIcon
import pandas as pd
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(QtWidgets.QWidget):
	
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(1143, 829)
        Form.setMaximumSize(QtCore.QSize(1143, 829))
        Form.setWindowIcon(QtGui.QIcon("./icon.png"))
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1121, 811))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.openF = QtWidgets.QPushButton(self.formLayoutWidget)
        self.openF.setObjectName("openF")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.openF)
        self.tabWidget = QtWidgets.QTabWidget(self.formLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 41))
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(110, 20, 51, 21))
        self.spinBox.setObjectName("spinBox")
        self.show_kn = QtWidgets.QPushButton(self.tab)
        self.show_kn.setGeometry(QtCore.QRect(180, 20, 93, 21))
        self.show_kn.setObjectName("show_kn")
        self.table = QtWidgets.QTableWidget(self.tab)
        self.table.setGeometry(QtCore.QRect(10, 60, 1091, 631))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.Camera = QtWidgets.QPushButton(self.tab)
        self.Camera.setGeometry(QtCore.QRect(20, 710, 93, 28))
        self.Camera.setObjectName("Camera")
        self.info = QtWidgets.QPushButton(self.tab)
        self.info.setGeometry(QtCore.QRect(130, 710, 93, 28))
        self.info.setObjectName("info")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.show_un = QtWidgets.QPushButton(self.tab_2)
        self.show_un.setGeometry(QtCore.QRect(190, 20, 93, 21))
        
       
#unknow people button
        self.show_un.setObjectName("show_un")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_2.setGeometry(QtCore.QRect(120, 20, 51, 21))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.label_2.setObjectName("label_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 60, 1091, 631))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
#info 2 button        
        self.info_2 = QtWidgets.QPushButton(self.tab_2)
        self.info_2.setGeometry(QtCore.QRect(130, 710, 93, 28))
        self.info_2.setObjectName("info_2")
#camera2 button
        self.Camera_2 = QtWidgets.QPushButton(self.tab_2)
        self.Camera_2.setGeometry(QtCore.QRect(20, 710, 93, 28))
        self.Camera_2.setObjectName("Camera_2")

        self.radioButton1 = QtWidgets.QRadioButton(self.tab)
        self.radioButton1.setGeometry(QtCore.QRect(1000, 710, 61, 20))
        self.radioButton1.setObjectName("radioButton")
        self.tabWidget.addTab(self.tab, "")


        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(1000, 710, 61, 20))
        self.radioButton.setObjectName("radioButton")
        self.tabWidget.addTab(self.tab_2, "")





        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.tabWidget)

        self.retranslateUzb(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.openF.clicked.connect(self.openfl)
        self.show_kn.clicked.connect(self.showtab1)
        self.radioButton.clicked.connect(self.check)
        self.radioButton1.clicked.connect(self.check1)
        self.show_un.clicked.connect(self.showtab2)
        self.Camera.clicked.connect(self.cam1)
        self.Camera_2.clicked.connect(self.cam1)
        self.info.clicked.connect(self.instructionUZ)


    
        
    def openfl(self):
        self.path = QFileDialog.getOpenFileName(self,'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        
        self.all_data = pd.read_csv(self.path[0])

    def showtab1(self):

        numcolumn = self.spinBox.value()

        if numcolumn == 0:
            numRows = len(self.all_data.index)
        else: 
            numRows = numcolumn

        self.table.setColumnCount(len(self.all_data.columns))
        self.table.setRowCount(numRows)
        self.table.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):  
                self.table.setItem(i,j,QTableWidgetItem(str(self.all_data.iat[i,j])))

        self.table.resizeColumnsToContents()




    def showtab2(self):

        numcolumn = self.spinBox_2.value()

        if numcolumn == 0:
            numRows = len(self.all_data.index)
        else: 
            numRows = numcolumn

        self.tableWidget_2.setColumnCount(len(self.all_data.columns))
        self.tableWidget_2.setRowCount(numRows)
        self.tableWidget_2.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):  
                self.tableWidget_2.setItem(i,j,QTableWidgetItem(str(self.all_data.iat[i,j])))

        self.tableWidget_2.resizeColumnsToContents()



    def check(self):
        
        # checking if it is checked
        if self.radioButton.isChecked():
            
            # changing text of label
            self.retranslateEng(Form)
        # if it is not checked
        else:
            # changing text of label
            self.retranslateUzb(Form)


    def check1(self):
        # checking if it is checked
        if self.radioButton1.isChecked():
        # changing text of label
            self.retranslateEng(Form)
        # if it is not checked
        else:
        # changing text of label
            self.retranslateUzb(Form)


    def cam1(self):
     	import Face_Camera
     	Face_Camera.camera()     	
			

    
       
    def instructionUZ(self):
    	pass

    	

    def instructionEng(self):
    	pass



    def retranslateEng(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cascade"))
        self.openF.setText(_translate("Form", "Browse files"))
        self.label.setText(_translate("Form", "Known People"))
        self.show_kn.setText(_translate("Form", "Show"))
        self.Camera.setText(_translate("Form", "Camera"))
        self.info.setText(_translate("Form", "Instructions"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Known"))
        self.show_un.setText(_translate("Form", "Show"))
        self.label_2.setText(_translate("Form", "Unknown People"))
        self.info_2.setText(_translate("Form", "Instructions"))
        self.Camera_2.setText(_translate("Form", "Camera"))
        self.radioButton.setText(_translate("Form", "Eng"))
        self.radioButton1.setText(_translate("Form", "Eng"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Unknow"))


    def retranslateUzb(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cascade"))
        self.openF.setText(_translate("Form", "Fayl Yuklash"))
        self.label.setText(_translate("Form", "Tanish Odamlar"))
        self.show_kn.setText(_translate("Form", "Yuklash"))
        self.Camera.setText(_translate("Form", "Kamera"))
        self.info.setText(_translate("Form", "Yo'riqnoma"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tanish"))
        self.show_un.setText(_translate("Form", "Ko'rsatish"))
        self.label_2.setText(_translate("Form", "Notanish Odamlar"))
        self.info_2.setText(_translate("Form", "Yo'riqnoma"))
        self.Camera_2.setText(_translate("Form", "Kamera"))
        self.radioButton.setText(_translate("Form", "Eng"))
        self.radioButton1.setText(_translate("Form", "Eng"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Notanish"))


        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
