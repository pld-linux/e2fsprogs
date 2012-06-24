# conditional build
# --without nls
# --with allstatic

Summary:	Tools for the second extended (ext2) filesystem
Summary(de):	Tools f�r das zweite erweiterte (ext2) Dateisystem
Summary(es):	Herramientas para el sistema de archivos ext2
Summary(fr):	Outils pour le syst�me de fichiers ext2
Summary(pl):	Narz�dzia do systemu plikowego ext2
Summary(pt_BR):	Ferramentas para o sistema de arquivos ext2
Summary(ru):	������� ��� ������ � �������� �������� ext2
Summary(tr):	ext2 dosya sistemi i�in ara�lar
Summary(uk):	���̦�� ��� ������ � �������� �������� ext2
Name:		e2fsprogs
Version:	1.27
Release:	5
License:	GPL
Group:		Applications/System
Source0:	ftp://download.sourceforge.net/pub/sourceforge/e2fsprogs/%{name}-%{version}.tar.gz
Source1:	http://opensource.captech.com/e2compr/ftp/e2compr-0.4.texinfo.gz
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		e2compr-info.patch
Patch2:		%{name}-mountlabel3.patch
Patch3:		%{name}-rlimit-workaround.patch
URL:		http://e2fsprogs.sourceforge.net/
PreReq:		/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	texinfo
Obsoletes:	libext2fs2

%description
The e2fsprogs package contains a number of utilities for creating,
checking, modifying and correcting any inconsistencies in second
extended (ext2) filesystems. E2fsprogs contains e2fsck (used to repair
filesystem inconsistencies after an unclean shutdown), mke2fs (used to
initialize a partition to contain an empty ext2 filesystem), debugfs
(used to examine the internal structure of a filesystem, to manually
repair a corrupted filesystem or to create test cases for e2fsck),
tune2fs (used to modify filesystem parameters) and most of the other
core ext2fs filesystem utilities.

%description -l de
Dieses Paket enth�lt eine Auswahl an Utilities zum Erstellen, Pr�fen
und zur Instandsetzung von ext2-Dateisystemen.

%description -l es
Este paquete incluye varios utilitarios para creaci�n, chequeo y
arreglo de sistema de archivos ext2.

%description -l fr
Ce package contient de nombreux utilitaires pour cr�er, v�rifier, et
r�parer les syst�mes de fichiers ext2.

%description -l pl
Pakiet ten zawiera narz�dzia do tworzenia, sprawdzania i naprawiania
wolumen�w dyskowych z systemem plikowym ext2. E2fsprogs zawiera e2fsck
(u�ywany do naprawiania niesp�jno�ci w systemie plikowym po
niepoprawnym zamkni�ciu systemu), mke2fs (u�ywany do inicjacji
wolumen�w ext2), debugfs (�ywany do sprawdzania wewn�trznej struktury
wolumen�w ext2, a tak�e do r�cznego naprawiania b��d�w), tune2fs
(u�ywany do modyfikacji parametr�w wolumen�w ext2) i kilka innych
narz�dzi do ext2.

%description -l pt_BR
Este pacote inclui v�rios utilit�rios para cria��o, checagem e reparo
de sistema de arquivos ext2.

%description -l ru
����� e2fsprogs �������� ����� ������ ��� ��������, ��������,
����������� � ���������� ����� ������ � �������� ������� ext2.
E2fsprogs �������� e2fsck (������������ ��� ����������� ������ �����
"��������" �������� ������), mke2fs (��� ������������� ������� �
�������� ������ �������� ������� ext2), debugfs (��� ��������
���������� ��������� �������� �������, ������� ������� ������������
�������� ������� ��� ��� �������� ������ ��� e2fsck), tune2fs (���
����������� ���������� �������� �������) � ����������� ���������
�������� ������ ��� ext2fs.

%description -l tr
Bu paket, ext2 dosya sistemlerini yaratmak, onarmak, kontrol etmek ve
baz� parametrelerini de�i�tirmek i�in gerekli yaz�l�mlar� i�erir.

%description -l uk
����� e2fsprogs ͦ����� ��¦� ���̦� ��� ���������, ����צ���,
����Ʀ��æ� �� ����������� ����-���� ������� � �����צ� �����ͦ ext2.
E2fsprogs ͦ����� e2fsck (����������դ���� ��� ����������� �������
Ц��� "�����ϧ" ������� ������), mke2fs (��� �Φ���̦��æ� ���Ħ�� ��
��������� �������ϧ ������ϧ ������� ext2), debugfs (��� ��������
����Ҧ���ϧ ��������� ������ϧ �������, ������� ������� ���������ϧ
������ϧ ������� ��� ��� ��������� ���Ԧ� ��� e2fsck), tune2fs (���
����Ʀ��æ� �������Ҧ� ������ϧ �������) �� ¦��ۦ��� ����� �������
���̦� ��� ext2fs.

