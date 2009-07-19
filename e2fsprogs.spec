#
# Conditional build:
%bcond_with	allstatic	# link everything statically
%bcond_without	static		# link e2fsck dynamically with libc
%bcond_without	nls		# build without NLS
%bcond_without	initrd		# don't build initrd version
%bcond_with	uClibc		# link initrd version with static glibc instead of uClibc
%bcond_without	dietlibc	# link initrd version with dietlibc instead of uClibc
#
%ifarch sparc64 sparc
%undefine       with_uClibc
%endif
#
Summary:	Utilities for managing the second extended (ext2) filesystem
Summary(cs.UTF-8):	Nástroje pro správu souborových systémů typu ext2
Summary(da.UTF-8):	Værktøjer til håndtering af ext2 filsystemer
Summary(de.UTF-8):	Dienstprogramme zum Verwalten des Second Extended-Dateisystems (ext2)
Summary(es.UTF-8):	Utilidades para la gestión de un sistema de ficheros ext2
Summary(fr.UTF-8):	Utilitaires pour la gestion du système de fichiers ext2
Summary(id.UTF-8):	Utility untuk management filesystem ext2
Summary(is.UTF-8):	Tól til að sýsla með ext2 skráarkerfið
Summary(it.UTF-8):	Utility per la gestione del filesystem (ext2)
Summary(ja.UTF-8):	Second Extended (ext2) ファイルシステムを管理するためのユーティリティ
Summary(ko.UTF-8):	ext2 파일 시스템을 관리하는 유틸리티
Summary(nb.UTF-8):	Verktøy for håndtering av ext2 filsystemet
Summary(pl.UTF-8):	Narzędzia do systemu plikowego ext2
Summary(pt.UTF-8):	Utilitários para gerir o sistema de ficheiros ext2
Summary(pt_BR.UTF-8):	Ferramentas para o sistema de arquivos ext2
Summary(ru.UTF-8):	Утилиты управления файловой системой ext2
Summary(sk.UTF-8):	Pomocné programy pre správu ext2 súborového systému
Summary(sl.UTF-8):	Pripomočki za upravljanje datotečnega sistema ext2
Summary(sv.UTF-8):	Verktyg för att hantera det andra utökade (ext2) filsystemet
Summary(tr.UTF-8):	ext2 dosya sistemi için araçlar
Summary(uk.UTF-8):	Утиліти для роботи з файловою системою ext2
Summary(zh_CN.UTF-8):	管理第二扩展（ext2）文件系统的工具。
Summary(zh_TW.UTF-8):	用於管理 ext2 檔案系統的工具程式。
Name:		e2fsprogs
Version:	1.41.8
Release:	5
License:	GPL v2 (with LGPL v2 and BSD parts)
Group:		Applications/System
Source0:	http://dl.sourceforge.net/e2fsprogs/%{name}-%{version}.tar.gz
# Source0-md5:	6708cc8e484809fc5cfb232882e48489
Source1:	e2compr-0.4.texinfo.gz
# Source1-md5:	c3c59ff37e49d8759abb1ef95a8d3abf
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source2-md5:	992a37783bd42a897232972917e8ca7d
Patch0:		%{name}-info.patch
Patch1:		e2compr-info.patch
Patch2:		%{name}-498381.patch
Patch3:		%{name}-diet.patch
Patch4:		%{name}-external-libblkid.patch
Patch5:		%{name}-external-libuuid.patch
URL:		http://e2fsprogs.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.11
BuildRequires:	rpmbuild(macros) >= 1.426
BuildRequires:	texinfo
BuildRequires:	texinfo-texi2dvi
BuildRequires:	libblkid-devel
BuildRequires:	libuuid-devel
%if %{with allstatic}
BuildRequires:	glibc-static
%endif
%if %{with initrd}
	%if %{with uClibc}
BuildRequires:	uClibc-static >= 2:0.9.29
	%else
		%if %{with dietlibc}
BuildRequires:	dietlibc-static
BuildRequires:	libblkid-dietlibc
BuildRequires:	libuuid-dietlibc
		%else
BuildRequires:	glibc-static
		%endif
	%endif
%endif
Requires(post,postun):	/sbin/ldconfig
Requires:	fsck
Requires:	libcom_err = %{version}-%{release}
Obsoletes:	e2fsprogs-evms
Obsoletes:	libext2fs2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# changing CFLAGS in the middle confuses confcache
%undefine       configure_cache

# for some reason known only to rpm there must be "\\|" not "\|" here
%define		dietarch	%(echo %{_target_cpu} | sed -e 's/i.86\\|pentium.\\|athlon/i386/;s/amd64/x86_64/;s/armv.*/arm/')
%define		dietlibdir	%{_prefix}/lib/dietlibc/lib-%{dietarch}

%ifarch ppc ppc64
# for dietlibc
%define		filterout_ld	-Wl,-z,relro
%endif

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

%description -l cs.UTF-8
Balíček e2fsprogs obsahuje několik programů pro vytváření, kontrolu
úpravy a opravy nekonzistencí v systémech souborů typu ext2 (second
extended filesystem). Balíček obsahuje program e2fsck (na opravy
nekonzistencí systémů souborů, které nebyly odpojeny při vypnutí
systému), mke2fs (pro vytvoření prázdného systému souborů typu ext2 v
diskovém oddílu), debugfs (pro kontrolu interní struktury systému
souborů, manuální opravu poškozeného systému souborů a pro vytváření
testovacích případů pro e2fsck), tune2fs (pro úpravu parametrů systému
souborů) a většinu dalších programů pro práci se systémy souborů typu
ext2fs.

