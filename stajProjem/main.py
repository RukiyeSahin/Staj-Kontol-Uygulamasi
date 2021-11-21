# --------------------KÜTÜPHANE--------------------#
# -------------------------------------------------#
import csv
import pandas as pd
from PyQt5 import QtGui
import sys
import os
from PyQt5 import QtWidgets
import datetime
from PyQt5.QtWidgets import *
from datetime import date
from DonemSorgguUI import MlUi_MainWindow
from FormGuncelleeUI import MyyUi_MainWindow
from FormKaydettUI import MeUi_MainWindow
from FormSayfasiUI import *
from GiriisUI import *
from OgrenciSorguuUI import MyUi_MainWindow
from OgrenciSorguuUI import MyUi_MainWindow
from YerSorguu2UI import MyeeUi_MainWindow
from YerSorguuUI import MyeUi_MainWindow


# --------------------UYGULAMA OLUŞTUR--------------------#
# -------------------------------------------------#

Uygulama = QApplication(sys.argv)
penGiris = QDialog()
ui2 = Ui_Dialog()
ui2.setupUi(penGiris)
penGiris.show()

penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)  # pencereyi form ile birleştirdik
# penAna.show()
# penAna.showMaximized()

penOgrSorguu = QMainWindow()
ui3 = MyUi_MainWindow()
ui3.setupUi(penOgrSorguu)

penFormKayit = QMainWindow()
ui4 = MeUi_MainWindow()
ui4.setupUi(penFormKayit)
#penFormKayit = QDialog()
#ui4 = MeUi_Dialog()
#ui4.setupUi(penFormKayit)

penFormGuncelle = QMainWindow()
ui5 = MyyUi_MainWindow()
ui5.setupUi(penFormGuncelle)

penDonemSorggu = QMainWindow()
ui9 = MlUi_MainWindow()
ui9.setupUi(penDonemSorggu)

penYerSorguu = QMainWindow()
ui7 = MyeUi_MainWindow()
ui7.setupUi(penYerSorguu)

penYerSorguu2 = QMainWindow()
ui8 = MyeeUi_MainWindow()
ui8.setupUi(penYerSorguu2)

# --------------------VERİTABANI-------------------#
# -------------------------------------------------#
import sqlite3

global curs
global conn
conn = sqlite3.connect('staj.db')  # Veritaban bağlantı kısmı
curs = conn.cursor()  # veri alışverişi


