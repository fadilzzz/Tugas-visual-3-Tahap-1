import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class paymenttype(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("paymenttype.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.form.btnSimpan.clicked.connect(self.doSimpanPaymentType)
        self.form.btnUbah.clicked.connect(self.doUbahPaymentType)
        self.form.btnHapus.clicked.connect(self.doHapusPaymentType)
        self.form.editCari.textChanged.connect(self.doCariPaymentType)
        self.form.tabelPaymentType.itemClicked.connect(self.doTabelKlik)

        self.tampilDataPaymentType()

    def doSimpanPaymentType(self):
        if not self.form.editIdPayment.text().strip():
            QMessageBox.information(None,"Informasi","ID Payment belum di isi")
            self.form.editIdPayment.setFocus()
        elif not self.form.editNamaPayment.text().strip():
            QMessageBox.information(None,"Informasi","Nama Payment belum di isi")
            self.form.editNamaPayment.setFocus()
        elif not self.form.editStatus.text().strip():
            QMessageBox.information(None,"Informasi","Status belum di isi")
            self.form.editStatus.setFocus()
        elif not self.form.editDeskripsi.text().strip():
            QMessageBox.information(None,"Informasi","Deskripsi belum di isi")
            self.form.editDeskripsi.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Simpan Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdPayment.text()
                tempNama = self.form.editNamaPayment.text()
                tempStatus = self.form.editStatus.text()
                tempDeskripsi = self.form.editDeskripsi.text()
                tempProvider = self.form.editProvider.text()
                self.crud.simpanPaymentType(tempID, tempNama, tempStatus, tempDeskripsi, tempProvider)
                self.tampilDataPaymentType()
            else:
                pass

    def doUbahPaymentType(self):
        if not self.form.editIdPayment.text().strip():
            QMessageBox.information(None,"Informasi","ID Payment belum di isi. Klik data dari tabel.")
            self.form.editIdPayment.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Ubah","Ubah Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdPayment.text()
                tempNama = self.form.editNamaPayment.text()
                tempStatus = self.form.editStatus.text()
                tempDeskripsi = self.form.editDeskripsi.text()
                tempProvider = self.form.editProvider.text()
                self.crud.ubahPaymentType(tempID, tempNama, tempStatus, tempDeskripsi, tempProvider)
                self.tampilDataPaymentType()
            else:
                pass

    def doHapusPaymentType(self):
        if not self.form.editIdPayment.text().strip():
            QMessageBox.information(None,"Informasi","ID Payment belum di isi. Klik data dari tabel.")
            self.form.editIdPayment.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Hapus","Hapus Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdPayment.text()
                self.crud.hapusPaymentType(tempID)
                self.tampilDataPaymentType()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
            else:
                pass

    def tampilDataPaymentType(self):
        baris = self.crud.dataPaymentType()
        self.form.tabelPaymentType.setRowCount(0)
        for r in baris:
            i = self.form.tabelPaymentType.rowCount()
            self.form.tabelPaymentType.insertRow(i)
            self.form.tabelPaymentType.setItem(i,0, QTableWidgetItem(r["id_payment"]))
            self.form.tabelPaymentType.setItem(i,1, QTableWidgetItem(r["nama_payment"]))
            self.form.tabelPaymentType.setItem(i,2, QTableWidgetItem(r["status"]))
            self.form.tabelPaymentType.setItem(i,3, QTableWidgetItem(r["deskripsi"]))
            self.form.tabelPaymentType.setItem(i,4, QTableWidgetItem(r["provider"]))

        self.bersihkanForm()

    def doCariPaymentType(self):
        cari = self.form.editCari.text()
        baris = self.crud.cariPaymentType(cari)
        self.form.tabelPaymentType.setRowCount(0)
        for r in baris:
            i = self.form.tabelPaymentType.rowCount()
            self.form.tabelPaymentType.insertRow(i)
            self.form.tabelPaymentType.setItem(i,0, QTableWidgetItem(r["id_payment"]))
            self.form.tabelPaymentType.setItem(i,1, QTableWidgetItem(r["nama_payment"]))
            self.form.tabelPaymentType.setItem(i,2, QTableWidgetItem(r["status"]))
            self.form.tabelPaymentType.setItem(i,3, QTableWidgetItem(r["deskripsi"]))
            self.form.tabelPaymentType.setItem(i,4, QTableWidgetItem(r["provider"]))

    def bersihkanForm(self):
        self.form.editIdPayment.clear()
        self.form.editNamaPayment.clear()
        self.form.editStatus.clear()
        self.form.editDeskripsi.clear()
        self.form.editProvider.clear()

    def doTabelKlik(self, item):
        row = item.row()
        id_payment = self.form.tabelPaymentType.item(row, 0).text()
        nama_payment = self.form.tabelPaymentType.item(row, 1).text()
        status = self.form.tabelPaymentType.item(row, 2).text()
        deskripsi = self.form.tabelPaymentType.item(row, 3).text()
        provider = self.form.tabelPaymentType.item(row, 4).text()

        self.form.editIdPayment.setText(id_payment)
        self.form.editNamaPayment.setText(nama_payment)
        self.form.editStatus.setText(status)
        self.form.editDeskripsi.setText(deskripsi)
        self.form.editProvider.setText(provider)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = payment_type()
    widget.show()
    sys.exit(app.exec())