%description -l da.UTF-8
e2fsprogs-pakken indeholder diverse værktøjer for at lave,
kontrollere, modificere og reparere ext2-filsystemer. e2fsprogs
indeholder e2fsck (bruges for at reparere filsystemer efter uren
nedlukning af systemet), mke2fs (bruges for at initialisere en
partition med et tomt ext2-filsystem), debugfs (bruges for at
undersøge de interne strukturer i filsystemet, for manuelt at kunne
reparere et ødelagt filsystem eller lave testscenarier for e2fsck),
tune2fs (bruges for at modificere filsystem-parametre) og flere andre
værktøjer for at ændre og undersøge ext2-filsystemer.

%description -l de.UTF-8
Das Paket e2fsprogs enthält eine Reihe von Dienstprogrammen zum
Anlegen, Überprüfen, Ändern und Reparieren von Inkonsistenzen in
Second Extended-Dateisystemen (ext2). e2fsprogs enthält: e2fsck (zum
Korrigieren von Inkonsistenzen im Dateisystem nach einem
Computerabsturz), mke2fs (zum Initialisieren einer Partition mit einem
leeren ext2-Dateisystem), debugfs (zum Überprüfen der internen
Struktur eines Dateisystems, zum manuellen Reparieren eines
beschädigten Dateisystems oder zum Erstellen von Testfällen für
e2fsck), tune2fs (zum Ändern der Dateisystemparameter) und die meisten
anderen wichtigen Dienstprogramme für ext2fs-Dateisystemem.

%description -l es.UTF-8
El paquete e2fsprogs contiene varias utilidades para crear, controlar,
modificar y corregir las inconsistencias en un sistema de ficheros
ext2. e2fsprogs contiene e2fsck (resuelve el problema de
inconsistencia después de haber apagado el ordenador de manera
incorrecta), mke2fs (inicializa una nueva partición para contener un
sistema de ficheros ext2 vacío), debugfs (examina la estructura
interna de un sistema de ficheros para reparar manualmente los errores
presentes en un sistema de ficheros o crear casos de prueba para
e2fsck), tune2fs (modifica los parámetros del sistema de ficheros) y
la mayoría de las utilidades principales del systema de ficheros
ext2fs.

%description -l fr.UTF-8
Le paquetage e2fsprogs contient plusieurs utilitaires permettant de
créer, vérifier, modifier et corriger des incohérences dans des
systèmes de fichiers de type ext2. e2fsprogs contient e2fsck
(réparation d'incohérences de système de fichiers après un arrêt
brutal), mke2fs (initialisation d'une partition devant contenir un
système de fichiers ext2 vide), debugfs (examen de la structure
interne d'un système de fichiers afin de réparer manuellement un
système de fichiers corrompu ou de créer des cas de test pour e2fsck),
tune2fs (modification des paramètres de systèmes de fichiers) et la
plupart des autres utilitaires clés pour les systèmes de fichiers
ext2fs.

%description -l id.UTF-8
Package e2fsprogs berisi beberapa utility untuk membuat, cek, merubah,
dan memperbaiki kerusakan, pada second extended (ext2) filesystem.
e2fsprogs berisi e2fsck (digunakan untuk memperbaiki filesystem
inconsistencies yang biasanya terjadi setelah unclean shutdown),
mke2fs (digunakan untuk membuat filesystem ext2 yang kosong), debugfs
(untuk memeriksa internal structure dari filesystem, dan secara manual
memperbaiki corrupted filesystem atau untuk membuat test cases untuk
e2fsck), tune2fs (untuk merubah parameter filesystem) dan kebanyakan
utility untuk filesystem ext2.

%description -l is.UTF-8
e2fsprogs pakkinn inniheldur nokkur forrit til að búa til, skoða,
breyta og laga allar villur í Linux skráarkerfinu (ext2). e2fsprogs
inniheldur e2fsck (notað til að laga villur í skráarkerfinu eftir
vonda enduruppkeyrslu), mke2fs (notað til að undirbúa harða disk töflu
til að innihalda tómt ext2 skráarkerfi), debugfs (notað til að skoða
innihald tóms ext2 skráarkerfis, til að handvirkt laga ónýtt
skráarkerfi eða til að undirbúa tilraunir fyrir e2fsck)m tune2fs(notað
til að breyta skráarkerfis möguleikum) og flest önnur ext2fs
skráarkerfis forritum

%description -l it.UTF-8
Il pacchetto e2fsprogs contiene varie utility per creare, controllare,
modificare e correggere le inconsistenze in un filesystem ext2.
e2fsprogs contiene e2fsck (risolve le inconsistenze di un filesystem
dopo un arresto non corretto del calcolatore), mke2fs (inizializza una
nuova partizione per un filesystem ext2 vuoto), debugfs (esamina la
struttura interna di un filesystem, è usato per riparare manualmente
gli errori presenti in un filesystem e per creare casi di test per
e2fsck), tune2fs (modifica i parametri del filesystem) e molte delle
utility principali per il filesystem ext2fs.

%description -l ja.UTF-8
e2fsprogs パッケージには Second Extended (ext2) ファイルシステムの
作成、検査、変更を行ったり、不整合を修復するためのユーティリティが
数多く含まれています。e2fsprogs には e2fsck (異常終了後にファイル
システムの不整合を修復する)、mke2fs (パーティションを初期化して空の
ext2 ファイルシステムを作成する)、debugfs (ファイルシステムの内部
構造を検査し、破損したファイルシステムを手動で修復したり、e2fsck
用のテストケースを作成する)、tune2fs (ファイルシステムのパラメータ
を変更する) のほか、主な ext2fs ファイルシステムユーティリティの
ほとんどが含まれます。

