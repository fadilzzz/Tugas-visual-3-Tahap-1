import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class dzikirplaylist(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("dzikirplaylist.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.form.btnSimpan.clicked.connect(self.doSimpanDzikirPlaylist)
        self.form.btnUbah.clicked.connect(self.doUbahDzikirPlaylist)
        self.form.btnHapus.clicked.connect(self.doHapusDzikirPlaylist)
        self.form.editCari.textChanged.connect(self.doCariDzikirPlaylist)
        self.form.tabelDzikirPlaylist.itemClicked.connect(self.doTabelKlik)

        self.tampilDataDzikirPlaylist()

    def doSimpanDzikirPlaylist(self):
        if not self.form.editIdPlaylist.text().strip():
            QMessageBox.information(None,"Informasi","ID Playlist belum di isi")
            self.form.editIdPlaylist.setFocus()
        elif not self.form.editNamaDzikir.text().strip():
            QMessageBox.information(None,"Informasi","Nama Dzikir belum di isi")
            self.form.editNamaDzikir.setFocus()
        elif not self.form.editJenisDzikir.text().strip():
            QMessageBox.information(None,"Informasi","Jenis Dzikir belum di isi")
            self.form.editJenisDzikir.setFocus()
        elif not self.form.editDeskripsi.text().strip():
            QMessageBox.information(None,"Informasi","Deskripsi belum di isi")
            self.form.editDeskripsi.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Simpan Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdPlaylist.text()
                tempNama = self.form.editNamaDzikir.text()
                tempJenis = self.form.editJenisDzikir.text()
                tempDeskripsi = self.form.editDeskripsi.text()
                tempAudio = self.form.editAudioPath.text()
                self.crud.simpanDzikirPlaylist(tempID, tempNama, tempJenis, tempDeskripsi, tempAudio)
                self.tampilDataDzikirPlaylist()
            else:
                pass

    def doUbahDzikirPlaylist(self):
        if not self.form.editIdPlaylist.text().strip():
            QMessageBox.information(None,"Informasi","ID Playlist belum di isi. Klik data dari tabel.")
            self.form.editIdPlaylist.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Ubah","Ubah Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdPlaylist.text()
                tempNama = self.form.editNamaDzikir.text()
                tempJenis = self.form.editJenisDzikir.text()
                tempDeskripsi = self.form.editDeskripsi.text()
                tempAudio = self.form.editAudioPath.text()
                self.crud.ubahDzikirPlaylist(tempID, tempNama, tempJenis, tempDeskripsi, tempAudio)
                self.tampilDataDzikirPlaylist()
            else:
                pass

    def doHapusDzikirPlaylist(self):
        if not self.form.editIdPlaylist.text().strip():
            QMessageBox.information(None,"Informasi","ID Playlist belum di isi. Klik data dari tabel.")
            self.form.editIdPlaylist.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Hapus","Hapus Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdPlaylist.text()
                self.crud.hapusDzikirPlaylist(tempID)
                self.tampilDataDzikirPlaylist()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
            else:
                pass

    def tampilDataDzikirPlaylist(self):
        baris = self.crud.dataDzikirPlaylist()
        self.form.tabelDzikirPlaylist.setRowCount(0)
        for r in baris:
            i = self.form.tabelDzikirPlaylist.rowCount()
            self.form.tabelDzikirPlaylist.insertRow(i)
            self.form.tabelDzikirPlaylist.setItem(i,0, QTableWidgetItem(r["id_playlist"]))
            self.form.tabelDzikirPlaylist.setItem(i,1, QTableWidgetItem(r["nama_dzikir"]))
            self.form.tabelDzikirPlaylist.setItem(i,2, QTableWidgetItem(r["jenis_dzikir"]))
            self.form.tabelDzikirPlaylist.setItem(i,3, QTableWidgetItem(r["deskripsi"]))
            self.form.tabelDzikirPlaylist.setItem(i,4, QTableWidgetItem(r["audio_path"]))

        self.bersihkanForm()

    def doCariDzikirPlaylist(self):
        cari = self.form.editCari.text()
        baris = self.crud.cariDzikirPlaylist(cari)
        self.form.tabelDzikirPlaylist.setRowCount(0)
        for r in baris:
            i = self.form.tabelDzikirPlaylist.rowCount()
            self.form.tabelDzikirPlaylist.insertRow(i)
            self.form.tabelDzikirPlaylist.setItem(i,0, QTableWidgetItem(r["id_playlist"]))
            self.form.tabelDzikirPlaylist.setItem(i,1, QTableWidgetItem(r["nama_dzikir"]))
            self.form.tabelDzikirPlaylist.setItem(i,2, QTableWidgetItem(r["jenis_dzikir"]))
            self.form.tabelDzikirPlaylist.setItem(i,3, QTableWidgetItem(r["deskripsi"]))
            self.form.tabelDzikirPlaylist.setItem(i,4, QTableWidgetItem(r["audio_path"]))

    def bersihkanForm(self):
        self.form.editIdPlaylist.clear()
        self.form.editNamaDzikir.clear()
        self.form.editJenisDzikir.clear()
        self.form.editDeskripsi.clear()
        self.form.editAudioPath.clear()

    def doTabelKlik(self, item):
        row = item.row()
        id_playlist = self.form.tabelDzikirPlaylist.item(row, 0).text()
        nama_dzikir = self.form.tabelDzikirPlaylist.item(row, 1).text()
        jenis_dzikir = self.form.tabelDzikirPlaylist.item(row, 2).text()
        deskripsi = self.form.tabelDzikirPlaylist.item(row, 3).text()
        audio_path = self.form.tabelDzikirPlaylist.item(row, 4).text()

        self.form.editIdPlaylist.setText(id_playlist)
        self.form.editNamaDzikir.setText(nama_dzikir)
        self.form.editJenisDzikir.setText(jenis_dzikir)
        self.form.editDeskripsi.setText(deskripsi)
        self.form.editAudioPath.setText(audio_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = dzikir_playlist()
    widget.show()
    sys.exit(app.exec())
