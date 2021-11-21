BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Form" (
	"OgrId"	INTEGER NOT NULL UNIQUE,
	"OgrAdi"	TEXT NOT NULL,
	"OgrSoyadi"	TEXT NOT NULL,
	"OgrTC"	TEXT NOT NULL,
	"OgrNo"	TEXT NOT NULL,
	"OgrFak"	TEXT NOT NULL,
	"OgrProg"	TEXT NOT NULL,
	"OgrSinif"	TEXT NOT NULL,
	"OgrEposta"	TEXT NOT NULL,
	"OgrTel"	TEXT NOT NULL,
	"StjDurum"	TEXT NOT NULL,
	"StjBasT"	TEXT NOT NULL,
	"StjBitT"	TEXT NOT NULL,
	"StjSure"	TEXT NOT NULL,
	"StjGun"	TEXT NOT NULL,
	"FrmAdi"	TEXT NOT NULL,
	"FrmAdres"	TEXT NOT NULL,
	"FrmAlani"	TEXT NOT NULL,
	"FrmPerSayi"	TEXT NOT NULL,
	"FrmSGK"	TEXT NOT NULL,
	"FrmTel"	TEXT NOT NULL,
	"FrmEposta"	TEXT NOT NULL,
	"YonAdi"	TEXT NOT NULL,
	"YonSoyadi"	TEXT NOT NULL,
	"YonGorev"	TEXT NOT NULL,
	"YonEposta"	TEXT NOT NULL,
	PRIMARY KEY("OgrId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "KullanıcıGiris" (
	"KulId"	INTEGER NOT NULL UNIQUE,
	"KulAdi"	TEXT NOT NULL,
	"KulSifre"	TEXT NOT NULL,
	PRIMARY KEY("KulId" AUTOINCREMENT)
);
INSERT INTO "Form" VALUES (89,'Ali','VELİ','0','1180505008','MÜH.FAK.','YAZILIM MÜH.','2','ali@outlook.com','5435362525','
','2020-10-02 15:01:59.922763','2020-10-02 15:01:59.922763','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (90,'Ahmet','AKPINAR','0','1180505014','MÜH.FAK.','YAZILIM MÜH.','2','ahmet5807@hotmail.com','5312153353','0','2020-10-02T00:00:00','2020-10-02T00:00:00','0','[]','Softtech','ANKARA','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (91,'Yasin','AKYASAN','0','1180505029','MÜH.FAK.','YAZILIM MÜH.','2','yasinakyasan1@outlook.com','5386807144','
','2020-10-02 15:01:59.922763','2020-10-02 15:01:59.922763','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (92,'BETÜL','ALKAN','0','1180505027','MÜH.FAK.','YAZILIM MÜH.','2','betulalkan14@gmail.com','5558655555','0','2020-10-02T00:00:00','2020-10-02T00:00:00','0','[]','Gittigidiyor','ANKARA','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (93,'AHMET EMRE','DENİZCİ','0','1180505042','MÜH.FAK.','YAZILIM MÜH.','2','ezelahmet2323@gmail.com','5433158747','0','2020-10-02T00:00:00','2020-10-02T00:00:00','0','[]','Softtech','ANKARA','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (94,'FATMA ZEHRA','ASLAN','0','1180505803','MÜH.FAK.','YAZILIM MÜH.','1','fatma.aslan.5454@gmail.com','5458745456','
','2020-10-02 15:01:59.922763','2020-10-02 15:01:59.922763','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (95,'ZEYNEL','AVKAROĞLU','0','1180505048','MÜH.FAK.','YAZILIM MÜH.','1','avkar47.zeyneL@gmail.com','5458724123','
','2020-10-02 15:01:59.922763','2020-10-02 15:01:59.922763','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (96,'NUMAN VEYSEL','AYAR','0','1180505043','MÜH.FAK.','YAZILIM MÜH.','1','nvayar@gmail.com','5074139321','
','2020-10-02 15:01:59.922763','2020-10-02 15:01:59.922763','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (97,'Muhammed','AYIRAN','0','1180505044','MÜH.FAK.','YAZILIM MÜH.','1','muhayiran@gmail.com','5524100529','
','2020-10-02 15:01:59.922763','2020-10-02 15:01:59.922763','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (98,'','','0','','','','','','','
','2020-10-02 15:01:59.922763','2020-10-02 15:01:59.922763','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (99,'','','0','*NORMALDE 80-100 arası öğrenci olacak bu listede','','','','','','
','2020-10-02 15:01:59.922763','2020-10-02 15:01:59.922763','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (100,'Arzu','VELİ','0','1180505008','MÜH.FAK.','YAZILIM MÜH.','2','ali@outlook.com','5435362525','
','2020-10-02 15:27:10.567229','2020-10-02 15:27:10.567229','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (101,'Yahya','AKPINAR','0','1180505014','MÜH.FAK.','YAZILIM MÜH.','2','ahmet5807@hotmail.com','5312153353','
','2020-10-02 15:27:10.567229','2020-10-02 15:27:10.567229','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (102,'Yeter','AKYASAN','0','1180505029','MÜH.FAK.','YAZILIM MÜH.','2','yasinakyasan1@outlook.com','5386807144','
','2020-10-02 15:27:10.567229','2020-10-02 15:27:10.567229','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (103,'Bebek','ALKAN','0','1180505027','MÜH.FAK.','YAZILIM MÜH.','2','betulalkan14@gmail.com','5558655555','
','2020-10-02 15:27:10.567229','2020-10-02 15:27:10.567229','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (104,'Aslan EMRE','DENİZCİ','0','1180505042','MÜH.FAK.','YAZILIM MÜH.','2','ezelahmet2323@gmail.com','5433158747','
','2020-10-02 15:27:10.567229','2020-10-02 15:27:10.567229','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (105,'FATOŞ ZEHRA','ASLAN','0','1180505803','MÜH.FAK.','YAZILIM MÜH.','1','fatma.aslan.5454@gmail.com','5458745456','
','2020-10-02 15:27:10.567229','2020-10-02 15:27:10.567229','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (106,'ZEYNEP','AVKAROĞLU','0','1180505048','MÜH.FAK.','YAZILIM MÜH.','1','avkar47.zeyneL@gmail.com','5458724123','
','2020-10-02 15:27:10.567229','2020-10-02 15:27:10.567229','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (107,'NURDAN VEYSEL','AYAR','0','1180505043','MÜH.FAK.','YAZILIM MÜH.','1','nvayar@gmail.com','5074139321','
','2020-10-02 15:27:10.567229','2020-10-02 15:27:10.567229','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "Form" VALUES (108,'Mesned','AYIRAN','0','1180505044','MÜH.FAK.','YAZILIM MÜH.','1','muhayiran@gmail.com','5524100529','
','2020-10-02 15:27:10.567229','2020-10-02 15:27:10.567229','0','0','0','0','0','0','0','0','0','0','0','0','0');
INSERT INTO "KullanıcıGiris" VALUES (1,'Olcay','Dark39');
INSERT INTO "KullanıcıGiris" VALUES (2,'Olcay','');
INSERT INTO "KullanıcıGiris" VALUES (3,'Olcay','Dark39');
INSERT INTO "KullanıcıGiris" VALUES (4,'Olcay','Dark39');
INSERT INTO "KullanıcıGiris" VALUES (5,'Olcay','Dark39');
COMMIT;
