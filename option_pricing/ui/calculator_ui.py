# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(617, 483)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.KeyParams_GroupBox = QGroupBox(self.centralwidget)
        self.KeyParams_GroupBox.setObjectName(u"KeyParams_GroupBox")
        self.KeyParams_GroupBox.setGeometry(QRect(20, 70, 581, 101))
        self.StockPrice = QLabel(self.KeyParams_GroupBox)
        self.StockPrice.setObjectName(u"StockPrice")
        self.StockPrice.setGeometry(QRect(10, 10, 121, 16))
        self.StockPriceInput = QLineEdit(self.KeyParams_GroupBox)
        self.StockPriceInput.setObjectName(u"StockPriceInput")
        self.StockPriceInput.setGeometry(QRect(140, 10, 113, 21))
        self.StrikeInput = QLineEdit(self.KeyParams_GroupBox)
        self.StrikeInput.setObjectName(u"StrikeInput")
        self.StrikeInput.setGeometry(QRect(140, 40, 113, 21))
        self.Strike = QLabel(self.KeyParams_GroupBox)
        self.Strike.setObjectName(u"Strike")
        self.Strike.setGeometry(QRect(40, 40, 101, 16))
        self.TimeInput = QLineEdit(self.KeyParams_GroupBox)
        self.TimeInput.setObjectName(u"TimeInput")
        self.TimeInput.setGeometry(QRect(140, 70, 113, 21))
        self.Time = QLabel(self.KeyParams_GroupBox)
        self.Time.setObjectName(u"Time")
        self.Time.setGeometry(QRect(10, 70, 131, 16))
        self.RiskFreeRate = QLabel(self.KeyParams_GroupBox)
        self.RiskFreeRate.setObjectName(u"RiskFreeRate")
        self.RiskFreeRate.setGeometry(QRect(310, 40, 111, 16))
        self.sigmaInput = QLineEdit(self.KeyParams_GroupBox)
        self.sigmaInput.setObjectName(u"sigmaInput")
        self.sigmaInput.setGeometry(QRect(430, 10, 113, 21))
        self.RiskFreeInput = QLineEdit(self.KeyParams_GroupBox)
        self.RiskFreeInput.setObjectName(u"RiskFreeInput")
        self.RiskFreeInput.setGeometry(QRect(430, 40, 113, 21))
        self.sigma = QLabel(self.KeyParams_GroupBox)
        self.sigma.setObjectName(u"sigma")
        self.sigma.setGeometry(QRect(340, 10, 81, 20))
        self.BT_GroupBox = QGroupBox(self.centralwidget)
        self.BT_GroupBox.setObjectName(u"BT_GroupBox")
        self.BT_GroupBox.setGeometry(QRect(20, 171, 281, 80))
        self.TimeStep_Input = QLineEdit(self.BT_GroupBox)
        self.TimeStep_Input.setObjectName(u"TimeStep_Input")
        self.TimeStep_Input.setGeometry(QRect(140, 40, 81, 21))
        self.TimeStep = QLabel(self.BT_GroupBox)
        self.TimeStep.setObjectName(u"TimeStep")
        self.TimeStep.setGeometry(QRect(60, 40, 71, 16))
        self.TimeStepMax_Button = QPushButton(self.BT_GroupBox)
        self.TimeStepMax_Button.setObjectName(u"TimeStepMax_Button")
        self.TimeStepMax_Button.setGeometry(QRect(230, 39, 41, 21))
        self.MC_GroupBox = QGroupBox(self.centralwidget)
        self.MC_GroupBox.setObjectName(u"MC_GroupBox")
        self.MC_GroupBox.setGeometry(QRect(320, 171, 281, 80))
        self.NumSim = QLabel(self.MC_GroupBox)
        self.NumSim.setObjectName(u"NumSim")
        self.NumSim.setGeometry(QRect(10, 39, 121, 21))
        self.NumSim_Input = QLineEdit(self.MC_GroupBox)
        self.NumSim_Input.setObjectName(u"NumSim_Input")
        self.NumSim_Input.setGeometry(QRect(130, 40, 81, 21))
        self.NumSimMax_Button = QPushButton(self.MC_GroupBox)
        self.NumSimMax_Button.setObjectName(u"NumSimMax_Button")
        self.NumSimMax_Button.setGeometry(QRect(220, 39, 41, 21))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(20, 260, 361, 81))
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(Qt.ElideNone)
        self.EuropeanStyle_RadioButton = QRadioButton(self.centralwidget)
        self.EuropeanStyle_RadioButton.setObjectName(u"EuropeanStyle_RadioButton")
        self.EuropeanStyle_RadioButton.setGeometry(QRect(30, 30, 100, 20))
        self.AmericanStyle_RadioButton = QRadioButton(self.centralwidget)
        self.AmericanStyle_RadioButton.setObjectName(u"AmericanStyle_RadioButton")
        self.AmericanStyle_RadioButton.setGeometry(QRect(150, 30, 100, 20))
        self.PricingModel_GroupBox = QGroupBox(self.centralwidget)
        self.PricingModel_GroupBox.setObjectName(u"PricingModel_GroupBox")
        self.PricingModel_GroupBox.setGeometry(QRect(250, 0, 351, 61))
        self.MC_CheckBox = QCheckBox(self.PricingModel_GroupBox)
        self.MC_CheckBox.setObjectName(u"MC_CheckBox")
        self.MC_CheckBox.setGeometry(QRect(250, 30, 121, 20))
        self.BS_CheckBox = QCheckBox(self.PricingModel_GroupBox)
        self.BS_CheckBox.setObjectName(u"BS_CheckBox")
        self.BS_CheckBox.setGeometry(QRect(10, 30, 121, 20))
        self.BT_CheckBox = QCheckBox(self.PricingModel_GroupBox)
        self.BT_CheckBox.setObjectName(u"BT_CheckBox")
        self.BT_CheckBox.setGeometry(QRect(130, 30, 121, 20))
        self.OptionStyle_GroupBox = QGroupBox(self.centralwidget)
        self.OptionStyle_GroupBox.setObjectName(u"OptionStyle_GroupBox")
        self.OptionStyle_GroupBox.setGeometry(QRect(20, 0, 221, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.OptionStyle_GroupBox.raise_()
        self.KeyParams_GroupBox.raise_()
        self.BT_GroupBox.raise_()
        self.MC_GroupBox.raise_()
        self.tableWidget.raise_()
        self.EuropeanStyle_RadioButton.raise_()
        self.AmericanStyle_RadioButton.raise_()
        self.PricingModel_GroupBox.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 617, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Option Pricing Calculator", None))
        self.KeyParams_GroupBox.setTitle("")
        self.StockPrice.setText(QCoreApplication.translate("MainWindow", u"Underlying Price (S)", None))
        self.Strike.setText(QCoreApplication.translate("MainWindow", u"Strike Price (K)", None))
        self.Time.setText(QCoreApplication.translate("MainWindow", u"Time to Maturity (T)", None))
        self.RiskFreeRate.setText(QCoreApplication.translate("MainWindow", u"Risk Free Rate (r)", None))
        self.sigma.setText(QCoreApplication.translate("MainWindow", u"Volatility (s)", None))
        self.BT_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Binomial Tree Input", None))
        self.TimeStep.setText(QCoreApplication.translate("MainWindow", u"Time Steps", None))
        self.TimeStepMax_Button.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.MC_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Monte Carlo Input", None))
        self.NumSim.setText(QCoreApplication.translate("MainWindow", u"No. of Simulations", None))
        self.NumSimMax_Button.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Black Scholes", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Binomial Tree", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Monte Carlo", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Call Price", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Put Price", None));
        self.EuropeanStyle_RadioButton.setText(QCoreApplication.translate("MainWindow", u"European", None))
        self.AmericanStyle_RadioButton.setText(QCoreApplication.translate("MainWindow", u"American", None))
        self.PricingModel_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Pricing Model", None))
        self.MC_CheckBox.setText(QCoreApplication.translate("MainWindow", u"Monte Carlo", None))
        self.BS_CheckBox.setText(QCoreApplication.translate("MainWindow", u"Black Scholes", None))
        self.BT_CheckBox.setText(QCoreApplication.translate("MainWindow", u"Binomial Tree", None))
        self.OptionStyle_GroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Option Style", None))
    # retranslateUi