%description -l nb.UTF-8
e2fsprogs-pakken inneholder diverse verktøy for å lage, kontrollere,
modifisere og reparere ext2-filsystemer. e2fsprogs inneholder e2fsck
(brukes for å reparere filsystemer etter uren nedkjøring av systemet),
mke2fs (brukes for å initialisere en partisjon med et tomt
ext2-filsystem), debugfs (brukes for å undersøke de interne
strukturene i filsystemet, for manuelt å kunne reparere et ødelagt
filsystem eller lage testscenarier for e2fsck), tune2fs (brukes for å
modifisere filsystem-parametre) og flere andre verktøy for å endre og
undersøke ext2-filsystemer.

%description -l pl.UTF-8
Pakiet ten zawiera narzędzia do tworzenia, sprawdzania i naprawiania
wolumenów dyskowych z systemem plikowym ext2. e2fsprogs zawiera e2fsck
(używany do naprawiania niespójności w systemie plikowym po
niepoprawnym zamknięciu systemu), mke2fs (używany do inicjacji
wolumenów ext2), debugfs (używany do sprawdzania wewnętrznej struktury
wolumenów ext2, a także do ręcznego naprawiania błędów), tune2fs
(używany do modyfikacji parametrów wolumenów ext2) i kilka innych
narzędzi do ext2.

%description -l pt.UTF-8
O pacote e2fsprogs contém uma quantidade de utilitários para criar,
verificar, modificar e corrigir algumas inconsistências no sistema de
ficheiros ext2. O e2fsprogs contém o e2fsck (usado para reparar as
inconsistências do sistema de ficheiros depois duma terminação
forçada), o mke2fs (usado para inicializar uma partição para esta
conter um sistema de ficheiros ext2 vazio), o debugfs (usado para
examinar a estrutura interna dum sistema de ficheiros, para reparar
manualmente um sistema de ficheiros corrompido ou para criar situações
de teste para o e2fsck), o tune2fs (usado para modificar os parâmetros
do sistema de ficheiros) e a maioria dos outros utilitários de base do
sistema de ficheiros ext2.

%description -l pt_BR.UTF-8
Este pacote inclui vários utilitários para criação, checagem e reparo
de sistema de arquivos ext2.

%description -l ru.UTF-8
Пакет e2fsprogs содержит утилиты для создания, проверки, изменения и
корректировки внутреннего состояния файловой системы ext2. e2fsprogs
содержит e2fsck (для восстановления файловой структуры после
некорректного завершения работы), mke2fs (для инициализации раздела
при создании пустой файловой системы ext2), debugfs (просмотр
внутренней структуры файловой системы для ручного восстановления
поврежденной файловой системы или создания тестовых ситуаций для
e2fsck), tune2fs (для изменения параметров файловой системы) и
множество других утилит для файловой системы ext2.

%description -l sk.UTF-8
Balík e2fsprogs obsahuje niekoľko programov pre vytváranie, kontrolu,
zmenu a opravu nekonzistencií na ext2 súborovom systéme. e2fsprogs
obsahuje e2fsck (pre opravu nekonzistentných údajov na súborovom
systéme po nečistom ukončení), mke2fs (pre vytvorenie prázdneho
súborového systému na diskovom oddieli), debugfs (pre skúmanie
vnútorných štruktúr súborového systému, jeho ručnú opravu alebo pre
vytvorenie testovacích prípadov pre e2fsck), tune2fs (pre modifikáciu
parametrov súborového systému) a väčšinu ďalších základných pomôcok
pre prácu s ext2fs.

%description -l sv.UTF-8
Paketet e2fsprogs innehåller ett antal verktyg för att skapa,
kontrollera, modifiera och rätta felaktigheter i det andra utökade
(ext2) filsystemet. e2fsprogs innehåller e2fsck (används för att
reparera felaktigheter efter en oren avstängning), mke2fs (används för
att initiera en partition att innehålla ett tomt ext2-filsystem),
debugfs (används för att undersöka den interna strukturen i ett
filsystem, manuellt reparera trasiga filsystem eller skapa testfall
för e2fsck), tune2fs (används för att modifiera filsystemparametrar)
och de flesta andra basverktygen för filsystemet ext2fs.

%description -l tr.UTF-8
Bu paket, ext2 dosya sistemlerini yaratmak, onarmak, kontrol etmek ve
bazı parametrelerini değiştirmek için gerekli yazılımları içerir.

%description -l uk.UTF-8
Пакет e2fsprogs містить набір утиліт для створення, перевірки,
модифікації та виправлення будь-яких помилок у файловій системі ext2.
e2fsprogs містить e2fsck (використовується для виправлення помилок
після "брудної" зупинки машини), mke2fs (для ініциалізації розділу та
створення порожньої файлової системи ext2), debugfs (для вивчення
внутрішньої структури файлової системи, ручного ремонту пошкодженої
файлової системи або для створення тестів для e2fsck), tune2fs (для
модифікації параметрів файлової системи) та більшість інших базових
утиліт для ext2fs.

