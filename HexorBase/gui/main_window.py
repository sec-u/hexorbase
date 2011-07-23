import os
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(605, 620)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("%s/Icons/Database.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.database_Gbox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.database_Gbox.setFont(font)
        self.database_Gbox.setObjectName(_fromUtf8("database_Gbox"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.database_Gbox)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mysql_button = QtGui.QPushButton(self.database_Gbox)
        self.mysql_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("%s/Icons/mysql_logo.ico"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mysql_button.setIcon(icon1)
        self.mysql_button.setIconSize(QtCore.QSize(100, 100))
        self.mysql_button.setObjectName(_fromUtf8("mysql_button"))
        self.verticalLayout_2.addWidget(self.mysql_button)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.oracle_status = QtGui.QLabel(self.database_Gbox)
        self.oracle_status.setAlignment(QtCore.Qt.AlignCenter)
        self.oracle_status.setObjectName(_fromUtf8("oracle_status"))
        self.horizontalLayout_3.addWidget(self.oracle_status)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem = QtGui.QSpacerItem(34, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.oracle_button = QtGui.QPushButton(self.database_Gbox)
        self.oracle_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("%s/Icons/Oracle_Logo.ico"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oracle_button.setIcon(icon2)
        self.oracle_button.setIconSize(QtCore.QSize(100, 100))
        self.oracle_button.setObjectName(_fromUtf8("oracle_button"))
        self.verticalLayout_3.addWidget(self.oracle_button)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mysql_status = QtGui.QLabel(self.database_Gbox)
        self.mysql_status.setAlignment(QtCore.Qt.AlignCenter)
        self.mysql_status.setObjectName(_fromUtf8("mysql_status"))
        self.horizontalLayout.addWidget(self.mysql_status)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(34, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.postgresql = QtGui.QPushButton(self.database_Gbox)
        self.postgresql.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/postgresql.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.postgresql.setIcon(icon3)
        self.postgresql.setIconSize(QtCore.QSize(93, 96))
        self.postgresql.setObjectName(_fromUtf8("postgresql"))
        self.verticalLayout_8.addWidget(self.postgresql)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.sql_status = QtGui.QLabel(self.database_Gbox)
        self.sql_status.setAlignment(QtCore.Qt.AlignCenter)
        self.sql_status.setObjectName(_fromUtf8("sql_status"))
        self.horizontalLayout_2.addWidget(self.sql_status)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.sqlite_button = QtGui.QPushButton(self.database_Gbox)
        self.sqlite_button.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("%s/Icons/SQLite_Logo-3e5453f0a4c3e6f5.ico"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sqlite_button.setIcon(icon4)
        self.sqlite_button.setIconSize(QtCore.QSize(100, 100))
        self.sqlite_button.setObjectName(_fromUtf8("sqlite_button"))
        self.verticalLayout.addWidget(self.sqlite_button)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.postgresql_label = QtGui.QLabel(self.database_Gbox)
        self.postgresql_label.setAlignment(QtCore.Qt.AlignCenter)
        self.postgresql_label.setObjectName(_fromUtf8("postgresql_label"))
        self.horizontalLayout_4.addWidget(self.postgresql_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(34, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.sql_button = QtGui.QPushButton(self.database_Gbox)
        self.sql_button.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("%s/Icons/sql-server-2008-logo.ico"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sql_button.setIcon(icon5)
        self.sql_button.setIconSize(QtCore.QSize(100, 100))
        self.sql_button.setObjectName(_fromUtf8("sql_button"))
        self.verticalLayout_6.addWidget(self.sql_button)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.sqlite_label = QtGui.QLabel(self.database_Gbox)
        self.sqlite_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sqlite_label.setObjectName(_fromUtf8("sqlite_label"))
        self.horizontalLayout_7.addWidget(self.sqlite_label)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_6)
        spacerItem4 = QtGui.QSpacerItem(197, 9, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.verticalLayout_11.addWidget(self.database_Gbox)
        self.AdminGbox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AdminGbox.setFont(font)
        self.AdminGbox.setObjectName(_fromUtf8("AdminGbox"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.AdminGbox)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label = QtGui.QLabel(self.AdminGbox)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Icons/administrator.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_14.addWidget(self.label)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_2 = QtGui.QLabel(self.AdminGbox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_7.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.AdminGbox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_7.addWidget(self.label_3)
        spacerItem6 = QtGui.QSpacerItem(38, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_7.addItem(spacerItem6)
        self.horizontalLayout_13.addLayout(self.verticalLayout_7)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.username_linedit = QtGui.QLineEdit(self.AdminGbox)
        self.username_linedit.setObjectName(_fromUtf8("username_linedit"))
        self.verticalLayout_5.addWidget(self.username_linedit)
        spacerItem7 = QtGui.QSpacerItem(20, 3, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem7)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.password_linedit = QtGui.QLineEdit(self.AdminGbox)
        self.password_linedit.setEchoMode(QtGui.QLineEdit.Password)
        self.password_linedit.setObjectName(_fromUtf8("password_linedit"))
        self.verticalLayout_4.addWidget(self.password_linedit)
        spacerItem8 = QtGui.QSpacerItem(20, 11, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem8)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.login_button = QtGui.QPushButton(self.AdminGbox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/login.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_button.setIcon(icon)
        self.login_button.setIconSize(QtCore.QSize(28, 27))
        self.login_button.setCheckable(True)
        self.login_button.setFlat(False)
        self.login_button.setObjectName(_fromUtf8("login_button"))
        self.horizontalLayout_11.addWidget(self.login_button)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.password_manager_button = QtGui.QPushButton(self.AdminGbox)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/manager.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.password_manager_button.setIcon(icon7)
        self.password_manager_button.setIconSize(QtCore.QSize(28, 27))
        self.password_manager_button.setObjectName(_fromUtf8("password_manager_button"))
        self.horizontalLayout_11.addWidget(self.password_manager_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_13.addLayout(self.verticalLayout_5)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem10)
        self.verticalLayout_11.addWidget(self.AdminGbox)
        spacerItem11 = QtGui.QSpacerItem(20, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem11)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem12)
        self.brutefore_database = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brutefore_database.sizePolicy().hasHeightForWidth())
        self.brutefore_database.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.brutefore_database.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/bruteforce.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brutefore_database.setIcon(icon8)
        self.brutefore_database.setIconSize(QtCore.QSize(47, 40))
        self.brutefore_database.setObjectName(_fromUtf8("brutefore_database"))
        self.horizontalLayout_9.addWidget(self.brutefore_database)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout_11.addWidget(self.groupBox)
        spacerItem14 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem14)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "HexorBase", None, QtGui.QApplication.UnicodeUTF8))
        self.database_Gbox.setTitle(QtGui.QApplication.translate("MainWindow", "Database Servers", None, QtGui.QApplication.UnicodeUTF8))
        self.oracle_status.setText(QtGui.QApplication.translate("MainWindow", "<font color=red>API is not Installed</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.mysql_status.setText(QtGui.QApplication.translate("MainWindow", "<font color=red>API not Installed</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.sql_status.setText(QtGui.QApplication.translate("MainWindow", "<font color=red>API not Installed</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.postgresql_label.setText(QtGui.QApplication.translate("MainWindow", "<font color=red>API not Installed</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.sqlite_label.setText(QtGui.QApplication.translate("MainWindow", "<font color=red>API not Installed</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.AdminGbox.setTitle(QtGui.QApplication.translate("MainWindow", "Administration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.brutefore_database.setText(QtGui.QApplication.translate("MainWindow", " Bruteforce Database Servers", None, QtGui.QApplication.UnicodeUTF8))
        self.login_button.setText(QtGui.QApplication.translate("MainWindow", " Lock as Default Login", None, QtGui.QApplication.UnicodeUTF8))
        self.password_manager_button.setText(QtGui.QApplication.translate("MainWindow", "Password Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Audit Database Servers ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Written by: Saviour Emmanuel Ekiko", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Report bugs at: savioboyz@rocketmail.com", None, QtGui.QApplication.UnicodeUTF8))