# --------------------CSV KISMI--------------------#
# -------------------------------------------------#
def OPENFILE():
    filename = QFileDialog.getOpenFileName(None, 'Open File', '(.csv)')
    if filename[0]:
        print(filename)
       # a, b = os.path.split(filename)
        with open(filename[0], 'r') as csv_file:
            with open("updated_test.csv", 'w') as f1:
                csv_file.readline()  # skip header line
                print(csv_file)
                an = datetime.datetime.now()
                for liness in csv_file:
                    lines = liness.split(";")
                    print(lines)
                    curs.execute("SELECT * FROM Form WHERE OgrNo=? AND OgrAdi=? ", \
                                 (lines[0], lines[1]))
                    conn.commit()
                    var = curs.fetchall()
                    if var:
                        print("Kayıt zaten var")
                    else:
                        curs.execute("INSERT INTO Form \
                                                   (OgrTC, OgrNo, OgrAdi, OgrSoyadi,OgrFak, OgrProg, OgrSinif,OgrEposta, OgrTel,StjDurum,StjBasT,StjBitT,StjSure,StjGun, FrmAdi,FrmAdres,FrmAlani,FrmPerSayi,FrmSGK,FrmTel,FrmEposta,YonAdi,YonSoyadi,YonGorev,YonEposta) \
                                                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
                                     (0, lines[0], lines[1], lines[2], lines[3], lines[4], lines[5],
                                      lines[6], lines[7], lines[8], an, an, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
                        conn.commit()
                cevap = QMessageBox.question(penAna, "DOSYA YÜKLE",
                                             "Dosya yükleme işleminiz başarıyla gerçekleşti.Lütfen yapmak istediğiniz işlemi menüden seçiniz", \
                                             QMessageBox.Ok)


# --------------------KULLANICIKAYIT-------------------#
# -------------------------------------------------#
def EKLE():
    _lneKulAdi = ui2.lneKulAdi.text()
    _lneKulSifre = ui2.lneKulSifre.text()

    curs.execute("INSERT INTO KullanıcıGiris (KulAdi,KulSifre) VALUES(?,?)", \
                 (_lneKulAdi, _lneKulSifre))
    conn.commit()
    cevap = QMessageBox.question(penAna, "GİRİŞ YAP", "Kayıt olduktan sonra lütfen giriş yapınız?")
    ui2.lneKulSifre.clear()


# --------------------KULLANICI GİRİŞ-------------------#
# -------------------------------------------------#

def GIRIS():
    _lneKulAdi = ui2.lneKulAdi.text()
    _lneKulSifre = ui2.lneKulSifre.text()
    curs.execute("SELECT * FROM KullanıcıGiris  WHERE KulAdi=? AND KulSifre=?", \
                 (_lneKulAdi, _lneKulSifre))
    conn.commit()
    results = curs.fetchall()
    if results:
        for i in results:
            penAna.show()
            penGiris.close()
    else:
        cevap = QMessageBox.question(penAna, "GİRİŞ YAP",
                                     "Kullanıcı Adı veya Şifre yanlış.Lütfen bilgilerinizi kontrol ediniz...")


# --------------------MENU SORGULA--------------------#
# -------------------------------------------------#

def OGRARA():
    penOgrSorguu.show()
    penYerSorguu2.close()
    penYerSorguu.close()
    penDonemSorggu.close()
    penAna.close()


def DONEMARA():
    #penDonemSorguu.show()
    penDonemSorggu.show()
    penOgrSorguu.close()
    penYerSorguu.close()
    penYerSorguu2.close()
    penAna.close()


def YERARA():
    penYerSorguu.show()
    penYerSorguu2.close()
    penOgrSorguu.close()
    penDonemSorggu.close()
    penAna.close()


def YERARA2():
    penYerSorguu2.show()
    penOgrSorguu.close()
    penDonemSorggu.close()
    penYerSorguu.close()
    penAna.close()


def CIKIS():
    print("çalışmadı")
    cevap = QMessageBox.question(penAna, "ÇIKIŞ", "Programdan çıkmak istediğinize emin misiniz?", \
                                 QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        conn.close()
        # sys.exit(Uygulama.closeAllWindows())
        sys.exit(Uygulama.exec_())  # uygulama ile ilgili tüm işlemleri kapattık

    else:
        print("kapatılmadı")
        # penOgrSorguu.show()



# --------------------ÖĞRENCİ ARA-------------------#
# -------------------------------------------------#

def OGRSORGU():
    _lneAdiSrg = ui3.lneAdiSrg.text()
    curs.execute("SELECT * FROM Form WHERE OgrAdi LIKE '%" + ui3.lneAdiSrg.text() + "%'")
    conn.commit()
    rows = curs.fetchall()

    if rows:
        OGRLISTELE()

    else:
        cevap = QMessageBox.question(penOgrSorguu, "ARAMA", "Böyle bir kayıt yok.Kaydetmek ister misiniz?", \
                                     QMessageBox.Yes | QMessageBox.No)
        if cevap == QMessageBox.Yes:
            penFormKayit.show()
            penOgrSorguu.close()
        else:
            penOgrSorguu.show()


penOgrSorguu.close()


# for row in rows:


# --------------------ÖĞRENCİ LİSTELE-------------------#
# -------------------------------------------------#
def OGRLISTELE():
    ui3.tblwOgrSorgu.clear()
    cevap = QMessageBox.question(penOgrSorguu, "ÖĞRENCİ LİSTELE",
                                 "Listelenen öğrencilerden, hakkında işlem yapmak istediğiniz öğrencinin SATIR NUMARASINI seçerek işlem yapınız...")
    _lneAdiSrg = ui3.lneAdiSrg.text()
    ui3.tblwOgrSorgu.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui3.tblwOgrSorgu.setHorizontalHeaderLabels(
        ('No', 'Öğrenci Adı', 'Öğrenci Soyadı', 'Öğrenci TC', 'Öğrenci Numarası', ' Öğrenci Fakülte', \
         'Öğrenci Bölüm', 'Öğrenci Sınıf', 'Öğrenci E-posta', 'Öğrenci Telefon', 'Staj Durum', \
         'Staj Başlangıç Tarihi', 'Staj Bitiş Tarihi', 'Staj Süre', 'Staj Gün', 'Firma Adı', \
         'Firma Adres', 'Firma Alanı', 'Firma Personel Sayısı', 'Firma SGK No', 'Firma Telefon', \
         'Firma E-posta', 'Yönetici Adı', 'Yönetici Soyadı', 'Yönetici Görev', 'Yönetici E-posta'))

    curs.execute("SELECT * FROM Form WHERE OgrAdi LIKE '%" + ui3.lneAdiSrg.text() + "%'")
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui3.tblwOgrSorgu.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))


# --------------------ÖĞRENCİ DOLDUR-------------------#
# -------------------------------------------------#
def OGRDOLDUR():
    # cevap = QMessageBox.question(penOgrSorguu, "ÖĞRENCİ LİSTELE",  "Listelenen öğrencilerden, hakkında işlem yapmak istediğiniz öğrencinin SATIR NUMARASINI seçerek işlem yapınız...")
    secili = ui3.tblwOgrSorgu.selectedItems()
    if secili:
        penFormGuncelle.show()
        _gunler = []
        ui5.lneOgrAdi.setText(secili[1].text())
        ui5.lneOgrSoyadi.setText(secili[2].text())
        ui5.lneTC.setText(secili[3].text())
        ui5.lneOgrNo.setText(secili[4].text())
        ui5.lneOkul.setText(secili[5].text())
        ui5.lnePrgAdi.setText(secili[6].text())
        ui5.lneOgrYil.setText(secili[7].text())
        ui5.lneEposta.setText(secili[8].text())
        ui5.lneOgrTel.setText(secili[9].text())
        if secili[10].text() == "Başarılı":
            ui5.rdbBsr.setChecked(True)
        if secili[10].text() == "Başarısız":
            ui5.rdbBsrz.setChecked(True)
        if secili[11].text() != 0:
            # #tarih = secili[11].text()
            ##yil = int(tarih[0:4])
            ##ay = int(tarih[5:7])
            ##gun = int(tarih[8:10])
            yil = int(secili[11].text()[0:4])
            ay = int(secili[11].text()[5:7])
            gun = int(secili[11].text()[8:10])
            ui5.dteStjBasT.setDate(QtCore.QDate(yil, ay, gun))
            # #ui.dteStjBasT.setDate(QtCore.QDate.currentDate())
        else:
            print("Yeni girilecek")

        if secili[12].text() != 0:
            yil = int(secili[12].text()[0:4])
            ay = int(secili[12].text()[5:7])
            gun = int(secili[12].text()[8:10])
            ui5.dteStjBitT.setDate(QtCore.QDate(yil, ay, gun))
        else:
            print("Yeni girilecek")

        ui5.lneStjSure.setText(secili[13].text())
        for gun in secili[14].text():
            if gun == "Pazartesi":
                ui5.chbPzt.setChecked(True)
            if gun == "Salı":
                ui5.chbSal.setChecked(True)
            if gun == "Çarşamba":
                ui5.chbCar.setChecked(True)
            if gun == "Perşembe":
                ui5.chbPer.setChecked(True)
            if gun == "Cuma":
                ui5.chbCum.setChecked(True)
            if gun == "Cumartesi":
                ui5.chbCmt.setChecked(True)

        ui5.cmbFrmAdi.setCurrentText(secili[15].text())
        ui5.cmbFrmAdres.setCurrentText(secili[16].text())
        ui5.lneFrmAlani.setText(secili[17].text())
        ui5.lneFrmPersai.setText(secili[18].text())
        ui5.lneFrmSgkNo.setText(secili[19].text())
        ui5.lneFrmTel.setText(secili[20].text())
        ui5.lneFrmEposta.setText(secili[21].text())
        ui5.lneYonAdi.setText(secili[22].text())
        ui5.lneYonSoyadi.setText(secili[23].text())
        ui5.lneYonGorev.setText(secili[24].text())
        ui5.lneYonEposta.setText(secili[25].text())

        penOgrSorguu.close()
        cevap = QMessageBox.question(penAna, "STAJ DURUM",
                                     "Lütfen staj durumu kısmını boş bırakmayınız.", \
                                     QMessageBox.Ok)




# --------------------KAYIT--------------------#
# -------------------------------------------------#

def KAYIT():
    _gunler = []
    _lneOgrAdi = ui4.lneOgrAdi.text()
    _lneOgrSoyadi = ui4.lneOgrSoyadi.text()
    _lneTC = ui4.lneTC.text()
    _lneOgrNo = ui4.lneOgrNo.text()
    _lneEposta = ui4.lneEposta.text()
    _lneFakulte = ui4.lneOkul.text()
    _lneBolum = ui4.lnePrgAdi.text()
    _lneSinif = ui4.lneOgrYil.text()
    _lneOgrTel = ui4.lneOgrTel.text()
    _lneEposta = ui4.lneEposta.text()
    _cmbFrmAdres = ui4.cmbFrmAdres.currentText()
    _cmbFrmAdi = ui4.cmbFrmAdi.currentText()
    _lneFrmAlan = ui4.lneFrmAlani.text()
    _lneFrmPerSayi = ui4.lneFrmPersai.text()
    _lneFrmSgk = ui4.lneFrmSgkNo.text()
    _lneFrmEposta = ui4.lneFrmEposta.text()
    _lneFrmTel = ui4.lneFrmTel.text()
    _lneYonAdi = ui4.lneYonAdi.text()
    _lneYonSoyadi = ui4.lneYonSoyadi.text()
    _lneYonGorev = ui4.lneYonGorev.text()
    _lneYonEposta = ui4.lneYonEposta.text()
    _dteStjBasT = ui4.dteStjBasT.date().toString(QtCore.Qt.ISODate)
    _dteStjBitT = ui4.dteStjBitT.date().toString(QtCore.Qt.ISODate)
    _lneStjSure = ui4.lneStjSure.text()
    if ui4.chbPzt.isChecked():
        _chbPzt = "Pazartesi"
        _gunler.append(_chbPzt)
    if ui4.chbSal.isChecked():
        _chbSal = "Salı"
        _gunler.append(_chbSal)
    if ui4.chbCar.isChecked():
        _chbCar = "Çarşamba"
        _gunler.append(_chbCar)
    if ui4.chbPer.isChecked():
        _chbPer = "Perşembe"
        _gunler.append(_chbPer)
    if ui4.chbCum.isChecked():
        _chbCum = "Cuma"
        _gunler.append(_chbCum)
    if ui4.chbCmt.isChecked():
        _chbCmt = "Cumartesi"
        _gunler.append(_chbCmt)
    if ui4.rdbBsr.isChecked():
        _StjDurum = "Başarılı"
    if ui4.rdbBsrz.isChecked():
        _StjDurum = "Başarısız"

    curs.execute("INSERT INTO Form \
                 (OgrTC,OgrNo, OgrAdi, OgrSoyadi,OgrFak, OgrProg, OgrSinif,OgrEposta, OgrTel,StjDurum,StjBasT,StjBitT,StjSure,StjGun, FrmAdi,FrmAdres,FrmAlani,FrmPerSayi,FrmSGK,FrmTel,FrmEposta,YonAdi,YonSoyadi,YonGorev,YonEposta) \
                 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                 (_lneTC, _lneOgrNo, _lneOgrAdi, _lneOgrSoyadi, _lneFakulte, _lneBolum, _lneSinif, _lneEposta,
                  _lneOgrTel, _StjDurum, _dteStjBasT, _dteStjBitT, _lneStjSure, str(_gunler), _cmbFrmAdi, _cmbFrmAdres,
                  _lneFrmAlan, _lneFrmPerSayi, _lneFrmSgk, _lneFrmTel, _lneFrmEposta, _lneYonAdi, _lneYonSoyadi,
                  _lneYonGorev, _lneYonEposta))

    conn.commit()




