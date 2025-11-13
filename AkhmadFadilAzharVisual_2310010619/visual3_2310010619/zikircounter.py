import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class zikircounter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("zikircounter.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.form.btnSimpan.clicked.connect(self.doSimpanZikirCounter)
        self.form.btnUbah.clicked.connect(self.doUbahZikirCounter)
        self.form.btnHapus.clicked.connect(self.doHapusZikirCounter)
        self.form.editCari.textChanged.connect(self.doCariZikirCounter)
        self.form.tabelZikirCounter.itemClicked.connect(self.doTabelKlik)

        self.tampilDataZikirCounter()

    def doSimpanZikirCounter(self):
        if not self.form.editIdCounter.text().strip():
            QMessageBox.information(None,"Informasi","ID Counter belum di isi")
            self.form.editIdCounter.setFocus()
        elif not self.form.editIdUser.text().strip():
            QMessageBox.information(None,"Informasi","ID User belum di isi")
            self.form.editIdUser.setFocus()
        elif not self.form.editIdPlaylist.text().strip():
            QMessageBox.information(None,"Informasi","ID Playlist belum di isi")
            self.form.editIdPlaylist.setFocus()
        elif not self.form.editTotalZikir.text().strip():
            QMessageBox.information(None,"Informasi","Total Zikir belum di isi")
            self.form.editTotalZikir.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Simpan Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdCounter.text()
                tempIdUser = self.form.editIdUser.text()
                tempIdPlaylist = self.form.editIdPlaylist.text()
                tempTotal = self.form.editTotalZikir.text()
                tempTanggal = self.form.editTanggal.text()
                self.crud.simpanZikirCounter(tempID, tempIdUser, tempIdPlaylist, tempTotal, tempTanggal)
                self.tampilDataZikirCounter()
            else:
                pass

    def doUbahZikirCounter(self):
        if not self.form.editIdCounter.text().strip():
            QMessageBox.information(None,"Informasi","ID Counter belum di isi. Klik data dari tabel.")
            self.form.editIdCounter.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Ubah","Ubah Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdCounter.text()
                tempIdUser = self.form.editIdUser.text()
                tempIdPlaylist = self.form.editIdPlaylist.text()
                tempTotal = self.form.editTotalZikir.text()
                tempTanggal = self.form.editTanggal.text()
                self.crud.ubahZikirCounter(tempID, tempIdUser, tempIdPlaylist, tempTotal, tempTanggal)
                self.tampilDataZikirCounter()
            else:
                pass

    def doHapusZikirCounter(self):
        if not self.form.editIdCounter.text().strip():
            QMessageBox.information(None,"Informasi","ID Counter belum di isi. Klik data dari tabel.")
            self.form.editIdCounter.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Hapus","Hapus Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdCounter.text()
                self.crud.hapusZikirCounter(tempID)
                self.tampilDataZikirCounter()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
            else:
                pass

    def tampilDataZikirCounter(self):
        baris = self.crud.dataZikirCounter()
        self.form.tabelZikirCounter.setRowCount(0)
        for r in baris:
            i = self.form.tabelZikirCounter.rowCount()
            self.form.tabelZikirCounter.insertRow(i)
            self.form.tabelZikirCounter.setItem(i,0, QTableWidgetItem(r["id_counter"]))
            self.form.tabelZikirCounter.setItem(i,1, QTableWidgetItem(r["id_user"]))
            self.form.tabelZikirCounter.setItem(i,2, QTableWidgetItem(r["id_playlist"]))
            self.form.tabelZikirCounter.setItem(i,3, QTableWidgetItem(r["total_zikir"]))
            self.form.tabelZikirCounter.setItem(i,4, QTableWidgetItem(r["tanggal"]))

        self.bersihkanForm()

    def doCariZikirCounter(self):
        cari = self.form.editCari.text()
        baris = self.crud.cariZikirCounter(cari)
        self.form.tabelZikirCounter.setRowCount(0)
        for r in baris:
            i = self.form.tabelZikirCounter.rowCount()
            self.form.tabelZikirCounter.insertRow(i)
            self.form.tabelZikirCounter.setItem(i,0, QTableWidgetItem(r["id_counter"]))
            self.form.tabelZikirCounter.setItem(i,1, QTableWidgetItem(r["id_user"]))
            self.form.tabelZikirCounter.setItem(i,2, QTableWidgetItem(r["id_playlist"]))
            self.form.tabelZikirCounter.setItem(i,3, QTableWidgetItem(r["total_zikir"]))
            self.form.tabelZikirCounter.setItem(i,4, QTableWidgetItem(r["tanggal"]))

    def bersihkanForm(self):
        self.form.editIdCounter.clear()
        self.form.editIdUser.clear()
        self.form.editIdPlaylist.clear()
        self.form.editTotalZikir.clear()
        self.form.editTanggal.clear()

    def doTabelKlik(self, item):
        row = item.row()
        id_counter = self.form.tabelZikirCounter.item(row, 0).text()
        id_user = self.form.tabelZikirCounter.item(row, 1).text()
        id_playlist = self.form.tabelZikirCounter.item(row, 2).text()
        total_zikir = self.form.tabelZikirCounter.item(row, 3).text()
        tanggal = self.form.tabelZikirCounter.item(row, 4).text()

        self.form.editIdCounter.setText(id_counter)
        self.form.editIdUser.setText(id_user)
        self.form.editIdPlaylist.setText(id_playlist)
        self.form.editTotalZikir.setText(total_zikir)
        self.form.editTanggal.setText(tanggal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = zikir_counter()
    widget.show()
    sys.exit(app.exec())
