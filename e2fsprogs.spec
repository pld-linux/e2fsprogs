#
# Conditional build:
# _without_nls		- without NLS
# _with_allstatic	- link everything statically
#
Summary:	Utilities for managing the second extended (ext2) filesystem
Summary(cs):	Nástroje pro správu souborovıch systémù typu ext2
Summary(da):	Værktøjer til håndtering af ext2 filsystemer
Summary(de):	Dienstprogramme zum Verwalten des Second Extended-Dateisystems (ext2)
Summary(es):	Utilidades para la gestión de un sistema de ficheros ext2
Summary(fr):	Utilitaires pour la gestion du système de fichiers ext2
Summary(id):	Utility untuk management filesystem ext2
Summary(is):	Tól til ağ sısla meğ ext2 skráarkerfiğ
Summary(it):	Utility per la gestione del filesystem (ext2)
Summary(ja):	Second Extended (ext2) ¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤ò´ÉÍı¤¹¤ë¤¿¤á¤Î¥æ¡¼¥Æ¥£¥ê¥Æ¥£
Summary(ko):	ext2 ÆÄÀÏ ½Ã½ºÅÛÀ» °ü¸®ÇÏ´Â À¯Æ¿¸®Æ¼
Summary(no):	Verktøy for håndtering av ext2 filsystemet
Summary(pl):	Narzêdzia do systemu plikowego ext2
Summary(pt):	Utilitários para gerir o sistema de ficheiros ext2
Summary(pt_BR):	Ferramentas para o sistema de arquivos ext2
Summary(ru):	õÔÉÌÉÔÙ ÕĞÒÁ×ÌÅÎÉÑ ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÏÊ ext2
Summary(sk):	Pomocné programy pre správu ext2 súborového systému
Summary(sl):	Pripomoèki za upravljanje datoteènega sistema ext2
Summary(sv):	Verktyg för att hantera det andra utökade (ext2) filsystemet
Summary(tr):	ext2 dosya sistemi için araçlar
Summary(uk):	õÔÉÌ¦ÔÉ ÄÌÑ ÒÏÂÏÔÉ Ú ÆÁÊÌÏ×ÏÀ ÓÉÓÔÅÍÏÀ ext2
Summary(zh_CN):	¹ÜÀíµÚ¶şÀ©Õ¹£¨ext2£©ÎÄ¼şÏµÍ³µÄ¹¤¾ß¡£
Summary(zh_TW):	¥Î©óºŞ²z ext2 ÀÉ®×¨t²Îªº¤u¨ãµ{¦¡¡C
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
Balíèek e2fsprogs obsahuje nìkolik programù pro vytváøení, kontrolu
úpravy a opravy nekonzistencí v systémech souborù typu ext2 (second
extended filesystem). Balíèek obsahuje program e2fsck (na opravy
nekonzistencí systémù souborù, které nebyly odpojeny pøi vypnutí
systému), mke2fs (pro vytvoøení prázdného systému souborù typu ext2 v
diskovém oddílu), debugfs (pro kontrolu interní struktury systému
souborù, manuální opravu po¹kozeného systému souborù a pro vytváøení
testovacích pøípadù pro e2fsck), tune2fs (pro úpravu parametrù systému
souborù) a vìt¹inu dal¹ích programù pro práci se systémy souborù typu
ext2fs.

%description -l da
e2fsprogs-pakken indeholder diverse værktøjer for at lave,
kontrollere, modificere og reparere ext2-filsystemer. e2fsprogs
indeholder e2fsck (bruges for at reparere filsystemer efter uren
nedlukning af systemet), mke2fs (bruges for at initialisere en
partition med et tomt ext2-filsystem), debugfs (bruges for at
undersøge de interne strukturer i filsystemet, for manuelt at kunne
reparere et ødelagt filsystem eller lave testscenarier for e2fsck),
tune2fs (bruges for at modificere filsystem-parametre) og flere andre
værktøjer for at ændre og undersøge ext2-filsystemer.

%description -l de
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

%description -l es
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

%description -l fr
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
e2fsprogs pakkinn inniheldur nokkur forrit til ağ búa til, skoğa,
breyta og laga allar villur í Linux skráarkerfinu (ext2). e2fsprogs
inniheldur e2fsck (notağ til ağ laga villur í skráarkerfinu eftir
vonda enduruppkeyrslu), mke2fs (notağ til ağ undirbúa harğa disk töflu
til ağ innihalda tómt ext2 skráarkerfi), debugfs (notağ til ağ skoğa
innihald tóms ext2 skráarkerfis, til ağ handvirkt laga ónıtt
skráarkerfi eğa til ağ undirbúa tilraunir fyrir e2fsck)m tune2fs(notağ
til ağ breyta skráarkerfis möguleikum) og flest önnur ext2fs
skráarkerfis forritum

%description -l it
Il pacchetto e2fsprogs contiene varie utility per creare, controllare,
modificare e correggere le inconsistenze in un filesystem ext2.
e2fsprogs contiene e2fsck (risolve le inconsistenze di un filesystem
dopo un arresto non corretto del calcolatore), mke2fs (inizializza una
nuova partizione per un filesystem ext2 vuoto), debugfs (esamina la
struttura interna di un filesystem, è usato per riparare manualmente
gli errori presenti in un filesystem e per creare casi di test per
e2fsck), tune2fs (modifica i parametri del filesystem) e molte delle
utility principali per il filesystem ext2fs.

%description -l ja
e2fsprogs ¥Ñ¥Ã¥±¡¼¥¸¤Ë¤Ï Second Extended (ext2) ¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤Î
ºîÀ®¡¢¸¡ºº¡¢ÊÑ¹¹¤ò¹Ô¤Ã¤¿¤ê¡¢ÉÔÀ°¹ç¤ò½¤Éü¤¹¤ë¤¿¤á¤Î¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤¬
¿ôÂ¿¤¯´Ş¤Ş¤ì¤Æ¤¤¤Ş¤¹¡£e2fsprogs ¤Ë¤Ï e2fsck (°Û¾ï½ªÎ»¸å¤Ë¥Õ¥¡¥¤¥ë
¥·¥¹¥Æ¥à¤ÎÉÔÀ°¹ç¤ò½¤Éü¤¹¤ë)¡¢mke2fs (¥Ñ¡¼¥Æ¥£¥·¥ç¥ó¤ò½é´ü²½¤·¤Æ¶õ¤Î
ext2 ¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤òºîÀ®¤¹¤ë)¡¢debugfs (¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤ÎÆâÉô
¹½Â¤¤ò¸¡ºº¤·¡¢ÇËÂ»¤·¤¿¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤ò¼êÆ°¤Ç½¤Éü¤·¤¿¤ê¡¢e2fsck
ÍÑ¤Î¥Æ¥¹¥È¥±¡¼¥¹¤òºîÀ®¤¹¤ë)¡¢tune2fs (¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤Î¥Ñ¥é¥á¡¼¥¿
¤òÊÑ¹¹¤¹¤ë) ¤Î¤Û¤«¡¢¼ç¤Ê ext2fs ¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤Î
¤Û¤È¤ó¤É¤¬´Ş¤Ş¤ì¤Ş¤¹¡£

%description -l no
e2fsprogs-pakken inneholder diverse verktøy for å lage, kontrollere,
modifisere og reparere ext2-filsystemer. e2fsprogs inneholder e2fsck
(brukes for å reparere filsystemer etter uren nedkjøring av systemet),
mke2fs (brukes for å initialisere en partisjon med et tomt
ext2-filsystem), debugfs (brukes for å undersøke de interne
strukturene i filsystemet, for manuelt å kunne reparere et ødelagt
filsystem eller lage testscenarier for e2fsck), tune2fs (brukes for å
modifisere filsystem-parametre) og flere andre verktøy for å endre og
undersøke ext2-filsystemer.

%description -l pl
Pakiet ten zawiera narzêdzia do tworzenia, sprawdzania i naprawiania
wolumenów dyskowych z systemem plikowym ext2. e2fsprogs zawiera e2fsck
(u¿ywany do naprawiania niespójno¶ci w systemie plikowym po
niepoprawnym zamkniêciu systemu), mke2fs (u¿ywany do inicjacji
wolumenów ext2), debugfs (u¿ywany do sprawdzania wewnêtrznej struktury
wolumenów ext2, a tak¿e do rêcznego naprawiania b³êdów), tune2fs
(u¿ywany do modyfikacji parametrów wolumenów ext2) i kilka innych
narzêdzi do ext2.

%description -l pt
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

%description -l pt_BR
Este pacote inclui vários utilitários para criação, checagem e reparo
de sistema de arquivos ext2.

%description -l ru
ğÁËÅÔ e2fsprogs ÓÏÄÅÒÖÉÔ ÕÔÉÌÉÔÙ ÄÌÑ ÓÏÚÄÁÎÉÑ, ĞÒÏ×ÅÒËÉ, ÉÚÍÅÎÅÎÉÑ É
ËÏÒÒÅËÔÉÒÏ×ËÉ ×ÎÕÔÒÅÎÎÅÇÏ ÓÏÓÔÏÑÎÉÑ ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÙ ext2. e2fsprogs
ÓÏÄÅÒÖÉÔ e2fsck (ÄÌÑ ×ÏÓÓÔÁÎÏ×ÌÅÎÉÑ ÆÁÊÌÏ×ÏÊ ÓÔÒÕËÔÕÒÙ ĞÏÓÌÅ
ÎÅËÏÒÒÅËÔÎÏÇÏ ÚÁ×ÅÒÛÅÎÉÑ ÒÁÂÏÔÙ), mke2fs (ÄÌÑ ÉÎÉÃÉÁÌÉÚÁÃÉÉ ÒÁÚÄÅÌÁ
ĞÒÉ ÓÏÚÄÁÎÉÉ ĞÕÓÔÏÊ ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÙ ext2), debugfs (ĞÒÏÓÍÏÔÒ
×ÎÕÔÒÅÎÎÅÊ ÓÔÒÕËÔÕÒÙ ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÙ ÄÌÑ ÒÕŞÎÏÇÏ ×ÏÓÓÔÁÎÏ×ÌÅÎÉÑ
ĞÏ×ÒÅÖÄÅÎÎÏÊ ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÙ ÉÌÉ ÓÏÚÄÁÎÉÑ ÔÅÓÔÏ×ÙÈ ÓÉÔÕÁÃÉÊ ÄÌÑ
e2fsck), tune2fs (ÄÌÑ ÉÚÍÅÎÅÎÉÑ ĞÁÒÁÍÅÔÒÏ× ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÙ) É
ÍÎÏÖÅÓÔ×Ï ÄÒÕÇÉÈ ÕÔÉÌÉÔ ÄÌÑ ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÙ ext2.

%description -l sk
Balík e2fsprogs obsahuje niekoµko programov pre vytváranie, kontrolu,
zmenu a opravu nekonzistencií na ext2 súborovom systéme. e2fsprogs
obsahuje e2fsck (pre opravu nekonzistentnıch údajov na súborovom
systéme po neèistom ukonèení), mke2fs (pre vytvorenie prázdneho
súborového systému na diskovom oddieli), debugfs (pre skúmanie
vnútornıch ¹truktúr súborového systému, jeho ruènú opravu alebo pre
vytvorenie testovacích prípadov pre e2fsck), tune2fs (pre modifikáciu
parametrov súborového systému) a väè¹inu ïal¹ích základnıch pomôcok
pre prácu s ext2fs.

%description -l sv
Paketet e2fsprogs innehåller ett antal verktyg för att skapa,
kontrollera, modifiera och rätta felaktigheter i det andra utökade
(ext2) filsystemet. e2fsprogs innehåller e2fsck (används för att
reparera felaktigheter efter en oren avstängning), mke2fs (används för
att initiera en partition att innehålla ett tomt ext2-filsystem),
debugfs (används för att undersöka den interna strukturen i ett
filsystem, manuellt reparera trasiga filsystem eller skapa testfall
för e2fsck), tune2fs (används för att modifiera filsystemparametrar)
och de flesta andra basverktygen för filsystemet ext2fs.

%description -l tr
Bu paket, ext2 dosya sistemlerini yaratmak, onarmak, kontrol etmek ve
bazı parametrelerini değiştirmek için gerekli yazılımları içerir.

%description -l uk
ğÁËÅÔ e2fsprogs Í¦ÓÔÉÔØ ÎÁÂ¦Ò ÕÔÉÌ¦Ô ÄÌÑ ÓÔ×ÏÒÅÎÎÑ, ĞÅÒÅ×¦ÒËÉ,
ÍÏÄÉÆ¦ËÁÃ¦§ ÔÁ ×ÉĞÒÁ×ÌÅÎÎÑ ÂÕÄØ-ÑËÉÈ ĞÏÍÉÌÏË Õ ÆÁÊÌÏ×¦Ê ÓÉÓÔÅÍ¦ ext2.
e2fsprogs Í¦ÓÔÉÔØ e2fsck (×ÉËÏÒÉÓÔÏ×Õ¤ÔØÓÑ ÄÌÑ ×ÉĞÒÁ×ÌÅÎÎÑ ĞÏÍÉÌÏË
Ğ¦ÓÌÑ "ÂÒÕÄÎÏ§" ÚÕĞÉÎËÉ ÍÁÛÉÎÉ), mke2fs (ÄÌÑ ¦Î¦ÃÉÁÌ¦ÚÁÃ¦§ ÒÏÚÄ¦ÌÕ ÔÁ
ÓÔ×ÏÒÅÎÎÑ ĞÏÒÏÖÎØÏ§ ÆÁÊÌÏ×Ï§ ÓÉÓÔÅÍÉ ext2), debugfs (ÄÌÑ ×É×ŞÅÎÎÑ
×ÎÕÔÒ¦ÛÎØÏ§ ÓÔÒÕËÔÕÒÉ ÆÁÊÌÏ×Ï§ ÓÉÓÔÅÍÉ, ÒÕŞÎÏÇÏ ÒÅÍÏÎÔÕ ĞÏÛËÏÄÖÅÎÏ§
ÆÁÊÌÏ×Ï§ ÓÉÓÔÅÍÉ ÁÂÏ ÄÌÑ ÓÔ×ÏÒÅÎÎÑ ÔÅÓÔ¦× ÄÌÑ e2fsck), tune2fs (ÄÌÑ
ÍÏÄÉÆ¦ËÁÃ¦§ ĞÁÒÁÍÅÔÒ¦× ÆÁÊÌÏ×Ï§ ÓÉÓÔÅÍÉ) ÔÁ Â¦ÌØÛ¦ÓÔØ ¦ÎÛÉÈ ÂÁÚÏ×ÉÈ
ÕÔÉÌ¦Ô ÄÌÑ ext2fs.

%description -l zh_CN
e2fsprogs Èí¼ş°ü°üº¬Ò»Ğ©ÊµÓÃ³ÌĞò£¬ÓÃÓÚ´´½¨¡¢¼ì²é¡¢ ĞŞ¸ÄºÍ¾ÀÕı¸¨ÖúÀ©Õ¹
(ext2) ÎÄ¼şÏµÍ³ÖĞµÄÈÎºÎ²»Í³Ò»Ö®´¦¡£ e2fsprogs °üº¬
e2fsck£¨ÓÃÓÚÔÚ·ÇÕı³£¹Ø»úºóĞŞ¸´ÎÄ¼şÏµÍ³µÄ²»Í³Ò»Ö®´¦£©¡¢
mke2fs£¨ÓÃÓÚ½«·ÖÇø³õÊ¼»¯Îª°üº¬¿Õ°×ext2 ÎÄ¼şÏµÍ³£©¡¢
debugfs£¨ÓÃÓÚ¼ì²éÎÄ¼şÏµÍ³µÄÄÚ²¿½á¹¹¡¢ÊÖ¶¯ĞŞ¸´±»ÆÆ»µµÄÎÄ¼şÏµÍ³»òÎªe2fsck
´´½¨²âÊÔ·¶Àı£©¡¢ tune2fs£¨ÓÃÓÚĞŞ¸ÄÎÄ¼şÏµÍ³²ÎÊı£©ºÍÆäËü´ó¶àÊıºËĞÄ
ext2fs ÎÄ¼şÏµÍ³ÊµÓÃ³ÌĞò¡£

%package devel
Summary:	ext2 filesystem-specific libraries and headers
Summary(cs):	Knihovny a hlavièkové soubory pro systém souborù ext2
Summary(da):	ext2 filsystemsspecifikke biblioteker og headerfiler
Summary(de):	Bibliotheken und Header-Dateien für ext2-Dateisysteme
Summary(es):	Bibliotecas y archivos de inclusión para e2fs
Summary(fr):	Bibliothèques et en-têtes spécifiques au système de fichiers ext2
Summary(id):	Library dan file header untuk e2fsprogs
Summary(is):	Ağgerğasöfn og hausaskrár fyrir ext2 skráarkerfiğ
Summary(it):	Librerie e file header specifici per il filesystem ext2
Summary(ja):	ext2 ¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤Ë¸ÇÍ­¤ÎÀÅÅª¥é¥¤¥Ö¥é¥ê¤È¥Ø¥Ã¥À¡¼
Summary(ko):	ext2 ÆÄÀÏ½Ã½ºÅÛ-ÁöÁ¤ Á¤Àû ¶óÀÌºê·¯¸®¿Í Çì´õµé
Summary(no):	ext2 filsystemspesifikke bibliotek og headerfiler
Summary(pl):	Pliki nag³ówkowe do bibliotek e2fs
Summary(pt):	Bibliotecas e ficheiros de inclusão específicos do sistema de ficheiros ext2
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para e2fs
Summary(ru):	âÉÂÌÉÏÔÅËÉ É ÆÁÊÌÙ ÚÁÇÏÌÏ×ËÏ× ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ĞÒÏÇÒÁÍÍ, ÉÓĞÏÌØÚÕÀİÉÈ ext2
Summary(sk):	Kni¾nice a hlavièkové súbory pre ext2-¹pecifické programy
Summary(sl):	Knji¾nice in glave, specifiène datoteènemu sistemu ext2
Summary(sv):	ext2 filsystemspecifika bibliotek och huvuden
Summary(uk):	â¦ÂÌ¦ÏÔËÉ ĞÒÏÇÒÁÍ¦ÓÔÁ ÔÁ ÈÅÄÅÒÉ ÄÌÑ ÒÏÂÏÔÉ Ú ext2fs
Summary(zh_CN):	ext2 ÎÄ¼şÏµÍ³ÌØÓĞµÄ¾²Ì¬¿âºÍÍ·ÎÄ¼ş¡£
Summary(zh_TW):	ext2 ÀÉ®×¨t²Î¯S©wªºÀRºA¨ç¦¡®w»PªíÀY¡C
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libext2fs2-devel

%description devel
e2fsprogs-devel contains the libraries and header files needed to
develop second extended (ext2) filesystem-specific programs.

%description devel -l cs
Balíèek e2fsprogs-devel obsahuje knihovny a hlavièkové soubory
potøebné pro vıvoj programù pracujících se systémem souborù ext2
(second extended fs).

%description devel -l da
e2fsprogs-devel indeholder de headerfiler og biblioteker man behøver
for at udvikle programmer specielt rettet mod ext2-filsystemer.

%description devel -l de
Das Paket e2fsprogs-devel enthält die Bibliotheken und Header-Dateien,
die für die Entwicklung von Programmen für das Second
Extended-Dateisystem (ext2) erforderlich sind.

%description devel -l es
e2fsprogs-devel contiene las bibliotecas y los ficheros de cabecera
necesarios para desarrollar programas específicos para el sistema de
ficheros ext2.

%description devel -l fr
e2fsprogs-devel contient les bibliothèques et fichiers d'en-tête
nécessaires au développement de programmes spécifiques au système de
fichiers ext2.

%description devel -l id
e2fsprogs-devel berisi library dan file header yang dibutuhkan untuk
develop program yang berkaitan dengan filesystem ext2.

%description devel -l is
e2fsprogs-devel inniheldur library og header skrár sem şarf til ağ búa
til (ext2) skráarsafns forrit

%description devel -l it
e2fsprogs-devel contiene le librerie e i file header necessari per
sviluppare programmi specifici per il filesystem ext2.

%description devel -l ja
e2fspgrogs-devel ¤Ë¤Ï¡¢Second Extended (ext2) ¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤Ë¸ÇÍ­
¤Î¥×¥í¥°¥é¥à¤ò³«È¯¤¹¤ë¤¿¤á¤ËÉ¬Í×¤Ê¥é¥¤¥Ö¥é¥ê¤È¥Ø¥Ã¥À¡¼¥Õ¥¡¥¤¥ë¤¬´Ş¤Ş¤ì
¤Æ¤¤¤Ş¤¹¡£

%description devel -l no
e2fsprogs-devel inneholder de headerfiler og bibliotek man trenger for
å utvikle programmer spesielt rettet mot ext2-filsystemer.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja niezbêdne do tworzenia programów
obs³uguj±cych e2fs.

%description devel -l pt
O pacote e2fsprogs-devel contém as bibliotecas e ficheiros de inclusão
necessários para desenvolver programas específicos do sistema de
ficheiros ext2.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para desenvolvimento de programas
específicos para sistema de arquivo ext2.

%description devel -l ru
e2fsprogs-devel ÓÏÄÅÒÖÉÔ ÓÔÁÔÉŞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ É ÆÁÊÌÙ ÚÁÇÏÌÏ×ËÏ×,
ÎÅÏÂÈÏÄÉÍÙÅ ĞÒÉ ÒÁÚÒÁÂÏÔËÅ ĞÒÏÇÒÁÍÍ, ÉÓĞÏÌØÚÕÀİÉÈ ÆÁÊÌÏ×ÕÀ ÓÉÓÔÅÍÕ
ext2.

%description devel -l sk
e2fsprogs-devel obsahuje kni¾nice a hlavièkové súbory potrebné pre
vıvoj programov pre ext2 súborovı systém.

%description devel -l sv
e2fsprogs-devel innehåller bibliotek och huvudfiler som behövs för att
utveckla filsystemsspecifika program för det andra utökade (ext2)
filsystemet.

%description devel -l uk
e2fsprogs-devel Í¦ÓÔÉÔØ Â¦ÂÌ¦ÏÔÅËÉ ÔÁ ÈÅÄÅÒÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÎÁĞÉÓÁÎÎÑ
ĞÒÏÇÒÁÍ, ÑË¦ ĞÒÁÃÀÀÔØ Ú ÆÁÊÌÏ×ÏÀ ÓÉÓÔÅÍÏÀ ext2.

%description devel -l zh_CN
e2fsprogs-devel °üº¬¿ª·¢¸¨ÖúÀ©Õ¹ (ext2)
ÎÄ¼şÏµÍ³×¨ÓÃ³ÌĞòËùĞèµÄ³ÌĞò¿âºÍÍ·ÎÄ¼ş¡£

%package static
Summary:	ext2 filesystem-specific static libraries
Summary(cs):	Statické knihovny pro systém souborù ext2
Summary(da):	ext2 filsystemsspecifikke statiske biblioteker
Summary(de):	Statische Bibliotheken für ext2-Dateisysteme
Summary(es):	Bibliotecas estaticas para e2fs
Summary(fr):	Bibliothèques statiques spécifiques au système de fichiers ext2
Summary(it):	Librerie statiche specifici per il filesystem ext2
Summary(no):	ext2 filsystemspesifikke statiske bibliotek
Summary(pl):	Biblioteki statyczne do obs³ugi systemu plików ext2
Summary(pt):	Bibliotecas estaticas específicos do sistema de ficheiros ext2
Summary(pt_BR):	Bibliotecas estaticas para e2fs
Summary(ru):	óÔÁÔÉŞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ĞÒÏÇÒÁÍÍ, ÉÓĞÏÌØÚÕÀİÉÈ ext2
Summary(sk):	Statické kni¾nice a hlavièkové súbory pre ext2-¹pecifické programy
Summary(sv):	ext2 filsystemspecifika statiska bibliotek
Summary(uk):	óÔÁÔÉŞÎ¦ Â¦ÂÌ¦ÏÔËÉ ĞÒÏÇÒÁÍ¦ÓÔÁ ÄÌÑ ÒÏÂÏÔÉ Ú ext2fs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries needed to develop ext2 filesystem-specific programs
statically linked with e2progs libs.

%description static -l de
Libraries zur Entwicklung von ext2-Dateisystemspezifischen Programmen
erforderlich sind.

%description static -l es
Bibliotecas estaticas para desarrollo de programas específicos para
sistema de archivo ext2.

%description static -l pl
Biblioteki statyczne do obs³ugi e2fs niezbêdne do kompilacji programów
statycznie skonsolidowanych (linkowanych) z bibliotekami do e2fs.

%description static -l pt_BR
Bibliotecas estaticas para desenvolvimento de programas específicos
para sistema de arquivo ext2.

%description static -l ru
e2fsprogs-devel-static ÓÏÄÅÒÖÉÔ ÓÔÁÔÉŞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ
ÄÌÑ ÎÁĞÉÓÁÎÉÑ ĞÒÏÇÒÁÍÍ, ÒÁÂÏÔÁÀİÉÈ Ó ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÏÊ ext2.

%description static -l uk
e2fsprogs-devel-static Í¦ÓÔÉÔØ ÓÔÁÔÉŞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ
ÎÁĞÉÓÁÎÎÑ ĞÒÏÇÒÁÍ, ÑË¦ ĞÒÁÃÀÀÔØ Ú ÆÁÊÌÏ×ÏÀ ÓÉÓÔÅÍÏÀ ext2.

%package evms
Summary:	e2fs EVMS module
Summary(pl):	Modu³ e2fs dla EVMS
Group:		Libraries
Requires:	%{name} = %{version}
Requires:	evms

%description evms
e2fs EVMS module.

%description evms -l pl
Modu³ e2fs dla EVMS.

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