%description -l zh_CN.UTF-8
e2fsprogs 软件包包含一些实用程序，用于创建、检查、 修改和纠正辅助扩展
(ext2) 文件系统中的任何不统一之处。 e2fsprogs 包含
e2fsck（用于在非正常关机后修复文件系统的不统一之处）、
mke2fs（用于将分区初始化为包含空白ext2 文件系统）、
debugfs（用于检查文件系统的内部结构、手动修复被破坏的文件系统或为e2fsck
创建测试范例）、 tune2fs（用于修改文件系统参数）和其它大多数核心
ext2fs 文件系统实用程序。

%package libs
Summary:	ext2 filesystem-specific libraries
Summary(pl.UTF-8):	Biblioteki dla systemu plików ext2
Group:		Libraries
Conflicts:	e2fsprogs < 1.40.6-3
Conflicts:	fsck < 1.40.6-3

%description libs
ext2 filesystem-specific libraries.

%description libs -l pl.UTF-8
Biblioteki dla systemu plików ext2.

%package devel
Summary:	ext2 filesystem-specific libraries and headers
Summary(cs.UTF-8):	Knihovny a hlavičkové soubory pro systém souborů ext2
Summary(da.UTF-8):	ext2 filsystemsspecifikke biblioteker og headerfiler
Summary(de.UTF-8):	Bibliotheken und Header-Dateien für ext2-Dateisysteme
Summary(es.UTF-8):	Bibliotecas y archivos de inclusión para e2fs
Summary(fr.UTF-8):	Bibliothèques et en-têtes spécifiques au système de fichiers ext2
Summary(id.UTF-8):	Library dan file header untuk e2fsprogs
Summary(is.UTF-8):	Aðgerðasöfn og hausaskrár fyrir ext2 skráarkerfið
Summary(it.UTF-8):	Librerie e file header specifici per il filesystem ext2
Summary(ja.UTF-8):	ext2 ファイルシステムに固有の静的ライブラリとヘッダー
Summary(ko.UTF-8):	ext2 파일시스템-지정 정적 라이브러리와 헤더들
Summary(nb.UTF-8):	ext2 filsystemspesifikke bibliotek og headerfiler
Summary(pl.UTF-8):	Pliki nagłówkowe do bibliotek e2fs
Summary(pt.UTF-8):	Bibliotecas e ficheiros de inclusão específicos do sistema de ficheiros ext2
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para e2fs
Summary(ru.UTF-8):	Библиотеки и файлы заголовков для разработки программ, использующих ext2
Summary(sk.UTF-8):	Knižnice a hlavičkové súbory pre ext2-špecifické programy
Summary(sl.UTF-8):	Knjižnice in glave, specifične datotečnemu sistemu ext2
Summary(sv.UTF-8):	ext2 filsystemspecifika bibliotek och huvuden
Summary(uk.UTF-8):	Бібліотки програміста та хедери для роботи з ext2fs
Summary(zh_CN.UTF-8):	ext2 文件系统特有的静态库和头文件。
Summary(zh_TW.UTF-8):	ext2 檔案系統特定的靜態函式庫與表頭。
Group:		Development/Libraries
%if %{without allstatic}
Requires:	%{name}-libs = %{version}-%{release}
%endif
Requires:	libcom_err-devel = %{version}-%{release}
Requires:	libuuid-devel
Obsoletes:	libext2fs2-devel

%description devel
e2fsprogs-devel contains the libraries and header files needed to
develop second extended (ext2) filesystem-specific programs.

%description devel -l cs.UTF-8
Balíček e2fsprogs-devel obsahuje knihovny a hlavičkové soubory
potřebné pro vývoj programů pracujících se systémem souborů ext2
(second extended fs).

%description devel -l da.UTF-8
e2fsprogs-devel indeholder de headerfiler og biblioteker man behøver
for at udvikle programmer specielt rettet mod ext2-filsystemer.

%description devel -l de.UTF-8
Das Paket e2fsprogs-devel enthält die Bibliotheken und Header-Dateien,
die für die Entwicklung von Programmen für das Second
Extended-Dateisystem (ext2) erforderlich sind.

%description devel -l es.UTF-8
e2fsprogs-devel contiene las bibliotecas y los ficheros de cabecera
necesarios para desarrollar programas específicos para el sistema de
ficheros ext2.

%description devel -l fr.UTF-8
e2fsprogs-devel contient les bibliothèques et fichiers d'en-tête
nécessaires au développement de programmes spécifiques au système de
fichiers ext2.

%description devel -l id.UTF-8
e2fsprogs-devel berisi library dan file header yang dibutuhkan untuk
develop program yang berkaitan dengan filesystem ext2.

%description devel -l is.UTF-8
e2fsprogs-devel inniheldur library og header skrár sem þarf til að búa
til (ext2) skráarsafns forrit

%description devel -l it.UTF-8
e2fsprogs-devel contiene le librerie e i file header necessari per
sviluppare programmi specifici per il filesystem ext2.

%description devel -l ja.UTF-8
e2fspgrogs-devel には、Second Extended (ext2) ファイルシステムに固有
のプログラムを開発するために必要なライブラリとヘッダーファイルが含まれ
ています。

%description devel -l nb.UTF-8
e2fsprogs-devel inneholder de headerfiler og bibliotek man trenger for
å utvikle programmer spesielt rettet mot ext2-filsystemer.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja niezbędne do tworzenia programów
obsługujących e2fs.

%description devel -l pt.UTF-8
O pacote e2fsprogs-devel contém as bibliotecas e ficheiros de inclusão
necessários para desenvolver programas específicos do sistema de
ficheiros ext2.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento de programas
específicos para sistema de arquivo ext2.