# --------------------DOLDUR-------------------#
# -------------------------------------------------#
def GUNCELLE():
    secili = ui3.tblwOgrSorgu.selectedItems()
    secim = ui9.tblwDonOgr.selectedItems()
    if secili:
        # for row in secili:
        _Id = int(secili[0].text())
        _gunler = []
        _lneOgrAdi = ui5.lneOgrAdi.text()
        _lneOgrSoyadi = ui5.lneOgrSoyadi.text()
        _lneTC = ui5.lneTC.text()
        _lneOgrNo = ui5.lneOgrNo.text()
        _lneEposta = ui5.lneEposta.text()
        _lneFakulte = ui5.lneOkul.text()
        _lneBolum = ui5.lnePrgAdi.text()
        _lneSinif = ui5.lneOgrYil.text()
        _lneOgrTel = ui5.lneOgrTel.text()
        _lneEposta = ui5.lneEposta.text()
        _cmbFrmAdres = ui5.cmbFrmAdres.currentText()
        _cmbFrmAdi = ui5.cmbFrmAdi.currentText()
        _lneFrmAlan = ui5.lneFrmAlani.text()
        _lneFrmPerSayi = ui5.lneFrmPersai.text()
        _lneFrmSgk = ui5.lneFrmSgkNo.text()
        _lneFrmEposta = ui5.lneFrmEposta.text()
        _lneFrmTel = ui5.lneFrmTel.text()
        _lneYonAdi = ui5.lneYonAdi.text()
        _lneYonSoyadi = ui5.lneYonSoyadi.text()
        _lneYonGorev = ui5.lneYonGorev.text()
        _lneYonEposta = ui5.lneYonEposta.text()
        _dteStjBasT = ui5.dteStjBasT.dateTime().toString(QtCore.Qt.ISODate)
        _dteStjBitT = ui5.dteStjBitT.dateTime().toString(QtCore.Qt.ISODate)
        _lneStjSure = ui5.lneStjSure.text()
        if ui5.chbPzt.isChecked():
            _chbPzt = "Pazartesi"
            _gunler.append(_chbPzt)
        if ui5.chbSal.isChecked():
            _chbSal = "Salı"
            _gunler.append(_chbSal)
        if ui5.chbCar.isChecked():
            _chbCar = "Çarşamba"
            _gunler.append(_chbCar)
        if ui5.chbPer.isChecked():
            _chbPer = "Perşembe"
            _gunler.append(_chbPer)
        if ui5.chbCum.isChecked():
            _chbCum = "Cuma"
            _gunler.append(_chbCum)
        if ui5.chbCmt.isChecked():
            _chbCmt = "Cumartesi"
            _gunler.append(_chbCmt)
        if ui5.rdbBsr.isChecked():
            _StjDurum = "Başarılı"
        if ui5.rdbBsrz.isChecked():
            _StjDurum = "Başarısız"
        else:
            _StjDurum = 0
        curs.execute(
            "UPDATE Form SET OgrTC=?, OgrNo=?, OgrAdi=?, OgrSoyadi=?, OgrFak=?, OgrProg=?, OgrSinif=?, OgrEposta=?, OgrTel=?, StjDurum=?, StjBasT=?, StjBitT=?, StjSure=?, StjGun=?, FrmAdi=?, FrmAdres=?, FrmAlani=?, FrmPerSayi=?, FrmSGK=?, FrmTel=?, FrmEposta=?, YonAdi=?, YonSoyadi=?, YonGorev=?, YonEposta=? WHERE OgrId=?", \
            (
                _lneTC, _lneOgrNo, _lneOgrAdi, _lneOgrSoyadi, _lneFakulte, _lneBolum, _lneSinif, _lneEposta,
                _lneOgrTel,
                _StjDurum, _dteStjBasT, _dteStjBitT, _lneStjSure, str(_gunler), _cmbFrmAdi, _cmbFrmAdres,
                _lneFrmAlan,
                _lneFrmPerSayi, _lneFrmSgk, _lneFrmTel, _lneFrmEposta, _lneYonAdi, _lneYonSoyadi, _lneYonGorev,
                _lneYonEposta, _Id))

        conn.commit()
        cevap = QMessageBox.question(penAna, "GÜNCELLE", "Güncelleme işleminiz Başarılı bir şekilde gerçekleşti.", \
                                     QMessageBox.Ok)
        if cevap == QMessageBox.Ok:
            penFormGuncelle.close()
            penDonemSorggu.close()
            penOgrSorguu.show()
           # _lneAdiSrg = ui3.lneAdiSrg.text()
            #if _lneAdiSrg:
                #OGRSORGU()


    if secim:
        _Id = int(secim[0].text())
        _gunler = []
        _lneOgrAdi = ui5.lneOgrAdi.text()
        _lneOgrSoyadi = ui5.lneOgrSoyadi.text()
        _lneTC = ui5.lneTC.text()
        _lneOgrNo = ui5.lneOgrNo.text()
        _lneEposta = ui5.lneEposta.text()
        _lneFakulte = ui5.lneOkul.text()
        _lneBolum = ui5.lnePrgAdi.text()
        _lneSinif = ui5.lneOgrYil.text()
        _lneOgrTel = ui5.lneOgrTel.text()
        _lneEposta = ui5.lneEposta.text()
        _cmbFrmAdres = ui5.cmbFrmAdres.currentText()
        # _cmbFrmAdresT = ui4.cmbFrmAdres.currentText()
        # _cmbFrmAdiT=ui4.cmbFrmAdi.Text()
        # _cmbFrmAdi = ui4.cmbFrmAdi.addItem()
        _cmbFrmAdi = ui5.cmbFrmAdi.currentText()
        _lneFrmAlan = ui5.lneFrmAlani.text()
        _lneFrmPerSayi = ui5.lneFrmPersai.text()
        _lneFrmSgk = ui5.lneFrmSgkNo.text()
        _lneFrmEposta = ui5.lneFrmEposta.text()
        _lneFrmTel = ui5.lneFrmTel.text()
        _lneYonAdi = ui5.lneYonAdi.text()
        _lneYonSoyadi = ui5.lneYonSoyadi.text()
        _lneYonGorev = ui5.lneYonGorev.text()
        _lneYonEposta = ui5.lneYonEposta.text()
        _dteStjBasT = ui5.dteStjBasT.dateTime().toString(QtCore.Qt.ISODate)
        _dteStjBitT = ui5.dteStjBitT.dateTime().toString(QtCore.Qt.ISODate)
        _lneStjSure = ui5.lneStjSure.text()
        if ui5.chbPzt.isChecked():
            _chbPzt = "Pazartesi"
            _gunler.append(_chbPzt)
        if ui5.chbSal.isChecked():
            _chbSal = "Salı"
            _gunler.append(_chbSal)
        if ui5.chbCar.isChecked():
            _chbCar = "Çarşamba"
            _gunler.append(_chbCar)
        if ui5.chbPer.isChecked():
            _chbPer = "Perşembe"
            _gunler.append(_chbPer)
        if ui5.chbCum.isChecked():
            _chbCum = "Cuma"
            _gunler.append(_chbCum)
        if ui5.chbCmt.isChecked():
            _chbCmt = "Cumartesi"
            _gunler.append(_chbCmt)
        if ui5.rdbBsr.isChecked():
            _StjDurum = "Başarılı"
        if ui5.rdbBsrz.isChecked():
            _StjDurum = "Başarısız"
        else:
            _StjDurum = 0
        curs.execute(
            "UPDATE Form SET OgrTC=?, OgrNo=?, OgrAdi=?, OgrSoyadi=?, OgrFak=?, OgrProg=?, OgrSinif=?, OgrEposta=?, OgrTel=?, StjDurum=?, StjBasT=?, StjBitT=?, StjSure=?, StjGun=?, FrmAdi=?, FrmAdres=?, FrmAlani=?, FrmPerSayi=?, FrmSGK=?, FrmTel=?, FrmEposta=?, YonAdi=?, YonSoyadi=?, YonGorev=?, YonEposta=? WHERE OgrId=?", \
            (
                _lneTC, _lneOgrNo, _lneOgrAdi, _lneOgrSoyadi, _lneFakulte, _lneBolum, _lneSinif, _lneEposta, _lneOgrTel,
                _StjDurum, _dteStjBasT, _dteStjBitT, _lneStjSure, str(_gunler), _cmbFrmAdi, _cmbFrmAdres, _lneFrmAlan,
                _lneFrmPerSayi, _lneFrmSgk, _lneFrmTel, _lneFrmEposta, _lneYonAdi, _lneYonSoyadi, _lneYonGorev,
                _lneYonEposta, _Id))

        conn.commit()
        cevapp = QMessageBox.question(penAna, "GÜNCELLE", "Güncelleme işleminiz Başarılı bir şekilde gerçekleşti.", \
                                     QMessageBox.Ok)
        if cevapp == QMessageBox.Ok:
            penFormGuncelle.close()
            penOgrSorguu.close()
            penDonemSorggu.show()




