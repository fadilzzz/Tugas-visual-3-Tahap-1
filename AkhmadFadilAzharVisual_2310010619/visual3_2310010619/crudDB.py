import mysql.connector

class my_cruddb:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'visual3_2310010619'
        )

    def simpanUsers(self, id_user, nama_user, email, password, kota):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO users (id_user, nama_user, email, password, kota) VALUES (%s, %s, %s, %s, %s)",(id_user, nama_user, email, password, kota))
        self.conn.commit()
        alamat.close()

    def ubahUsers(self, id_user, nama_user, email, password, kota):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE users SET nama_user=%s, email=%s, password=%s, kota=%s WHERE id_user=%s",(nama_user, email, password, kota, id_user))
        self.conn.commit()
        alamat.close()

    def hapusUsers(self, id_user):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM users WHERE id_user=%s",(id_user,))
        self.conn.commit()
        alamat.close()

    def dataUsers(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("SELECT * FROM users ORDER BY id_user ASC")
        record = alamat.fetchall()
        alamat.close()
        return record

    def cariUsers(self, param):
        sql = "SELECT * FROM users WHERE id_user LIKE %s OR nama_user LIKE %s OR email LIKE %s OR kota LIKE %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanDzikirPlaylist(self, id_playlist, nama_dzikir, jenis_dzikir, deskripsi, audio_path):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO dzikir_playlist (id_playlist, nama_dzikir, jenis_dzikir, deskripsi, audio_path) VALUES (%s, %s, %s, %s, %s)",(id_playlist, nama_dzikir, jenis_dzikir, deskripsi, audio_path))
        self.conn.commit()
        alamat.close()

    def ubahDzikirPlaylist(self, id_playlist, nama_dzikir, jenis_dzikir, deskripsi, audio_path):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE dzikir_playlist SET nama_dzikir=%s, jenis_dzikir=%s, deskripsi=%s, audio_path=%s WHERE id_playlist=%s",(nama_dzikir, jenis_dzikir, deskripsi, audio_path, id_playlist))
        self.conn.commit()
        alamat.close()

    def hapusDzikirPlaylist(self, id_playlist):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM dzikir_playlist WHERE id_playlist=%s",(id_playlist,))
        self.conn.commit()
        alamat.close()

    def dataDzikirPlaylist(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("SELECT * FROM dzikir_playlist ORDER BY id_playlist ASC")
        record = alamat.fetchall()
        alamat.close()
        return record

    def cariDzikirPlaylist(self, param):
        sql = "SELECT * FROM dzikir_playlist WHERE id_playlist LIKE %s OR nama_dzikir LIKE %s OR jenis_dzikir LIKE %s OR deskripsi LIKE %s OR audio_path LIKE %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanZikirCounter(self, id_counter, id_user, id_playlist, total_zikir, tanggal):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO zikir_counter (id_counter, id_user, id_playlist, total_zikir, tanggal) VALUES (%s, %s, %s, %s, %s)",(id_counter, id_user, id_playlist, total_zikir, tanggal))
        self.conn.commit()
        alamat.close()

    def ubahZikirCounter(self, id_counter, id_user, id_playlist, total_zikir, tanggal):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE zikir_counter SET id_user=%s, id_playlist=%s, total_zikir=%s, tanggal=%s WHERE id_counter=%s",(id_user, id_playlist, total_zikir, tanggal, id_counter))
        self.conn.commit()
        alamat.close()

    def hapusZikirCounter(self, id_counter):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM zikir_counter WHERE id_counter=%s",(id_counter,))
        self.conn.commit()
        alamat.close()

    def dataZikirCounter(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("SELECT * FROM zikir_counter ORDER BY id_counter ASC")
        record = alamat.fetchall()
        alamat.close()
        return record

    def cariZikirCounter(self, param):
        sql = "SELECT * FROM zikir_counter WHERE id_counter LIKE %s OR id_user LIKE %s OR id_playlist LIKE %s OR total_zikir LIKE %s OR tanggal LIKE %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanPaymentType(self, id_payment, nama_payment, status, deskripsi, provider):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO payment_type (id_payment, nama_payment, status, deskripsi, provider) VALUES (%s, %s, %s, %s, %s)",(id_payment, nama_payment, status, deskripsi, provider))
        self.conn.commit()
        alamat.close()

    def ubahPaymentType(self, id_payment, nama_payment, status, deskripsi, provider):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE payment_type SET nama_payment=%s, status=%s, deskripsi=%s, provider=%s WHERE id_payment=%s",(nama_payment, status, deskripsi, provider, id_payment))
        self.conn.commit()
        alamat.close()

    def hapusPaymentType(self, id_payment):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM payment_type WHERE id_payment=%s",(id_payment,))
        self.conn.commit()
        alamat.close()

    def dataPaymentType(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("SELECT * FROM payment_type ORDER BY id_payment ASC")
        record = alamat.fetchall()
        alamat.close()
        return record

    def cariPaymentType(self, param):
        sql = "SELECT * FROM payment_type WHERE id_payment LIKE %s OR nama_payment LIKE %s OR status LIKE %s OR deskripsi LIKE %s OR provider LIKE %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanShadaqahHistory(self, id_shadaqah, id_user, id_payment, jumlah_donasi, tanggal_donasi):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO shadaqah_history (id_shadaqah, id_user, id_payment, jumlah_donasi, tanggal_donasi) VALUES (%s, %s, %s, %s, %s)",(id_shadaqah, id_user, id_payment, jumlah_donasi, tanggal_donasi))
        self.conn.commit()
        alamat.close()

    def ubahShadaqahHistory(self, id_shadaqah, id_user, id_payment, jumlah_donasi, tanggal_donasi):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE shadaqah_history SET id_user=%s, id_payment=%s, jumlah_donasi=%s, tanggal_donasi=%s WHERE id_shadaqah=%s",(id_user, id_payment, jumlah_donasi, tanggal_donasi, id_shadaqah))
        self.conn.commit()
        alamat.close()

    def hapusShadaqahHistory(self, id_shadaqah):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM shadaqah_history WHERE id_shadaqah=%s",(id_shadaqah,))
        self.conn.commit()
        alamat.close()

    def dataShadaqahHistory(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("SELECT * FROM shadaqah_history ORDER BY id_shadaqah ASC")
        record = alamat.fetchall()
        alamat.close()
        return record

    def cariShadaqahHistory(self, param):
        sql = "SELECT * FROM shadaqah_history WHERE id_shadaqah LIKE %s OR id_user LIKE %s OR id_payment LIKE %s OR jumlah_donasi LIKE %s OR tanggal_donasi LIKE %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record