%description devel -l ru.UTF-8
e2fsprogs-devel содержит статические библиотеки и файлы заголовков,
необходимые при разработке программ, использующих файловую систему
ext2.

%description devel -l sk.UTF-8
e2fsprogs-devel obsahuje knižnice a hlavičkové súbory potrebné pre
vývoj programov pre ext2 súborový systém.

%description devel -l sv.UTF-8
e2fsprogs-devel innehåller bibliotek och huvudfiler som behövs för att
utveckla filsystemsspecifika program för det andra utökade (ext2)
filsystemet.

%description devel -l uk.UTF-8
e2fsprogs-devel містить бібліотеки та хедери, необхідні для написання
програм, які працюють з файловою системою ext2.

%description devel -l zh_CN.UTF-8
e2fsprogs-devel 包含开发辅助扩展 (ext2)
文件系统专用程序所需的程序库和头文件。

%package static
Summary:	ext2 filesystem-specific static libraries
Summary(cs.UTF-8):	Statické knihovny pro systém souborů ext2
Summary(da.UTF-8):	ext2 filsystemsspecifikke statiske biblioteker
Summary(de.UTF-8):	Statische Bibliotheken für ext2-Dateisysteme
Summary(es.UTF-8):	Bibliotecas estaticas para e2fs
Summary(fr.UTF-8):	Bibliothèques statiques spécifiques au système de fichiers ext2
Summary(it.UTF-8):	Librerie statiche specifici per il filesystem ext2
Summary(nb.UTF-8):	ext2 filsystemspesifikke statiske bibliotek
Summary(pl.UTF-8):	Biblioteki statyczne do obsługi systemu plików ext2
Summary(pt.UTF-8):	Bibliotecas estaticas específicos do sistema de ficheiros ext2
Summary(pt_BR.UTF-8):	Bibliotecas estaticas para e2fs
Summary(ru.UTF-8):	Статические библиотеки для разработки программ, использующих ext2
Summary(sk.UTF-8):	Statické knižnice a hlavičkové súbory pre ext2-špecifické programy
Summary(sv.UTF-8):	ext2 filsystemspecifika statiska bibliotek
Summary(uk.UTF-8):	Статичні бібліотки програміста для роботи з ext2fs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries needed to develop ext2 filesystem-specific programs
statically linked with e2progs libs.

%description static -l de.UTF-8
Libraries zur Entwicklung von ext2-Dateisystemspezifischen Programmen
erforderlich sind.

%description static -l es.UTF-8
Bibliotecas estaticas para desarrollo de programas específicos para
sistema de archivo ext2.

%description static -l pl.UTF-8
Biblioteki statyczne do obsługi e2fs niezbędne do kompilacji programów
statycznie skonsolidowanych (linkowanych) z bibliotekami do e2fs.

%description static -l pt_BR.UTF-8
Bibliotecas estaticas para desenvolvimento de programas específicos
para sistema de arquivo ext2.

%description static -l ru.UTF-8
e2fsprogs-devel-static содержит статические библиотеки, необходимые
для написания программ, работающих с файловой системой ext2.

%description static -l uk.UTF-8
e2fsprogs-devel-static містить статичні бібліотеки, необхідні для
написання програм, які працюють з файловою системою ext2.

%package -n libcom_err
Summary:	A Common Error Description Library for unices
Summary(pl.UTF-8):	Biblioteka opisu popularnych błędów dla uniksów
Group:		Libraries
Conflicts:	e2fsprogs < 1.34-3

%description -n libcom_err
A Common Error Description Library for unices.

%description -n libcom_err -l pl.UTF-8
Biblioteka opisu popularnych błędów dla uniksów.

%package -n libcom_err-devel
Summary:	Development files for Common Error Description Library for unices
Summary(pl.UTF-8):	Pliki dla programistów do biblioteki opisu popularnych błędów dla uniksów
Group:		Development/Libraries
Requires:	libcom_err = %{version}-%{release}
Conflicts:	e2fsprogs-devel < 1.34-3

%description -n libcom_err-devel
A Common Error Description Library for unices - development files.

%description -n libcom_err-devel -l pl.UTF-8
Biblioteka opisu popularnych błędów dla uniksów - pliki dla
programistów.

%package -n libcom_err-static
Summary:	Static version of Common Error Description Library for unices
Summary(pl.UTF-8):	Statyczna biblioteka opisu popularnych błędów dla uniksów
Group:		Development/Libraries
Requires:	libcom_err-devel = %{version}-%{release}
Conflicts:	e2fsprogs-static < 1.34-3

%description -n libcom_err-static
A Common Error Description Library for unices - static version.

%description -n libcom_err-static -l pl.UTF-8
Biblioteka opisu popularnych błędów dla uniksów - wersja statyczna.

%package initrd
Summary:	e2fsck and mke2fs - initrd version
Summary(pl.UTF-8):	e2fsck i mke2fs - wersja dla initrd
Group:		Base
Conflicts:	geninitrd < 10000.10

%description initrd
This package includes a e2fsck and mke2fs utilities staticaly
linked for initrd.

%description initrd -l pl.UTF-8
Pakiet ten zawiera narzędziae2fsck i mke2fs statycznie skonsolidowane
na potrzeby initrd.

%prep
%setup -q
%patch0 -p1
%{__gzip} -dc < %{SOURCE1} > doc/e2compr.texinfo
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

