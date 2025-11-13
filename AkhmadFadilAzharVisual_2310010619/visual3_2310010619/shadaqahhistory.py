import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class shadaqahhistory(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("shadaqahhistory.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.form.btnSimpan.clicked.connect(self.doSimpanShadaqahHistory)
        self.form.btnUbah.clicked.connect(self.doUbahShadaqahHistory)
        self.form.btnHapus.clicked.connect(self.doHapusShadaqahHistory)
        self.form.editCari.textChanged.connect(self.doCariShadaqahHistory)
        self.form.tabelShadaqahHistory.itemClicked.connect(self.doTabelKlik)

        self.tampilDataShadaqahHistory()

    def doSimpanShadaqahHistory(self):
        if not self.form.editIdShadaqah.text().strip():
            QMessageBox.information(None,"Informasi","ID Shadaqah belum di isi")
            self.form.editIdShadaqah.setFocus()
        elif not self.form.editIdUser.text().strip():
            QMessageBox.information(None,"Informasi","ID User belum di isi")
            self.form.editIdUser.setFocus()
        elif not self.form.editIdPayment.text().strip():
            QMessageBox.information(None,"Informasi","ID Payment belum di isi")
            self.form.editIdPayment.setFocus()
        elif not self.form.editJumlahDonasi.text().strip():
            QMessageBox.information(None,"Informasi","Jumlah Donasi belum di isi")
            self.form.editJumlahDonasi.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Simpan Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdShadaqah.text()
                tempIdUser = self.form.editIdUser.text()
                tempIdPayment = self.form.editIdPayment.text()
                tempJumlah = self.form.editJumlahDonasi.text()
                tempTanggal = self.form.editTanggalDonasi.text()
                self.crud.simpanShadaqahHistory(tempID, tempIdUser, tempIdPayment, tempJumlah, tempTanggal)
                self.tampilDataShadaqahHistory()
            else:
                pass

    def doUbahShadaqahHistory(self):
        if not self.form.editIdShadaqah.text().strip():
            QMessageBox.information(None,"Informasi","ID Shadaqah belum di isi. Klik data dari tabel.")
            self.form.editIdShadaqah.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Ubah","Ubah Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdShadaqah.text()
                tempIdUser = self.form.editIdUser.text()
                tempIdPayment = self.form.editIdPayment.text()
                tempJumlah = self.form.editJumlahDonasi.text()
                tempTanggal = self.form.editTanggalDonasi.text()
                self.crud.ubahShadaqahHistory(tempID, tempIdUser, tempIdPayment, tempJumlah, tempTanggal)
                self.tampilDataShadaqahHistory()
            else:
                pass

    def doHapusShadaqahHistory(self):
        if not self.form.editIdShadaqah.text().strip():
            QMessageBox.information(None,"Informasi","ID Shadaqah belum di isi. Klik data dari tabel.")
            self.form.editIdShadaqah.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Hapus","Hapus Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdShadaqah.text()
                self.crud.hapusShadaqahHistory(tempID)
                self.tampilDataShadaqahHistory()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
            else:
                pass

    def tampilDataShadaqahHistory(self):
        baris = self.crud.dataShadaqahHistory()
        self.form.tabelShadaqahHistory.setRowCount(0)
        for r in baris:
            i = self.form.tabelShadaqahHistory.rowCount()
            self.form.tabelShadaqahHistory.insertRow(i)
            self.form.tabelShadaqahHistory.setItem(i,0, QTableWidgetItem(r["id_shadaqah"]))
            self.form.tabelShadaqahHistory.setItem(i,1, QTableWidgetItem(r["id_user"]))
            self.form.tabelShadaqahHistory.setItem(i,2, QTableWidgetItem(r["id_payment"]))
            self.form.tabelShadaqahHistory.setItem(i,3, QTableWidgetItem(r["jumlah_donasi"]))
            self.form.tabelShadaqahHistory.setItem(i,4, QTableWidgetItem(r["tanggal_donasi"]))

        self.bersihkanForm()

    def doCariShadaqahHistory(self):
        cari = self.form.editCari.text()
        baris = self.crud.cariShadaqahHistory(cari)
        self.form.tabelShadaqahHistory.setRowCount(0)
        for r in baris:
            i = self.form.tabelShadaqahHistory.rowCount()
            self.form.tabelShadaqahHistory.insertRow(i)
            self.form.tabelShadaqahHistory.setItem(i,0, QTableWidgetItem(r["id_shadaqah"]))
            self.form.tabelShadaqahHistory.setItem(i,1, QTableWidgetItem(r["id_user"]))
            self.form.tabelShadaqahHistory.setItem(i,2, QTableWidgetItem(r["id_payment"]))
            self.form.tabelShadaqahHistory.setItem(i,3, QTableWidgetItem(r["jumlah_donasi"]))
            self.form.tabelShadaqahHistory.setItem(i,4, QTableWidgetItem(r["tanggal_donasi"]))

    def bersihkanForm(self):
        self.form.editIdShadaqah.clear()
        self.form.editIdUser.clear()
        self.form.editIdPayment.clear()
        self.form.editJumlahDonasi.clear()
        self.form.editTanggalDonasi.clear()

    def doTabelKlik(self, item):
        row = item.row()
        id_shadaqah = self.form.tabelShadaqahHistory.item(row, 0).text()
        id_user = self.form.tabelShadaqahHistory.item(row, 1).text()
        id_payment = self.form.tabelShadaqahHistory.item(row, 2).text()
        jumlah_donasi = self.form.tabelShadaqahHistory.item(row, 3).text()
        tanggal_donasi = self.form.tabelShadaqahHistory.item(row, 4).text()

        self.form.editIdShadaqah.setText(id_shadaqah)
        self.form.editIdUser.setText(id_user)
        self.form.editIdPayment.setText(id_payment)
        self.form.editJumlahDonasi.setText(jumlah_donasi)
        self.form.editTanggalDonasi.setText(tanggal_donasi)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = shadaqah_history()
    widget.show()
    sys.exit(app.exec())