# --------------------DÖNEM SORGU------------------#
# -------------------------------------------------#
def DONEMSORGU():
    #_lneDonBas = int(ui6.lneDonBas.text())
    #_lneDonBit = int(ui6.lneDonBit.text())
    _lneDonBas = int(ui9.lneDonYil.text()[0:4])
    _lneDonBit = int(ui9.lneDonYil.text()[5:9])
    basAy = int(1)
    basGun = int(1)
    sonAy = int(12)
    sonGun = int(31)
    donBas = date(_lneDonBas, basAy, basGun).isoformat()
    donBit = date(_lneDonBit, sonAy, sonGun).isoformat()
    curs.execute("SELECT * FROM Form WHERE StjBasT>=? AND StjBitT<=?", \
                 (donBas, donBit))
    conn.commit()
    rows = curs.fetchall()
    if rows:
        DONEMLISTELE()
    else:
        cevap = QMessageBox.question(penAna, "DONEM SORGU", "Bu tarihler arasında staj yapan öğrenci bulunmuyor.", \
                                     QMessageBox.Ok)






# --------------------DONEM LİSTELE--------------------#
# -------------------------------------------------#
def DONEMLISTELE():
    ui9.tblwDonOgr.clear()
    cevap = QMessageBox.question(penDonemSorggu, "DÖNEM LİSTELE",
                                 "Listelenen öğrencilerden, hakkında işlem yapmak istediğiniz öğrencinin SATIR NUMARASINI seçerek işlem yapınız...")
    #_lneDonBas = int(ui6.lneDonBas.text())
   # _lneDonBit = int(ui6.lneDonBit.text())
    _lneDonBas = int(ui9.lneDonYil.text()[0:4])
    _lneDonBit = int(ui9.lneDonYil.text()[5:9])
    basAy = int(1)
    basGun = int(1)
    sonAy = int(12)
    sonGun = int(31)
    donBas = date(_lneDonBas, basAy, basGun).isoformat()
    donBit = date(_lneDonBit, sonAy, sonGun).isoformat()
    ui9.tblwDonOgr.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui9.tblwDonOgr.setHorizontalHeaderLabels(
        ('No', 'Öğrenci Adı', 'Öğrenci Soyadı', 'Öğrenci TC', 'Öğrenci Numarası', ' Öğrenci Fakülte', \
         'Öğrenci Bölüm', 'Öğrenci Sınıf', 'Öğrenci E-posta', 'Öğrenci Telefon', 'Staj Durum', \
         'Staj Başlangıç Tarihi', 'Staj Bitiş Tarihi', 'Staj Süre', 'Staj Gün', 'Firma Adı', \
         'Firma Adres', 'Firma Alanı', 'Firma Personel Sayısı', 'Firma SGK No', 'Firma Telefon', \
         'Firma E-posta', 'Yönetici Adı', 'Yönetici Soyadı', 'Yönetici Görev', 'Yönetici E-posta'))
    # curs.execute("SELECT OgrAdi, OgrSoyadi FROM Form WHERE  strftime (StjBasT, '%Y')=? AND strftime(StjBitT, '%Y')=? BETWEEN "
    # "'_lneDonBas,' AND '_lneDonBit,' ")
    # curs.execute( "SELECT OgrAdi, OgrSoyadi FROM Form WHERE  strftime (StjBasT, '%Y')>=_lneDonBas AND strftime(StjBitT, '%Y')<=_lneDonBit  ")
    # curs.execute("SELECT OgrAdi, OgrSoyadi FROM Form WHERE  strftime ('%Y',StjBasT, 'unixepoch')>=? AND strftime( '%Y',StjBitT, 'unixepoch')<=? ",\
    # (_lneDonBas,_lneDonBit ))

    curs.execute("SELECT * FROM Form WHERE StjBasT>=? AND StjBitT<=?", \
                 (donBas, donBit))

    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui9.tblwDonOgr.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

    conn.commit()