%package devel
Summary:	e2fs header files
Summary(de):	Header-Dateien f�r eine e2fs
Summary(es):	Bibliotecas est�ticas y archivos de inclusi�n para e2fs
Summary(pl):	Pliki nag��wkowe do bibliotek e2fs
Summary(ru):	���������� ������������ � ������ ��� ������ � ext2fs
Summary(pt_BR):	Bibliotecas est�ticas e arquivos de inclus�o para e2fs
Summary(uk):	��̦���� ������ͦ��� �� ������ ��� ������ � ext2fs
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libext2fs2-devel

%description devel
E2fsprogs-devel contains header files and documentation needed to
develop second extended (ext2) filesystem-specific programs.

%description devel -l de
Header-Dateien, die zur Entwicklung von ext2-Dateisystemspezifischen
Programmen erforderlich sind.

%description devel -l es
Bibliotecas y archivos de inclusi�n para desarrollo de programas
espec�ficos para sistema de archivo ext2.

%description devel -l pl
Pliki nag��wkowe i dokumentacja niezb�dne do tworzenia program�w
obs�uguj�cych e2fs.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para desenvolvimento de programas
espec�ficos para sistema de arquivo ext2.

%description devel -l ru
E2fsprogs-devel �������� ���������� � ������, ����������� ���
��������� ��������, ���������� � �������� �������� ext2.

%description devel -l uk
E2fsprogs-devel ͦ����� ¦�̦����� �� ������, ����Ȧ�Φ ��� ���������
�������, �˦ �������� � �������� �������� ext2.

%package static
Summary:	e2fs static libraries
Summary(de):	e2fs statische Libraries
Summary(es):	Bibliotecas est�ticas y archivos de inclusi�n para e2fs
Summary(pl):	Biblioteki statyczne do obs�ugi e2fs
Summary(pt_BR):	Bibliotecas est�ticas e arquivos de inclus�o para e2fs
Summary(ru):	����������� ���������� ��� �������� ������ � ext2fs
Summary(uk):	������Φ ¦�̦���� ��� ������� ������ � ext2fs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries files needed to develop ext2 filesystem-specific
programs statically linked with e2progs libs.

%description static -l de
Libraries zur Entwicklung von ext2-Dateisystemspezifischen Programmen
erforderlich sind.

%description static -l es
Bibliotecas y archivos de inclusi�n para desarrollo de programas
espec�ficos para sistema de archivo ext2.

%description static -l pl
Biblioteki statyczne do ob�ugi e2fs niezb�dne do kompilacji program�w
statycznie skonsolidowanych (linkowanych) z bibliotekami do e2fs.

%description static -l pt_BR
Bibliotecas e arquivos de inclus�o para desenvolvimento de programas
espec�ficos para sistema de arquivo ext2.

%description static -l ru
E2fsprogs-devel-static �������� ����������� ����������, �����������
��� ��������� ��������, ���������� � �������� �������� ext2.

%description static -l uk
E2fsprogs-devel-static ͦ����� ������Φ ¦�̦�����, ����Ȧ�Φ ���
��������� �������, �˦ �������� � �������� �������� ext2.

%prep
%setup	-q
%patch0 -p1
gunzip < %{SOURCE1} > doc/e2compr.texinfo
patch -s -p1 < %{PATCH1}
%patch2 -p1
%patch3 -p1

%build
chmod u+w configure aclocal.m4
gettextize --copy --force
aclocal
autoconf

%configure \
	--with-root-prefix=/ \
	%{!?_without_nls:--enable-nls} \
	%{?_without_nls:--disable-nls} \
	%{?_with_allstatic:--disable-elf-shlibs} \
	%{!?_with_allstatic:--enable-elf-shlibs} \
	--enable-compression \
	%{?_without_static:--enable-dynamic-e2fsck} \
	--enable-fsck

%{__make} libs progs docs LDFLAGS="%{rpmldflags}"
cd doc
makeinfo --no-split e2compr.texinfo
cd ..

%install
rm -rf $RPM_BUILD_ROOT
export PATH=/sbin:$PATH

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

%clean
rm -rf $RPM_BUILD_ROOT

%files %{!?_without_nls:-f %{name}.lang}
%defattr(644,root,root,755)
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
%doc README RELEASE-NOTES

%{_infodir}/libext2fs.info*
%{_mandir}/man3/*
%lang(ja) %{_mandir}/ja/man3/*
%{_includedir}/*

%{!?_with_allstatic:%attr(755,root,root) %{_libdir}/lib*.so}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
