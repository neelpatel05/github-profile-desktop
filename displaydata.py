# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'displaydata.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 618)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 20, 361, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.editusername = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.editusername.setObjectName("editusername")
        self.horizontalLayout_7.addWidget(self.editusername)
        self.getdata = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.getdata.setObjectName("getdata")
        self.getdata.clicked.connect(self.getuserdata)
        self.horizontalLayout_7.addWidget(self.getdata)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 120, 511, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.username = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.username.setObjectName("username")
        self.horizontalLayout_3.addWidget(self.username)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.followers = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.followers.setObjectName("followers")
        self.horizontalLayout_2.addWidget(self.followers)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.following = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.following.setObjectName("following")
        self.horizontalLayout_5.addWidget(self.following)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.repos = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.repos.setObjectName("repos")
        self.horizontalLayout_6.addWidget(self.repos)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.location = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.location.setObjectName("location")
        self.horizontalLayout_4.addWidget(self.location)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 621, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 90, 171, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 270, 631, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.repostable = QtWidgets.QTableWidget(self.centralwidget)
        self.repostable.setGeometry(QtCore.QRect(20, 330, 591, 221))
        self.repostable.setObjectName("repostable")
        self.repostable.setColumnCount(0)
        self.repostable.setRowCount(0)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 300, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GitHub Profile Application"))
        self.label_7.setText(_translate("MainWindow", "Username"))
        self.getdata.setText(_translate("MainWindow", "Get Data"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_4.setText(_translate("MainWindow", "Followers"))
        self.label_5.setText(_translate("MainWindow", "Following"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_6.setText(_translate("MainWindow", "Repository"))
        self.label_3.setText(_translate("MainWindow", "Location"))
        self.label_8.setText(_translate("MainWindow", "GitHub Information"))
        self.label_9.setText(_translate("MainWindow", "Repositores"))

    def getuserdata(self):

        URL = "https://api.github.com/users/"+str(self.editusername.text())
        global data
        try:
            r=requests.get(url = URL)
            data=r.json()
            self.name.setText(str(data['name']))
            self.username.setText(str(data['login']))
            self.location.setText(str(data['location']))
            self.followers.setText(str(data['followers']))
            self.following.setText(str(data['following']))
            self.repos.setText(str(data['public_repos']))
            self.getuserrepos()

        except:
            self.name.setText("Some Error Occured")
        

    def getuserrepos(self):

        REPOSURL = str(data['repos_url'])
        count=0

        try:
            r=requests.get(url = REPOSURL)
            reposdata = r.json()
            for i in reposdata:
                count=count+1
                
            self.repostable.setRowCount(0)
            self.repostable.setRowCount(count)                
            self.repostable.setColumnCount(5)
            
            #self.repostable.setItem(0,0,QtGui.QTableWidgetItem("Repo Name"))
            #self.repostable.setItem(0,1,QtGui.QTableWidgetItem("Description"))
            #self.repostable.setItem(0,2,QtGui.QTableWidgetItem("Language"))
            #self.repostable.setItem(0,3,QtGui.QTableWidgetItem("Repo Name"))
            #self.repostable.setItem(0,4,QtGui.QTableWidgetItem("Branch"))
            
        except:
            self.location.setText("Some Error Occured")

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

