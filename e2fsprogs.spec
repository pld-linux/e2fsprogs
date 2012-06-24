#
# Conditional build:
# _without_nls		- without NLS
# _with_allstatic	- link everything statically
#
Summary:	Utilities for managing the second extended (ext2) filesystem
Summary(cs):	N�stroje pro spr�vu souborov�ch syst�m� typu ext2
Summary(da):	V�rkt�jer til h�ndtering af ext2 filsystemer
Summary(de):	Dienstprogramme zum Verwalten des Second Extended-Dateisystems (ext2)
Summary(es):	Utilidades para la gesti�n de un sistema de ficheros ext2
Summary(fr):	Utilitaires pour la gestion du syst�me de fichiers ext2
Summary(id):	Utility untuk management filesystem ext2
Summary(is):	T�l til a� s�sla me� ext2 skr�arkerfi�
Summary(it):	Utility per la gestione del filesystem (ext2)
Summary(ja):	Second Extended (ext2) �ե����륷���ƥ��������뤿��Υ桼�ƥ���ƥ�
Summary(ko):	ext2 ���� �ý����� �����ϴ� ��ƿ��Ƽ
Summary(no):	Verkt�y for h�ndtering av ext2 filsystemet
Summary(pl):	Narz�dzia do systemu plikowego ext2
Summary(pt):	Utilit�rios para gerir o sistema de ficheiros ext2
Summary(pt_BR):	Ferramentas para o sistema de arquivos ext2
Summary(ru):	������� ���������� �������� �������� ext2
Summary(sk):	Pomocn� programy pre spr�vu ext2 s�borov�ho syst�mu
Summary(sl):	Pripomo�ki za upravljanje datote�nega sistema ext2
Summary(sv):	Verktyg f�r att hantera det andra ut�kade (ext2) filsystemet
Summary(tr):	ext2 dosya sistemi i�in ara�lar
Summary(uk):	���̦�� ��� ������ � �������� �������� ext2
Summary(zh_CN):	����ڶ���չ��ext2���ļ�ϵͳ�Ĺ��ߡ�
Summary(zh_TW):	�Ω�޲z ext2 �ɮרt�Ϊ��u��{���C
Name:		e2fsprogs
Version:	1.34
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/e2fsprogs/%{name}-%{version}.tar.gz
# Source0-md5:	9be9375224f0970a55e39ebebf2a0ce5
Source1:	http://opensource.captech.com/e2compr/ftp/e2compr-0.4.texinfo.gz
# Source1-md5:	c3c59ff37e49d8759abb1ef95a8d3abf
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source2-md5:	992a37783bd42a897232972917e8ca7d
Source3:	%{name}-pl.po
Patch0:		%{name}-info.patch
Patch1:		e2compr-info.patch
Patch2:		%{name}-nostrip.patch
URL:		http://e2fsprogs.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	texinfo
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libext2fs2

%description
The e2fsprogs package contains a number of utilities for creating,
checking, modifying and correcting any inconsistencies in second
extended (ext2) filesystems. e2fsprogs contains e2fsck (used to repair
filesystem inconsistencies after an unclean shutdown), mke2fs (used to
initialize a partition to contain an empty ext2 filesystem), debugfs
(used to examine the internal structure of a filesystem, to manually
repair a corrupted filesystem or to create test cases for e2fsck),
tune2fs (used to modify filesystem parameters) and most of the other
core ext2fs filesystem utilities.

%description -l cs
Bal��ek e2fsprogs obsahuje n�kolik program� pro vytv��en�, kontrolu
�pravy a opravy nekonzistenc� v syst�mech soubor� typu ext2 (second
extended filesystem). Bal��ek obsahuje program e2fsck (na opravy
nekonzistenc� syst�m� soubor�, kter� nebyly odpojeny p�i vypnut�
syst�mu), mke2fs (pro vytvo�en� pr�zdn�ho syst�mu soubor� typu ext2 v
diskov�m odd�lu), debugfs (pro kontrolu intern� struktury syst�mu
soubor�, manu�ln� opravu po�kozen�ho syst�mu soubor� a pro vytv��en�
testovac�ch p��pad� pro e2fsck), tune2fs (pro �pravu parametr� syst�mu
soubor�) a v�t�inu dal��ch program� pro pr�ci se syst�my soubor� typu
ext2fs.

%description -l da
e2fsprogs-pakken indeholder diverse v�rkt�jer for at lave,
kontrollere, modificere og reparere ext2-filsystemer. e2fsprogs
indeholder e2fsck (bruges for at reparere filsystemer efter uren
nedlukning af systemet), mke2fs (bruges for at initialisere en
partition med et tomt ext2-filsystem), debugfs (bruges for at
unders�ge de interne strukturer i filsystemet, for manuelt at kunne
reparere et �delagt filsystem eller lave testscenarier for e2fsck),
tune2fs (bruges for at modificere filsystem-parametre) og flere andre
v�rkt�jer for at �ndre og unders�ge ext2-filsystemer.

%description -l de
Das Paket e2fsprogs enth�lt eine Reihe von Dienstprogrammen zum
Anlegen, �berpr�fen, �ndern und Reparieren von Inkonsistenzen in
Second Extended-Dateisystemen (ext2). e2fsprogs enth�lt: e2fsck (zum
Korrigieren von Inkonsistenzen im Dateisystem nach einem
Computerabsturz), mke2fs (zum Initialisieren einer Partition mit einem
leeren ext2-Dateisystem), debugfs (zum �berpr�fen der internen
Struktur eines Dateisystems, zum manuellen Reparieren eines
besch�digten Dateisystems oder zum Erstellen von Testf�llen f�r
e2fsck), tune2fs (zum �ndern der Dateisystemparameter) und die meisten
anderen wichtigen Dienstprogramme f�r ext2fs-Dateisystemem.

%description -l es
El paquete e2fsprogs contiene varias utilidades para crear, controlar,
modificar y corregir las inconsistencias en un sistema de ficheros
ext2. e2fsprogs contiene e2fsck (resuelve el problema de
inconsistencia despu�s de haber apagado el ordenador de manera
incorrecta), mke2fs (inicializa una nueva partici�n para contener un
sistema de ficheros ext2 vac�o), debugfs (examina la estructura
interna de un sistema de ficheros para reparar manualmente los errores
presentes en un sistema de ficheros o crear casos de prueba para
e2fsck), tune2fs (modifica los par�metros del sistema de ficheros) y
la mayor�a de las utilidades principales del systema de ficheros
ext2fs.

%description -l fr
Le paquetage e2fsprogs contient plusieurs utilitaires permettant de
cr�er, v�rifier, modifier et corriger des incoh�rences dans des
syst�mes de fichiers de type ext2. e2fsprogs contient e2fsck
(r�paration d'incoh�rences de syst�me de fichiers apr�s un arr�t
brutal), mke2fs (initialisation d'une partition devant contenir un
syst�me de fichiers ext2 vide), debugfs (examen de la structure
interne d'un syst�me de fichiers afin de r�parer manuellement un
syst�me de fichiers corrompu ou de cr�er des cas de test pour e2fsck),
tune2fs (modification des param�tres de syst�mes de fichiers) et la
plupart des autres utilitaires cl�s pour les syst�mes de fichiers
ext2fs.

%description -l id
Package e2fsprogs berisi beberapa utility untuk membuat, cek, merubah,
dan memperbaiki kerusakan, pada second extended (ext2) filesystem.
e2fsprogs berisi e2fsck (digunakan untuk memperbaiki filesystem
inconsistencies yang biasanya terjadi setelah unclean shutdown),
mke2fs (digunakan untuk membuat filesystem ext2 yang kosong), debugfs
(untuk memeriksa internal structure dari filesystem, dan secara manual
memperbaiki corrupted filesystem atau untuk membuat test cases untuk
e2fsck), tune2fs (untuk merubah parameter filesystem) dan kebanyakan
utility untuk filesystem ext2.

%description -l is
e2fsprogs pakkinn inniheldur nokkur forrit til a� b�a til, sko�a,
breyta og laga allar villur � Linux skr�arkerfinu (ext2). e2fsprogs
inniheldur e2fsck (nota� til a� laga villur � skr�arkerfinu eftir
vonda enduruppkeyrslu), mke2fs (nota� til a� undirb�a har�a disk t�flu
til a� innihalda t�mt ext2 skr�arkerfi), debugfs (nota� til a� sko�a
innihald t�ms ext2 skr�arkerfis, til a� handvirkt laga �n�tt
skr�arkerfi e�a til a� undirb�a tilraunir fyrir e2fsck)m tune2fs(nota�
til a� breyta skr�arkerfis m�guleikum) og flest �nnur ext2fs
skr�arkerfis forritum

%description -l it
Il pacchetto e2fsprogs contiene varie utility per creare, controllare,
modificare e correggere le inconsistenze in un filesystem ext2.
e2fsprogs contiene e2fsck (risolve le inconsistenze di un filesystem
dopo un arresto non corretto del calcolatore), mke2fs (inizializza una
nuova partizione per un filesystem ext2 vuoto), debugfs (esamina la
struttura interna di un filesystem, � usato per riparare manualmente
gli errori presenti in un filesystem e per creare casi di test per
e2fsck), tune2fs (modifica i parametri del filesystem) e molte delle
utility principali per il filesystem ext2fs.

%description -l ja
e2fsprogs �ѥå������ˤ� Second Extended (ext2) �ե����륷���ƥ��
�������������ѹ���Ԥä��ꡢ������������뤿��Υ桼�ƥ���ƥ���
��¿���ޤޤ�Ƥ��ޤ���e2fsprogs �ˤ� e2fsck (�۾ｪλ��˥ե�����
�����ƥ���������������)��mke2fs (�ѡ��ƥ��������������ƶ���
ext2 �ե����륷���ƥ���������)��debugfs (�ե����륷���ƥ������
��¤�򸡺�������»�����ե����륷���ƥ���ư�ǽ��������ꡢe2fsck
�ѤΥƥ��ȥ��������������)��tune2fs (�ե����륷���ƥ�Υѥ�᡼��
���ѹ�����) �Τۤ������ ext2fs �ե����륷���ƥ�桼�ƥ���ƥ���
�ۤȤ�ɤ��ޤޤ�ޤ���

%description -l no
e2fsprogs-pakken inneholder diverse verkt�y for � lage, kontrollere,
modifisere og reparere ext2-filsystemer. e2fsprogs inneholder e2fsck
(brukes for � reparere filsystemer etter uren nedkj�ring av systemet),
mke2fs (brukes for � initialisere en partisjon med et tomt
ext2-filsystem), debugfs (brukes for � unders�ke de interne
strukturene i filsystemet, for manuelt � kunne reparere et �delagt
filsystem eller lage testscenarier for e2fsck), tune2fs (brukes for �
modifisere filsystem-parametre) og flere andre verkt�y for � endre og
unders�ke ext2-filsystemer.

%description -l pl
Pakiet ten zawiera narz�dzia do tworzenia, sprawdzania i naprawiania
wolumen�w dyskowych z systemem plikowym ext2. e2fsprogs zawiera e2fsck
(u�ywany do naprawiania niesp�jno�ci w systemie plikowym po
niepoprawnym zamkni�ciu systemu), mke2fs (u�ywany do inicjacji
wolumen�w ext2), debugfs (u�ywany do sprawdzania wewn�trznej struktury
wolumen�w ext2, a tak�e do r�cznego naprawiania b��d�w), tune2fs
(u�ywany do modyfikacji parametr�w wolumen�w ext2) i kilka innych
narz�dzi do ext2.

%description -l pt
O pacote e2fsprogs cont�m uma quantidade de utilit�rios para criar,
verificar, modificar e corrigir algumas inconsist�ncias no sistema de
ficheiros ext2. O e2fsprogs cont�m o e2fsck (usado para reparar as
inconsist�ncias do sistema de ficheiros depois duma termina��o
for�ada), o mke2fs (usado para inicializar uma parti��o para esta
conter um sistema de ficheiros ext2 vazio), o debugfs (usado para
examinar a estrutura interna dum sistema de ficheiros, para reparar
manualmente um sistema de ficheiros corrompido ou para criar situa��es
de teste para o e2fsck), o tune2fs (usado para modificar os par�metros
do sistema de ficheiros) e a maioria dos outros utilit�rios de base do
sistema de ficheiros ext2.

%description -l pt_BR
Este pacote inclui v�rios utilit�rios para cria��o, checagem e reparo
de sistema de arquivos ext2.

%description -l ru
����� e2fsprogs �������� ������� ��� ��������, ��������, ��������� �
������������� ����������� ��������� �������� ������� ext2. e2fsprogs
�������� e2fsck (��� �������������� �������� ��������� �����
������������� ���������� ������), mke2fs (��� ������������� �������
��� �������� ������ �������� ������� ext2), debugfs (��������
���������� ��������� �������� ������� ��� ������� ��������������
������������ �������� ������� ��� �������� �������� �������� ���
e2fsck), tune2fs (��� ��������� ���������� �������� �������) �
��������� ������ ������ ��� �������� ������� ext2.

%description -l sk
Bal�k e2fsprogs obsahuje nieko�ko programov pre vytv�ranie, kontrolu,
zmenu a opravu nekonzistenci� na ext2 s�borovom syst�me. e2fsprogs
obsahuje e2fsck (pre opravu nekonzistentn�ch �dajov na s�borovom
syst�me po ne�istom ukon�en�), mke2fs (pre vytvorenie pr�zdneho
s�borov�ho syst�mu na diskovom oddieli), debugfs (pre sk�manie
vn�torn�ch �trukt�r s�borov�ho syst�mu, jeho ru�n� opravu alebo pre
vytvorenie testovac�ch pr�padov pre e2fsck), tune2fs (pre modifik�ciu
parametrov s�borov�ho syst�mu) a v��inu �al��ch z�kladn�ch pom�cok
pre pr�cu s ext2fs.

%description -l sv
Paketet e2fsprogs inneh�ller ett antal verktyg f�r att skapa,
kontrollera, modifiera och r�tta felaktigheter i det andra ut�kade
(ext2) filsystemet. e2fsprogs inneh�ller e2fsck (anv�nds f�r att
reparera felaktigheter efter en oren avst�ngning), mke2fs (anv�nds f�r
att initiera en partition att inneh�lla ett tomt ext2-filsystem),
debugfs (anv�nds f�r att unders�ka den interna strukturen i ett
filsystem, manuellt reparera trasiga filsystem eller skapa testfall
f�r e2fsck), tune2fs (anv�nds f�r att modifiera filsystemparametrar)
och de flesta andra basverktygen f�r filsystemet ext2fs.

%description -l tr
Bu paket, ext2 dosya sistemlerini yaratmak, onarmak, kontrol etmek ve
baz� parametrelerini de�i�tirmek i�in gerekli yaz�l�mlar� i�erir.

%description -l uk
����� e2fsprogs ͦ����� ��¦� ���̦� ��� ���������, ����צ���,
����Ʀ��æ� �� ����������� ����-���� ������� � �����צ� �����ͦ ext2.
e2fsprogs ͦ����� e2fsck (����������դ���� ��� ����������� �������
Ц��� "�����ϧ" ������� ������), mke2fs (��� �Φ���̦��æ� ���Ħ�� ��
��������� �������ϧ ������ϧ ������� ext2), debugfs (��� ��������
����Ҧ���ϧ ��������� ������ϧ �������, ������� ������� ���������ϧ
������ϧ ������� ��� ��� ��������� ���Ԧ� ��� e2fsck), tune2fs (���
����Ʀ��æ� �������Ҧ� ������ϧ �������) �� ¦��ۦ��� ����� �������
���̦� ��� ext2fs.

%description -l zh_CN
e2fsprogs ���������һЩʵ�ó������ڴ�������顢 �޸ĺ;���������չ
(ext2) �ļ�ϵͳ�е��κβ�ͳһ֮���� e2fsprogs ����
e2fsck�������ڷ������ػ����޸��ļ�ϵͳ�Ĳ�ͳһ֮������
mke2fs�����ڽ�������ʼ��Ϊ�����հ�ext2 �ļ�ϵͳ����
debugfs�����ڼ���ļ�ϵͳ���ڲ��ṹ���ֶ��޸����ƻ����ļ�ϵͳ��Ϊe2fsck
�������Է������� tune2fs�������޸��ļ�ϵͳ���������������������
ext2fs �ļ�ϵͳʵ�ó���

%package devel
Summary:	ext2 filesystem-specific libraries and headers
Summary(cs):	Knihovny a hlavi�kov� soubory pro syst�m soubor� ext2
Summary(da):	ext2 filsystemsspecifikke biblioteker og headerfiler
Summary(de):	Bibliotheken und Header-Dateien f�r ext2-Dateisysteme
Summary(es):	Bibliotecas y archivos de inclusi�n para e2fs
Summary(fr):	Biblioth�ques et en-t�tes sp�cifiques au syst�me de fichiers ext2
Summary(id):	Library dan file header untuk e2fsprogs
Summary(is):	A�ger�as�fn og hausaskr�r fyrir ext2 skr�arkerfi�
Summary(it):	Librerie e file header specifici per il filesystem ext2
Summary(ja):	ext2 �ե����륷���ƥ�˸�ͭ����Ū�饤�֥��ȥإå���
Summary(ko):	ext2 ���Ͻý���-���� ���� ���̺귯���� �����
Summary(no):	ext2 filsystemspesifikke bibliotek og headerfiler
Summary(pl):	Pliki nag��wkowe do bibliotek e2fs
Summary(pt):	Bibliotecas e ficheiros de inclus�o espec�ficos do sistema de ficheiros ext2
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para e2fs
Summary(ru):	���������� � ����� ���������� ��� ���������� ��������, ������������ ext2
Summary(sk):	Kni�nice a hlavi�kov� s�bory pre ext2-�pecifick� programy
Summary(sl):	Knji�nice in glave, specifi�ne datote�nemu sistemu ext2
Summary(sv):	ext2 filsystemspecifika bibliotek och huvuden
Summary(uk):	��̦���� ������ͦ��� �� ������ ��� ������ � ext2fs
Summary(zh_CN):	ext2 �ļ�ϵͳ���еľ�̬���ͷ�ļ���
Summary(zh_TW):	ext2 �ɮרt�ίS�w���R�A�禡�w�P���Y�C
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libext2fs2-devel

%description devel
e2fsprogs-devel contains the libraries and header files needed to
develop second extended (ext2) filesystem-specific programs.

%description devel -l cs
Bal��ek e2fsprogs-devel obsahuje knihovny a hlavi�kov� soubory
pot�ebn� pro v�voj program� pracuj�c�ch se syst�mem soubor� ext2
(second extended fs).

%description devel -l da
e2fsprogs-devel indeholder de headerfiler og biblioteker man beh�ver
for at udvikle programmer specielt rettet mod ext2-filsystemer.

%description devel -l de
Das Paket e2fsprogs-devel enth�lt die Bibliotheken und Header-Dateien,
die f�r die Entwicklung von Programmen f�r das Second
Extended-Dateisystem (ext2) erforderlich sind.

%description devel -l es
e2fsprogs-devel contiene las bibliotecas y los ficheros de cabecera
necesarios para desarrollar programas espec�ficos para el sistema de
ficheros ext2.

%description devel -l fr
e2fsprogs-devel contient les biblioth�ques et fichiers d'en-t�te
n�cessaires au d�veloppement de programmes sp�cifiques au syst�me de
fichiers ext2.

%description devel -l id
e2fsprogs-devel berisi library dan file header yang dibutuhkan untuk
develop program yang berkaitan dengan filesystem ext2.

%description devel -l is
e2fsprogs-devel inniheldur library og header skr�r sem �arf til a� b�a
til (ext2) skr�arsafns forrit

%description devel -l it
e2fsprogs-devel contiene le librerie e i file header necessari per
sviluppare programmi specifici per il filesystem ext2.

%description devel -l ja
e2fspgrogs-devel �ˤϡ�Second Extended (ext2) �ե����륷���ƥ�˸�ͭ
�Υץ�����ȯ���뤿���ɬ�פʥ饤�֥��ȥإå����ե����뤬�ޤޤ�
�Ƥ��ޤ���

%description devel -l no
e2fsprogs-devel inneholder de headerfiler og bibliotek man trenger for
� utvikle programmer spesielt rettet mot ext2-filsystemer.

%description devel -l pl
Pliki nag��wkowe i dokumentacja niezb�dne do tworzenia program�w
obs�uguj�cych e2fs.

%description devel -l pt
O pacote e2fsprogs-devel cont�m as bibliotecas e ficheiros de inclus�o
necess�rios para desenvolver programas espec�ficos do sistema de
ficheiros ext2.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para desenvolvimento de programas
espec�ficos para sistema de arquivo ext2.

%description devel -l ru
e2fsprogs-devel �������� ����������� ���������� � ����� ����������,
����������� ��� ���������� ��������, ������������ �������� �������
ext2.

%description devel -l sk
e2fsprogs-devel obsahuje kni�nice a hlavi�kov� s�bory potrebn� pre
v�voj programov pre ext2 s�borov� syst�m.

%description devel -l sv
e2fsprogs-devel inneh�ller bibliotek och huvudfiler som beh�vs f�r att
utveckla filsystemsspecifika program f�r det andra ut�kade (ext2)
filsystemet.

%description devel -l uk
e2fsprogs-devel ͦ����� ¦�̦����� �� ������, ����Ȧ�Φ ��� ���������
�������, �˦ �������� � �������� �������� ext2.

%description devel -l zh_CN
e2fsprogs-devel ��������������չ (ext2)
�ļ�ϵͳר�ó�������ĳ�����ͷ�ļ���

%package static
Summary:	ext2 filesystem-specific static libraries
Summary(cs):	Statick� knihovny pro syst�m soubor� ext2
Summary(da):	ext2 filsystemsspecifikke statiske biblioteker
Summary(de):	Statische Bibliotheken f�r ext2-Dateisysteme
Summary(es):	Bibliotecas estaticas para e2fs
Summary(fr):	Biblioth�ques statiques sp�cifiques au syst�me de fichiers ext2
Summary(it):	Librerie statiche specifici per il filesystem ext2
Summary(no):	ext2 filsystemspesifikke statiske bibliotek
Summary(pl):	Biblioteki statyczne do obs�ugi systemu plik�w ext2
Summary(pt):	Bibliotecas estaticas espec�ficos do sistema de ficheiros ext2
Summary(pt_BR):	Bibliotecas estaticas para e2fs
Summary(ru):	����������� ���������� ��� ���������� ��������, ������������ ext2
Summary(sk):	Statick� kni�nice a hlavi�kov� s�bory pre ext2-�pecifick� programy
Summary(sv):	ext2 filsystemspecifika statiska bibliotek
Summary(uk):	������Φ ¦�̦���� ������ͦ��� ��� ������ � ext2fs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries needed to develop ext2 filesystem-specific programs
statically linked with e2progs libs.

%description static -l de
Libraries zur Entwicklung von ext2-Dateisystemspezifischen Programmen
erforderlich sind.

%description static -l es
Bibliotecas estaticas para desarrollo de programas espec�ficos para
sistema de archivo ext2.

%description static -l pl
Biblioteki statyczne do obs�ugi e2fs niezb�dne do kompilacji program�w
statycznie skonsolidowanych (linkowanych) z bibliotekami do e2fs.

%description static -l pt_BR
Bibliotecas estaticas para desenvolvimento de programas espec�ficos
para sistema de arquivo ext2.

%description static -l ru
e2fsprogs-devel-static �������� ����������� ����������, �����������
��� ��������� ��������, ���������� � �������� �������� ext2.

%description static -l uk
e2fsprogs-devel-static ͦ����� ������Φ ¦�̦�����, ����Ȧ�Φ ���
��������� �������, �˦ �������� � �������� �������� ext2.

%package evms
Summary:	e2fs EVMS module
Summary(pl):	Modu� e2fs dla EVMS
Group:		Libraries
Requires:	%{name} = %{version}
Requires:	evms

%description evms
e2fs EVMS module.

%description evms -l pl
Modu� e2fs dla EVMS.

%prep
%setup	-q
%patch0 -p1
gunzip < %{SOURCE1} > doc/e2compr.texinfo
%patch1 -p1
%patch2 -p1

chmod u+w configure aclocal.m4 po/LINGUAS po/Makefile.in.in intl/Makefile.in

LINGUAS=$(cat po/LINGUAS)
echo "pl $LINGUAS" > po/LINGUAS
cp -f %{SOURCE3} po/pl.po

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-root-prefix="" \
	%{!?_without_nls:--enable-nls} \
	%{?_without_nls:--disable-nls} \
	%{?_with_allstatic:--disable-elf-shlibs} \
	%{!?_with_allstatic:--enable-elf-shlibs} \
	--enable-compression \
	--enable-htree \
	--enable-evms-11 \
	%{?_without_static:--enable-dynamic-e2fsck} \
	--enable-fsck \
	--disable-rpath

%{__make} libs LDFLAGS="%{rpmldflags}"
%{__make} progs LDFLAGS="%{rpmldflags}"
%{__make} docs LDFLAGS="%{rpmldflags}"
cd doc
makeinfo --no-split e2compr.texinfo
cd ..

%install
rm -rf $RPM_BUILD_ROOT
export PATH=/sbin:$PATH

echo "install-shlibs:" >> po/Makefile
echo "install-shlibs:" >> intl/Makefile

%{__make} install	DESTDIR=$RPM_BUILD_ROOT
%{__make} install-libs	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C po install	DESTDIR=$RPM_BUILD_ROOT

ln -sf e2fsck $RPM_BUILD_ROOT/sbin/fsck.ext2
ln -sf e2fsck $RPM_BUILD_ROOT/sbin/fsck.ext3
ln -sf mke2fs $RPM_BUILD_ROOT/sbin/mkfs.ext2

install doc/e2compr.info $RPM_BUILD_ROOT%{_infodir}

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

rm -f $RPM_BUILD_ROOT%{_mandir}/$a/man8/{mkfs,fsck}.ext[23].8*
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/$a/man8/fsck.ext2.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/$a/man8/fsck.ext3.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/$a/man8/mkfs.ext2.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/$a/man8/mkfs.ext3.8

%{!?_without_nls:%find_lang %{name}}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files %{!?_without_nls:-f %{name}.lang}
%defattr(644,root,root,755)
%doc ChangeLog README RELEASE-NOTES
%attr(755,root,root) /sbin/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%{!?_with_allstatic:%attr(755,root,root) /lib/lib*.so.*}
%{_mandir}/man[18]/*
%lang(fi) %{_mandir}/fi/man[18]/*
%lang(fr) %{_mandir}/fr/man[18]/*
%lang(hu) %{_mandir}/hu/man[18]/*
%lang(it) %{_mandir}/it/man[18]/*
%lang(ja) %{_mandir}/ja/man[18]/*
%lang(ko) %{_mandir}/ko/man[18]/*
%lang(pl) %{_mandir}/pl/man[18]/*
%{_datadir}/et
%{_datadir}/ss
%{_infodir}/e2compr.info*

%files devel
%defattr(644,root,root,755)
%doc doc/libblkid.txt
%{_infodir}/libext2fs.info*
%{_mandir}/man3/*
%lang(ja) %{_mandir}/ja/man3/*
%{_includedir}/*

%{!?_with_allstatic:%attr(755,root,root) %{_libdir}/lib*.so}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files evms
%defattr(644,root,root,755)
%attr(755,root,root) /lib/evms/*.so