sed -i -e '/AC_SUBST(DO_TEST_SUITE/a\MKINSTALLDIRS="install -d"\nAC_SUBST(MKINSTALLDIRS)\n' configure.in

# AX_TLS
tail -n +2604 aclocal.m4 > acinclude.m4

%build
cp -f /usr/share/automake/config.sub .
%{__gettextize}
%{__aclocal}
%{__autoconf}

%if %{with initrd}
%if %{with dietlibc}
# needed for syscall()
cp -a MCONFIG.in MCONFIG.in.org
sed -i -e 's|\(^LIBUUID = .*\)|\1 -lcompat|g' \
	-e 's|\(^STATIC_LIBUUID = .*\)|\1 -lcompat|g' MCONFIG.in
%endif
%configure \
	ac_cv_lib_dl_dlopen=no \
	%{?with_uClibc:CC="%{_target_cpu}-uclibc-gcc"} \
	%{?with_dietlibc:--with-cc="diet %{__cc}"} \
	--with-ccopts="%{rpmcflags} -Os" \
	--with-ldopts="%{rpmldflags} -static" \
	--disable-elf-shlibs \
	--disable-fsck \
	--disable-libblkid \
	--disable-libuuid \
	--disable-nls \
	--disable-testio-debug \
	--disable-e2initrd-helper \
	--disable-uuidd \
	--disable-tls \
	--disable-nls \
	--disable-threads

%{__make} -j1 libs
%{__make} progs
mv -f misc/mke2fs initrd-mke2fs
%{__make} clean
%{?with_dietlibc:mv MCONFIG.in.org MCONFIG.in}
%endif

%configure \
	--with-root-prefix="" \
	%{!?with_nls:--disable-nls} \
	%{!?with_allstatic:--enable-elf-shlibs} \
	--disable-fsck \
	--disable-libblkid \
	--disable-libuuid \
	--disable-uuidd \
	--enable-compression \
	--enable-htree \
	--disable-rpath

%{__make} -j1 libs \
	LDFLAGS="%{rpmldflags}"
%{__make} progs docs \
	LDFLAGS="%{rpmldflags}"

cd doc
makeinfo --no-split e2compr.texinfo

%install
rm -rf $RPM_BUILD_ROOT
%{?with_dietlibc:install -d $RPM_BUILD_ROOT%{dietlibdir}}
export PATH=/sbin:$PATH

echo "install-shlibs:" >> intl/Makefile

%{__make} install install-libs \
	root_libdir=/%{_lib} \
	mkinstalldirs='install -d' \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf e2fsck $RPM_BUILD_ROOT/sbin/fsck.ext2
ln -sf e2fsck $RPM_BUILD_ROOT/sbin/fsck.ext3
ln -sf mke2fs $RPM_BUILD_ROOT/sbin/mkfs.ext2

install doc/e2compr.info $RPM_BUILD_ROOT%{_infodir}

touch $RPM_BUILD_ROOT%{_sysconfdir}/e2fsck.conf

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/{mkfs,fsck}.ext[234]*.8*
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.ext2.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.ext3.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.ext4.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.ext4dev.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.ext2.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.ext3.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.ext4.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.ext4dev.8
# missing in non-english-man-pages tarball
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/hu/man8/fsck.ext3.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/hu/man8/fsck.ext4.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/hu/man8/fsck.ext4dev.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/it/man8/fsck.ext3.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/it/man8/fsck.ext4.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/it/man8/fsck.ext4dev.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/it/man8/mkfs.ext3.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/it/man8/mkfs.ext4.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/it/man8/mkfs.ext4dev.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/ja/man8/fsck.ext4.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/ja/man8/fsck.ext4dev.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/ja/man8/mkfs.ext4.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/ja/man8/mkfs.ext4dev.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/ko/man8/fsck.ext3.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/ko/man8/fsck.ext4.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/ko/man8/fsck.ext4dev.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/ko/man8/mkfs.ext3.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/ko/man8/mkfs.ext4.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/ko/man8/mkfs.ext4dev.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/pl/man8/fsck.ext4.8
echo '.so e2fsck.8' > $RPM_BUILD_ROOT%{_mandir}/pl/man8/fsck.ext4dev.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/pl/man8/mkfs.ext3.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/pl/man8/mkfs.ext4.8
echo '.so mke2fs.8' > $RPM_BUILD_ROOT%{_mandir}/pl/man8/mkfs.ext4dev.8

