import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtGui import QStandardItemModel, QStandardItem,QPixmap
from PyQt5.QtWidgets import QMainWindow,QWidget,QApplication,QDialog,QTableWidgetItem,QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('page1.ui', self)
        
        gambar=QPixmap('asset/imglogin.png')
        self.label.setPixmap(gambar)
       
        self.sandi.setEchoMode(QtWidgets.QLineEdit.Password)
        self.masuk.clicked.connect(self.GoPage2)
        
    def login(self):
        page2 = Utama()    
        widget.addWidget(page2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def GoPage2(self):
        data_user=["admin"]    
        data_password=["admin123"]
        user = str(self.user.text())
        password = str(self.sandi.text())
        if len(user) == 0 or len(password)==0:
            self.alert.setText("silahkan isi bidang kosong dahulu!!!")
        elif user not in data_user or password not in data_password:
            self.alert.setText("username atau password salah!!!")
        else:
           self.login()
   
class Utama(QMainWindow):
    def __init__(self):
        super(Utama, self).__init__()
        loadUi('main.ui', self)
        self.proses.clicked.connect(self.hitung_total)
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, "tableWidget")
        self.listView = self.findChild(QtWidgets.QListView, "listView")
        self.setFixedSize(self.size())
        
        self.hargaMenu = [
            10000,
            12000,
            15000,
            13000,
            11000,
            10000,
            20000,
            30000,
            25000,
            30000,
            17000,
            20000
        ]

        self.namaMenu = {
            self.label_13: 'Cappucino',
            self.label_14: 'Mocacino',
            self.label_15: 'Americano',
            self.label_16: 'Latte',
            self.label_17: 'Espresso',
            self.label_18: 'Mocha',
            self.label_19: 'Pasta',
            self.label_20: 'Kebab',
            self.label_21: 'Pizza',
            self.label_22: 'Hotdog',
            self.label_23: 'Dinsum',
            self.label_24: 'Steak',
        }
        
    def hitung_total(self):
        nama_pemesan = self.pemesan.text()
        no_pemesan = str(self.no_pesan.text())
        jumlah_uang = int(self.jumlah_uang.text())

        model = QStandardItemModel()
        model.appendRow(QStandardItem("Nama Pemesan: " + nama_pemesan))
        model.appendRow(QStandardItem("No Pemesan: " + no_pemesan))
        model.appendRow(QStandardItem("Jumlah Uang: " + str(jumlah_uang)))

        self.spinboxes = [
            self.spinBox_1,
            self.spinBox_2,
            self.spinBox_3,
            self.spinBox_4,
            self.spinBox_5,
            self.spinBox_6,
            self.spinBox_7,
            self.spinBox_8,
            self.spinBox_9,
            self.spinBox_10,
            self.spinBox_11,
            self.spinBox_12,
            
        ]

        total_harga = 0
        table_rows = []
        for i in range(len(self.spinboxes)):
            if self.spinboxes[i].value() == 0:
                continue
            else:
                jumlah = self.spinboxes[i].value()
                harga = self.hargaMenu[i]
                total_harga_menu = jumlah * harga
                nama_menu = self.namaMenu[list(self.namaMenu.keys())[i]]
                table_rows.append([nama_menu, jumlah, total_harga_menu])
                total_harga += total_harga_menu

        self.tableWidget.setRowCount(len(table_rows) + 2)  # Tambahkan 2 baris tambahan untuk total harga dan kembalian
        self.tableWidget.setColumnCount(3)  # Ubah jumlah kolom menjadi 3
        
        self.tableWidget.setColumnWidth(0, 80)
        self.tableWidget.setColumnWidth(1, 20)
        self.tableWidget.setColumnWidth(2, 50)
        self.tableWidget.horizontalHeader().setVisible(False)  # Menyembunyikan header atas
        self.tableWidget.verticalHeader().setVisible(False)  # Menyembunyikan header samping
        self.tableWidget.setShowGrid(False)

        for row, data in enumerate(table_rows):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(QtCore.Qt.AlignLeft)  # Mengatur perataan teks kiri
                self.tableWidget.setItem(row, col, item)

        total_item = QTableWidgetItem("Total Bayar")
        total_item.setTextAlignment(QtCore.Qt.AlignLeft)  # Mengatur perataan teks kiri
        total_value = QTableWidgetItem(str(total_harga))
        total_value.setTextAlignment(QtCore.Qt.AlignLeft)  # Mengatur perataan teks kiri
        self.tableWidget.setItem(len(table_rows), 0, total_item)
        self.tableWidget.setItem(len(table_rows), 2, total_value)

        kembalian = jumlah_uang - total_harga
        kembalian_item = QTableWidgetItem("Kembalian")
        kembalian_item.setTextAlignment(QtCore.Qt.AlignLeft)  # Mengatur perataan teks kiri
        kembalian_value = QTableWidgetItem(str(kembalian))
        kembalian_value.setTextAlignment(QtCore.Qt.AlignLeft)  # Mengatur perataan teks kiri
        self.tableWidget.setItem(len(table_rows) + 1, 0, kembalian_item)
        self.tableWidget.setItem(len(table_rows) + 1, 2, kembalian_value)

        self.listView.setModel(model)

        if jumlah_uang < total_harga:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Maaf, uang Anda kurang")
            msg.setWindowTitle("Peringatan")
            msg.exec_()

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
page1 = MainWindow()
widget.addWidget(page1)
widget.show()
sys.exit(app.exec_())