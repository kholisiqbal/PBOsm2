from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AppCaffe(object):
    def setupUi(self, AppCaffe):
        AppCaffe.setObjectName("AppCaffe")
        AppCaffe.setEnabled(True)
        AppCaffe.resize(793, 592)
        AppCaffe.setMinimumSize(QtCore.QSize(789, 565))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("asset/gambar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AppCaffe.setWindowIcon(icon)
        AppCaffe.setAutoFillBackground(False)
        AppCaffe.setStyleSheet("QmainWindow#AppCaffe {\n"
"    background-image: url(C:/Users/user/Documents/tugas akhir semester 2/PBO/asset/bg.jpeg);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(AppCaffe)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"    background-image: url(C:/Users/user/Documents/tugas akhir semester 2/PBO/asset/bg.jpeg);\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.label_54 = QtWidgets.QLabel(self.centralwidget)
        self.label_54.setGeometry(QtCore.QRect(280, 540, 221, 31))
        self.label_54.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_54.setObjectName("label_54")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(280, 20, 271, 31))
        self.label_30.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 28pt \"Arial\";")
        self.label_30.setObjectName("label_30")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 120, 771, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.spinBox_1 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_1.setObjectName("spinBox_1")
        self.gridLayout.addWidget(self.spinBox_1, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 5, 0, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout.addWidget(self.spinBox_5, 5, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 6, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_1.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 1, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 2, 2, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout.addWidget(self.spinBox_3, 3, 2, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout.addWidget(self.spinBox_4, 4, 2, 1, 1)
        self.spinBox_6 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout.addWidget(self.spinBox_6, 6, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 1, 0, 1, 1)
        self.spinBox_7 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_7.setObjectName("spinBox_7")
        self.gridLayout_2.addWidget(self.spinBox_7, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 1)
        self.spinBox_8 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.spinBox_8.setObjectName("spinBox_8")
        self.gridLayout_2.addWidget(self.spinBox_8, 1, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 2, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 1, 1, 1)
        self.spinBox_9 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_9.setObjectName("spinBox_9")
        self.gridLayout_2.addWidget(self.spinBox_9, 2, 2, 1, 1)
        self.spinBox_10 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_10.setObjectName("spinBox_10")
        self.gridLayout_2.addWidget(self.spinBox_10, 3, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 4, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_24.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 5, 0, 1, 1)
        self.spinBox_11 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_11.setObjectName("spinBox_11")
        self.gridLayout_2.addWidget(self.spinBox_11, 4, 2, 1, 1)
        self.spinBox_12 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_12.setObjectName("spinBox_12")
        self.gridLayout_2.addWidget(self.spinBox_12, 5, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(250, 390, 191, 121))
        self.tableWidget.setStyleSheet("font: 12pt \"Arial Narrow\";\n"
"border: none;\n"
"QTableView::item{padding:0px;}\n"
"background-color: rgb(170, 85, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(220, 280, 58, 19))
        self.label_28.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_28.setObjectName("label_28")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(220, 310, 231, 221))
        self.listView.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.listView.setObjectName("listView")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 280, 181, 201))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_25 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_25.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_25.setObjectName("label_25")
        self.verticalLayout.addWidget(self.label_25)
        self.pemesan = QtWidgets.QLineEdit(self.layoutWidget1)
        self.pemesan.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pemesan.setObjectName("pemesan")
        self.verticalLayout.addWidget(self.pemesan)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_26.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_26.setObjectName("label_26")
        self.verticalLayout.addWidget(self.label_26)
        self.no_pesan = QtWidgets.QLineEdit(self.layoutWidget1)
        self.no_pesan.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.no_pesan.setText("")
        self.no_pesan.setObjectName("no_pesan")
        self.verticalLayout.addWidget(self.no_pesan)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_27.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_27.setObjectName("label_27")
        self.verticalLayout.addWidget(self.label_27)
        self.jumlah_uang = QtWidgets.QLineEdit(self.layoutWidget1)
        self.jumlah_uang.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.jumlah_uang.setText("")
        self.jumlah_uang.setObjectName("jumlah_uang")
        self.verticalLayout.addWidget(self.jumlah_uang)
        self.proses = QtWidgets.QPushButton(self.layoutWidget1)
        self.proses.setStyleSheet("background-color: rgb(170, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.proses.setObjectName("proses")
        self.verticalLayout.addWidget(self.proses)
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(520, 70, 81, 53))
        self.label_33.setStyleSheet("font: 14pt \"Arial\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 255, 255);")
        self.label_33.setObjectName("label_33")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(160, 70, 91, 53))
        self.label_32.setStyleSheet("font: 14pt \"Arial\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 255, 255);")
        self.label_32.setObjectName("label_32")
        self.layoutWidget.raise_()
        self.label_54.raise_()
        self.label_30.raise_()
        self.layoutWidget.raise_()
        self.label_28.raise_()
        self.listView.raise_()
        self.tableWidget.raise_()
        self.label_33.raise_()
        self.label_32.raise_()
        AppCaffe.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AppCaffe)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 21))
        self.menubar.setObjectName("menubar")
        AppCaffe.setMenuBar(self.menubar)

        self.retranslateUi(AppCaffe)
        QtCore.QMetaObject.connectSlotsByName(AppCaffe)

    def retranslateUi(self, AppCaffe):
        _translate = QtCore.QCoreApplication.translate
        AppCaffe.setWindowTitle(_translate("AppCaffe", "AppCAffe"))
        self.label_54.setText(_translate("AppCaffe", "Copyright © 2023 InpoNgopi"))
        self.label_30.setText(_translate("AppCaffe", "DAFTAR MENU"))
        self.label_14.setText(_translate("AppCaffe", "Mocacino"))
        self.label_2.setText(_translate("AppCaffe", "                         Rp 12.000"))
        self.label_15.setText(_translate("AppCaffe", "Americano"))
        self.label_16.setText(_translate("AppCaffe", "Latte"))
        self.label_3.setText(_translate("AppCaffe", "                         Rp 15.000"))
        self.label_4.setText(_translate("AppCaffe", "                         Rp 13.000"))
        self.label_17.setText(_translate("AppCaffe", "Espresso"))
        self.label_18.setText(_translate("AppCaffe", "Mocha"))
        self.label_5.setText(_translate("AppCaffe", "                         Rp 11.000"))
        self.label_6.setText(_translate("AppCaffe", "                         Rp 10.000"))
        self.label_13.setText(_translate("AppCaffe", "Cappucino"))
        self.label_1.setText(_translate("AppCaffe", "                         Rp 10.000"))
        self.label_7.setText(_translate("AppCaffe", "                         Rp 20.000"))
        self.label_19.setText(_translate("AppCaffe", "Pasta"))
        self.label_20.setText(_translate("AppCaffe", "Kebab"))
        self.label_8.setText(_translate("AppCaffe", "                         Rp 30.000"))
        self.label_21.setText(_translate("AppCaffe", "Pizza"))
        self.label_22.setText(_translate("AppCaffe", "Hotdog"))
        self.label_9.setText(_translate("AppCaffe", "                         Rp 25.000"))
        self.label_23.setText(_translate("AppCaffe", "Dinsum"))
        self.label_11.setText(_translate("AppCaffe", "                         Rp 17.000"))
        self.label_24.setText(_translate("AppCaffe", "Steak"))
        self.label_12.setText(_translate("AppCaffe", "                         Rp 20.000"))
        self.label_10.setText(_translate("AppCaffe", "                         Rp 30.000"))
        self.label_28.setText(_translate("AppCaffe", "Pesanan"))
        self.label_25.setText(_translate("AppCaffe", "Nama Pemesan"))
        self.label_26.setText(_translate("AppCaffe", "Nomor Pemesan"))
        self.label_27.setText(_translate("AppCaffe", "Jumlah Uang"))
        self.proses.setText(_translate("AppCaffe", "Proses"))
        self.label_33.setText(_translate("AppCaffe", "Makanan"))
        self.label_32.setText(_translate("AppCaffe", "Minuman"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AppCaffe = QtWidgets.QMainWindow()
    ui = Ui_AppCaffe()
    ui.setupUi(AppCaffe)
    AppCaffe.show()
    sys.exit(app.exec_())