%if %{with nls}
[ "`file $RPM_BUILD_ROOT%{_datadir}/locale/it/LC_MESSAGES/e2fsprogs.mo |\
	sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
%find_lang %{name}
%endif

rm -f $RPM_BUILD_ROOT%{_mandir}/README.e2fsprogs-non-english-man-pages

%if %{with initrd}
install -d $RPM_BUILD_ROOT%{_libdir}/initrd
install initrd-mke2fs $RPM_BUILD_ROOT%{_libdir}/initrd/mke2fs
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n libcom_err -p /sbin/ldconfig
%postun	-n libcom_err -p /sbin/ldconfig

%files %{?with_nls:-f %{name}.lang}
%defattr(644,root,root,755)
# COPYING specifies license details for some parts of package
%doc COPYING README RELEASE-NOTES
%attr(755,root,root) /sbin/badblocks
%attr(755,root,root) /sbin/debugfs
%attr(755,root,root) /sbin/dumpe2fs
%attr(755,root,root) /sbin/e2fsck
%attr(755,root,root) /sbin/e2image
%attr(755,root,root) /sbin/e2label
%attr(755,root,root) /sbin/e2undo
%attr(755,root,root) /sbin/fsck.ext2
%attr(755,root,root) /sbin/fsck.ext3
%attr(755,root,root) /sbin/fsck.ext4
%attr(755,root,root) /sbin/fsck.ext4dev
%attr(755,root,root) /sbin/logsave
%attr(755,root,root) /sbin/mke2fs
%attr(755,root,root) /sbin/mkfs.ext2
%attr(755,root,root) /sbin/mkfs.ext3
%attr(755,root,root) /sbin/mkfs.ext4
%attr(755,root,root) /sbin/mkfs.ext4dev
%attr(755,root,root) /sbin/resize2fs
%attr(755,root,root) /sbin/tune2fs
%attr(755,root,root) %{_bindir}/chattr
%attr(755,root,root) %{_bindir}/lsattr
%attr(755,root,root) %{_bindir}/mk_cmds
%attr(755,root,root) %{_sbindir}/filefrag
%attr(755,root,root) %{_sbindir}/mklost+found
%attr(755,root,root) %{_libdir}/e2initrd_helper
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/e2fsck.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mke2fs.conf
%{_mandir}/man1/chattr.1*
%{_mandir}/man1/lsattr.1*
%{_mandir}/man1/mk_cmds.1*
%{_mandir}/man5/e2fsck.conf.5*
%{_mandir}/man5/mke2fs.conf.5*
%{_mandir}/man8/badblocks.8*
%{_mandir}/man8/debugfs.8*
%{_mandir}/man8/dumpe2fs.8*
%{_mandir}/man8/e2fsck.8*
%{_mandir}/man8/e2image.8*
%{_mandir}/man8/e2label.8*
%{_mandir}/man8/e2undo.8*
%{_mandir}/man8/filefrag.8*
%{_mandir}/man8/fsck.ext2.8*
%{_mandir}/man8/fsck.ext3.8*
%{_mandir}/man8/fsck.ext4.8*
%{_mandir}/man8/fsck.ext4dev.8*
%{_mandir}/man8/logsave.8*
%{_mandir}/man8/mke2fs.8*
%{_mandir}/man8/mkfs.ext2.8*
%{_mandir}/man8/mkfs.ext3.8*
%{_mandir}/man8/mkfs.ext4.8*
%{_mandir}/man8/mkfs.ext4dev.8*
%{_mandir}/man8/mklost+found.8*
%{_mandir}/man8/resize2fs.8*
%{_mandir}/man8/tune2fs.8*
%lang(fi) %{_mandir}/fi/man1/chattr.1*
%lang(fi) %{_mandir}/fi/man1/lsattr.1*
%lang(fr) %{_mandir}/fr/man1/lsattr.1*
%lang(fr) %{_mandir}/fr/man8/badblocks.8*
%lang(fr) %{_mandir}/fr/man8/dumpe2fs.8*
%lang(fr) %{_mandir}/fr/man8/e2label.8*
%lang(fr) %{_mandir}/fr/man8/mklost+found.8*
%lang(hu) %{_mandir}/hu/man1/chattr.1*
%lang(hu) %{_mandir}/hu/man1/lsattr.1*
%lang(hu) %{_mandir}/hu/man8/dumpe2fs.8*
%lang(hu) %{_mandir}/hu/man8/e2fsck.8*
%lang(hu) %{_mandir}/hu/man8/fsck.ext2.8*
%lang(hu) %{_mandir}/hu/man8/fsck.ext3.8*
%lang(hu) %{_mandir}/hu/man8/fsck.ext4.8*
%lang(hu) %{_mandir}/hu/man8/fsck.ext4dev.8*
%lang(hu) %{_mandir}/hu/man8/tune2fs.8*
%lang(it) %{_mandir}/it/man1/chattr.1*
%lang(it) %{_mandir}/it/man1/lsattr.1*
%lang(it) %{_mandir}/it/man8/badblocks.8*
%lang(it) %{_mandir}/it/man8/debugfs.8*
%lang(it) %{_mandir}/it/man8/dumpe2fs.8*
%lang(it) %{_mandir}/it/man8/e2fsck.8*
%lang(it) %{_mandir}/it/man8/fsck.ext2.8*
%lang(it) %{_mandir}/it/man8/fsck.ext3.8*
%lang(it) %{_mandir}/it/man8/fsck.ext4.8*
%lang(it) %{_mandir}/it/man8/fsck.ext4dev.8*
%lang(it) %{_mandir}/it/man8/mke2fs.8*
%lang(it) %{_mandir}/it/man8/mkfs.ext2.8*
%lang(it) %{_mandir}/it/man8/mkfs.ext3.8*
%lang(it) %{_mandir}/it/man8/mkfs.ext4.8*
%lang(it) %{_mandir}/it/man8/mkfs.ext4dev.8*
%lang(it) %{_mandir}/it/man8/mklost+found.8*
%lang(it) %{_mandir}/it/man8/tune2fs.8*
%lang(ja) %{_mandir}/ja/man1/chattr.1*
%lang(ja) %{_mandir}/ja/man1/lsattr.1*
%lang(ja) %{_mandir}/ja/man8/badblocks.8*
%lang(ja) %{_mandir}/ja/man8/debugfs.8*
%lang(ja) %{_mandir}/ja/man8/dumpe2fs.8*
%lang(ja) %{_mandir}/ja/man8/e2fsck.8*
%lang(ja) %{_mandir}/ja/man8/e2image.8*
%lang(ja) %{_mandir}/ja/man8/e2label.8*
%lang(ja) %{_mandir}/ja/man8/fsck.ext2.8*
%lang(ja) %{_mandir}/ja/man8/fsck.ext3.8*
%lang(ja) %{_mandir}/ja/man8/fsck.ext4.8*
%lang(ja) %{_mandir}/ja/man8/fsck.ext4dev.8*
%lang(ja) %{_mandir}/ja/man8/mke2fs.8*
%lang(ja) %{_mandir}/ja/man8/mkfs.ext2.8*
%lang(ja) %{_mandir}/ja/man8/mkfs.ext3.8*
%lang(ja) %{_mandir}/ja/man8/mkfs.ext4.8*
%lang(ja) %{_mandir}/ja/man8/mkfs.ext4dev.8*
%lang(ja) %{_mandir}/ja/man8/mklost+found.8*
%lang(ja) %{_mandir}/ja/man8/resize2fs.8*
%lang(ja) %{_mandir}/ja/man8/tune2fs.8*
%lang(ko) %{_mandir}/ko/man1/chattr.1*
%lang(ko) %{_mandir}/ko/man1/lsattr.1*
%lang(ko) %{_mandir}/ko/man8/badblocks.8*
%lang(ko) %{_mandir}/ko/man8/debugfs.8*
%lang(ko) %{_mandir}/ko/man8/dumpe2fs.8*
%lang(ko) %{_mandir}/ko/man8/e2fsck.8*
%lang(ko) %{_mandir}/ko/man8/fsck.ext2.8*
%lang(ko) %{_mandir}/ko/man8/fsck.ext3.8*
%lang(ko) %{_mandir}/ko/man8/fsck.ext4.8*
%lang(ko) %{_mandir}/ko/man8/fsck.ext4dev.8*
%lang(ko) %{_mandir}/ko/man8/mke2fs.8*
%lang(ko) %{_mandir}/ko/man8/mkfs.ext2.8*
%lang(ko) %{_mandir}/ko/man8/mkfs.ext3.8*
%lang(ko) %{_mandir}/ko/man8/mkfs.ext4.8*
%lang(ko) %{_mandir}/ko/man8/mkfs.ext4dev.8*
%lang(ko) %{_mandir}/ko/man8/mklost+found.8*
%lang(ko) %{_mandir}/ko/man8/tune2fs.8*
%lang(pl) %{_mandir}/pl/man1/chattr.1*
%lang(pl) %{_mandir}/pl/man1/lsattr.1*
%lang(pl) %{_mandir}/pl/man8/badblocks.8*
%lang(pl) %{_mandir}/pl/man8/debugfs.8*
%lang(pl) %{_mandir}/pl/man8/dumpe2fs.8*
%lang(pl) %{_mandir}/pl/man8/e2fsck.8*
%lang(pl) %{_mandir}/pl/man8/e2label.8*
%lang(pl) %{_mandir}/pl/man8/fsck.ext2.8*
%lang(pl) %{_mandir}/pl/man8/fsck.ext3.8*
%lang(pl) %{_mandir}/pl/man8/fsck.ext4.8*
%lang(pl) %{_mandir}/pl/man8/fsck.ext4dev.8*
%lang(pl) %{_mandir}/pl/man8/mke2fs.8*
%lang(pl) %{_mandir}/pl/man8/mkfs.ext2.8*
%lang(pl) %{_mandir}/pl/man8/mkfs.ext3.8*
%lang(pl) %{_mandir}/pl/man8/mkfs.ext4.8*
%lang(pl) %{_mandir}/pl/man8/mkfs.ext4dev.8*
%lang(pl) %{_mandir}/pl/man8/mklost+found.8*
%lang(pl) %{_mandir}/pl/man8/tune2fs.8*
%{_datadir}/ss
%{_infodir}/e2compr.info*

%if %{without allstatic}
%files libs
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libe2p.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libe2p.so.2
%attr(755,root,root) /%{_lib}/libext2fs.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libext2fs.so.2
%attr(755,root,root) /%{_lib}/libss.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libss.so.2
%endif

%files devel
%defattr(644,root,root,755)
%if %{without allstatic}
%attr(755,root,root) %{_libdir}/libe2p.so
%attr(755,root,root) %{_libdir}/libext2fs.so
%attr(755,root,root) %{_libdir}/libss.so
%endif
%{_includedir}/e2p
%{_includedir}/ext2fs
%{_includedir}/ss
%{_pkgconfigdir}/e2p.pc
%{_pkgconfigdir}/ext2fs.pc
%{_pkgconfigdir}/ss.pc
%{_infodir}/libext2fs.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libe2p.a
%{_libdir}/libext2fs.a
%{_libdir}/libss.a

%files -n libcom_err
%defattr(644,root,root,755)
%if %{without allstatic}
%attr(755,root,root) /%{_lib}/libcom_err.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libcom_err.so.2
%endif

%files -n libcom_err-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/compile_et
%{!?with_allstatic:%attr(755,root,root) %{_libdir}/libcom_err.so}
%{_includedir}/et
%{_datadir}/et
%{_pkgconfigdir}/com_err.pc
%{_mandir}/man1/compile_et.1*
%lang(ja) %{_mandir}/ja/man1/compile_et.1*
%{_mandir}/man3/com_err.3*
%lang(ja) %{_mandir}/ja/man3/com_err.3*

%files -n libcom_err-static
%defattr(644,root,root,755)
%{_libdir}/libcom_err.a

%if %{with initrd}
%files initrd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/initrd/mke2fs
%endif