def DONEMDOLDUR():
   # secim = ui6.tblwDonOgr.selectedItems()
   secim = ui9.tblwDonOgr.selectedItems()
   if secim:
    penFormGuncelle.show()
    _gunler = []
    ui5.lneOgrAdi.setText(secim[1].text())
    ui5.lneOgrSoyadi.setText(secim[2].text())
    ui5.lneTC.setText(secim[3].text())
    ui5.lneOgrNo.setText(secim[4].text())
    ui5.lneOkul.setText(secim[5].text())
    ui5.lnePrgAdi.setText(secim[6].text())
    ui5.lneOgrYil.setText(secim[7].text())
    ui5.lneEposta.setText(secim[8].text())
    ui5.lneOgrTel.setText(secim[9].text())
    if secim[10].text() == "Başarılı":
        ui5.rdbBsr.setChecked(True)
    if secim[10].text() == "Başarısız":
        ui5.rdbBsrz.setChecked(True)
    if secim[11].text() != 0:
        # #tarih = secili[11].text()
        ##yil = int(tarih[0:4])
        ##ay = int(tarih[5:7])
        ##gun = int(tarih[8:10])
        yil = int(secim[11].text()[0:4])
        ay = int(secim[11].text()[5:7])
        gun = int(secim[11].text()[8:10])
        ui5.dteStjBasT.setDate(QtCore.QDate(yil, ay, gun))
        # #ui.dteStjBasT.setDate(QtCore.QDate.currentDate())
    else:
        print("Yeni girilecek")

    if secim[12].text() != 0:
        yil = int(secim[12].text()[0:4])
        ay = int(secim[12].text()[5:7])
        gun = int(secim[12].text()[8:10])
        ui5.dteStjBitT.setDate(QtCore.QDate(yil, ay, gun))
    else:
        print("Yeni girilecek")

    ui5.lneStjSure.setText(secim[13].text())
    for gun in secim[14].text():
        if gun == "Pazartesi":
            ui5.chbPzt.setChecked(True)
        if gun == "Salı":
            ui5.chbSal.setChecked(True)
        if gun == "Çarşamba":
            ui5.chbCar.setChecked(True)
        if gun == "Perşembe":
            ui5.chbPer.setChecked(True)
        if gun == "Cuma":
            ui5.chbCum.setChecked(True)
        if gun == "Cumartesi":
            ui5.chbCmt.setChecked(True)

    ui5.cmbFrmAdi.setCurrentText(secim[15].text())
    ui5.cmbFrmAdres.setCurrentText(secim[16].text())
    ui5.lneFrmAlani.setText(secim[17].text())
    ui5.lneFrmPersai.setText(secim[18].text())
    ui5.lneFrmSgkNo.setText(secim[19].text())
    ui5.lneFrmTel.setText(secim[20].text())
    ui5.lneFrmEposta.setText(secim[21].text())
    ui5.lneYonAdi.setText(secim[22].text())
    ui5.lneYonSoyadi.setText(secim[23].text())
    ui5.lneYonGorev.setText(secim[24].text())
    ui5.lneYonEposta.setText(secim[25].text())

    penDonemSorggu.close()
    cevap = QMessageBox.question(penAna, "STAJ DURUM","Lütfen staj durumu kısmını boş bırakmayınız.", QMessageBox.Ok)


# --------------------YER LİSTELE-------------------#
# -------------------------------------------------#
def YERLISTELE():
    _lneStjYerAdi = ui7.lneStjYerAdi.text().capitalize()
    # _lneYerIli = ui7.lneYerIli.text()
    ui7.tblwYerSorgu.clear()
    ui7.tblwYerSorgu.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui7.tblwYerSorgu.setHorizontalHeaderLabels(
        ('No', 'Öğrenci Adı', 'Öğrenci Soyadı', 'Öğrenci TC', 'Öğrenci Numarası', ' Öğrenci Fakülte', \
         'Öğrenci Bölüm', 'Öğrenci Sınıf', 'Öğrenci E-posta', 'Öğrenci Telefon', 'Staj Durum', \
         'Staj Başlangıç Tarihi', 'Staj Bitiş Tarihi', 'Staj Süre', 'Staj Gün', 'Firma Adı', \
         'Firma Adres', 'Firma Alanı', 'Firma Personel Sayısı', 'Firma SGK No', 'Firma Telefon', \
         'Firma E-posta', 'Yönetici Adı', 'Yönetici Soyadı', 'Yönetici Görev', 'Yönetici E-posta'))

    curs.execute("SELECT * FROM Form WHERE FrmAdi=?  ", \
                 (_lneStjYerAdi,))
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui7.tblwYerSorgu.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

    curs.execute("SELECT COUNT(*) FROM Form WHERE FrmAdi=? ", \
                 (_lneStjYerAdi,))
    kayitSayisi = curs.fetchone()
    ui7.lneStjYerOgrSayi.setText(str(kayitSayisi[0]))


# --------------------YER SORGU-------------------#
# -------------------------------------------------#
def YERSORGU():
    _lneStjYerAdi = ui7.lneStjYerAdi.text().capitalize()
    # _lneYerIli = ui7.lneYerIli.text()

    curs.execute("SELECT * FROM Form WHERE FrmAdi=? ", \
                 (_lneStjYerAdi,))  # virgül koymamın nedeni demet halinde alması virgül sayesinde parçalıyorum
    conn.commit()
    YERLISTELE()


# --------------------YER LİSTELE-------------------#
# -------------------------------------------------#
def YERLISTELE2():
    # _lneStjYerAdi = ui7.lneStjYerAdi.text()
    _lneStjYerIli = ui8.lneStjYerIli.text().upper()
    ui8.tblwYerSorgu.clear()
    ui8.tblwYerSorgu.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui8.tblwYerSorgu.setHorizontalHeaderLabels(
        ('No', 'Öğrenci Adı', 'Öğrenci Soyadı', 'Öğrenci TC', 'Öğrenci Numarası', ' Öğrenci Fakülte', \
         'Öğrenci Bölüm', 'Öğrenci Sınıf', 'Öğrenci E-posta', 'Öğrenci Telefon', 'Staj Durum', \
         'Staj Başlangıç Tarihi', 'Staj Bitiş Tarihi', 'Staj Süre', 'Staj Gün', 'Firma Adı', \
         'Firma Adres', 'Firma Alanı', 'Firma Personel Sayısı', 'Firma SGK No', 'Firma Telefon', \
         'Firma E-posta', 'Yönetici Adı', 'Yönetici Soyadı', 'Yönetici Görev', 'Yönetici E-posta'))

    curs.execute("SELECT * FROM Form WHERE FrmAdres=?  ", \
                 (_lneStjYerIli,))
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui8.tblwYerSorgu.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

    curs.execute("SELECT COUNT(*) FROM Form WHERE FrmAdres=? ", \
                 (_lneStjYerIli,))
    kayitSayisi = curs.fetchone()
    ui8.lneStjYerOgrSayi.setText(str(kayitSayisi[0]))


# --------------------YER SORGU-------------------#
# -------------------------------------------------#
def YERSORGU2():
    _lneStjYerIli = ui8.lneStjYerIli.text().upper()
    # _lneYerIli = ui7.lneYerIli.text()

    curs.execute("SELECT * FROM Form WHERE FrmAdres=? ", \
                 (_lneStjYerIli,))  # virgül koymamın nedeni demet halinde alması virgül sayesinde parçalıyorum
    conn.commit()
    YERLISTELE2()


# --------------------SİGNAL SLOT-------------------#
# -------------------------------------------------#
ui2.btnKulKayit.clicked.connect(EKLE)
ui2.btnGiris.clicked.connect(GIRIS)
ui.menuOgr.triggered.connect(OGRARA)
ui.menuStajDnm.triggered.connect(DONEMARA)
ui.menuStjYerAdi.triggered.connect(YERARA)
ui.menuStjYerIli.triggered.connect(YERARA2)
ui.menuCikis.triggered.connect(CIKIS)
ui3.menuOgr.triggered.connect(OGRARA)
ui3.menuStajDnm.triggered.connect(DONEMARA)
ui3.menuStjYerAdi.triggered.connect(YERARA)
ui3.menuStjYerIli.triggered.connect(YERARA2)
ui3.menuCikis.triggered.connect(CIKIS)
ui3.btnAra.clicked.connect(OGRSORGU)
ui3.tblwOgrSorgu.itemSelectionChanged.connect(OGRDOLDUR)
ui4.btnKaydet.clicked.connect(KAYIT)
ui5.btnGuncelle.clicked.connect(GUNCELLE)
ui7.menuOgr.triggered.connect(OGRARA)
ui7.menuStajDnm.triggered.connect(DONEMARA)
ui7.menuStjYerAdi.triggered.connect(YERARA)
ui7.menuStjYerIli.triggered.connect(YERARA2)
ui7.menuCikis.triggered.connect(CIKIS)
ui7.btnAra.clicked.connect(YERSORGU)
ui8.menuOgr.triggered.connect(OGRARA)
ui8.menuStajDnm.triggered.connect(DONEMARA)
ui8.menuStjYerAdi.triggered.connect(YERARA)
ui8.menuStjYerIli.triggered.connect(YERARA2)
ui8.menuCikis.triggered.connect(CIKIS)
ui8.btnAra.clicked.connect(YERSORGU2)
ui.btnYukle.clicked.connect(OPENFILE)
ui9.menuOgr.triggered.connect(OGRARA)
ui9.menuStajDnm.triggered.connect(DONEMARA)
ui9.menuStjYerAdi.triggered.connect(YERARA)
ui9.menuStjYerIli.triggered.connect(YERARA2)
ui9.menuCikis.triggered.connect(CIKIS)
ui9.btnAra_2.clicked.connect(DONEMSORGU)
ui9.tblwDonOgr.itemSelectionChanged.connect(DONEMDOLDUR)

sys.exit(Uygulama.exec_())  # uygulama ile ilgili tüm işlemleri kapattık
