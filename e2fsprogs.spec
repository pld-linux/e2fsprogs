Summary:	Tools for the second extended (ext2) filesystem
Summary(de):	Tools für das zweite erweiterte (ext2) Dateisystem
Summary(fr):	Outils pour le système de fichiers ext2
Summary(pl):	Narzêdzia do systemu plikowego ext2
Summary(tr):	ext2 dosya sistemi için araçlar
Name:		e2fsprogs
Version:	1.21
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://download.sourceforge.net/pub/sourceforge/e2fsprogs/%{name}-%{version}.tar.gz
Source1:	http://opensource.captech.com/e2compr/ftp/e2compr-0.4.texinfo.gz
Patch0:		%{name}-info.patch
URL:		http://e2fsprogs.sourceforge.net/
PreReq:		/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%if %{?BOOT:1}%{!?BOOT:0}
BuildRequires:	glibc-static
%endif

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
Dieses Paket enthält eine Auswahl an Utilities zum Erstellen, Prüfen
und zur Instandsetzung von ext2-Dateisystemen.

%description -l fr
Ce package contient de nombreux utilitaires pour créer, vérifier, et
réparer les systèmes de fichiers ext2.

%description -l pl
Pakiet ten zawiera narzêdzia do tworzenia, sprawdzania i naprawiania
wolumenów dyskowych z systemem plikowym ext2. E2fsprogs zawiera e2fsck
(u¿ywany do naprawiania niespójno¶ci w systemie plikowym po
nipoprawnym zamkniêciu ststemu), mke2fs (u¿ywany do inicjacji
wolumenów ext2), debugfs (¿ywany do sprawdzania wewnêtrznej struktóry
wolumenów ext2, a tak¿e do recznego naprawiania b³êdów), tune2fs
(u¿ywany do modyfikacji parametrów eolumenów ext2) i kilka innych
narzêdzi do ext2.

%description -l tr
Bu paket, ext2 dosya sistemlerini yaratmak, onarmak, kontrol etmek ve
bazý parametrelerini deðiþtirmek için gerekli yazýlýmlarý içerir.

%package devel
Summary:	e2fs header files
Summary(de):	Header-Dateien für eine e2fs
Summary(pl):	Pliki nag³ówkowe do bibliotek e2fs
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
E2fsprogs-devel contand header files and documentation needed to
develop second extended (ext2) filesystem-specific programs.

%description -l de devel
Header-Dateien, die zur Entwicklung von ext2-Dateisystemspezifischen
Programmen erforderlich sind.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja niezbêdne do tworzenia programów
obs³ugukj±cych e2fs.

%package static
Summary:	e2fs static libraries
Summary(de):	e2fs statische Libraries
Summary(pl):	Biblioteki statyczne do obs³ugi e2fs
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries files needed to develop ext2 filesystem-specific
programs statically linked with e2progs libs.

%description -l de static
Libraries zur Entwicklung von ext2-Dateisystemspezifischen Programmen
erforderlich sind.

%description -l pl static
Biblioteki statyczne do ob³ugi e2fs niezêbdne do kompilacji programów
statycznie skonsolidowanych (likowanych) z bibliotekami do e2fs.

%package BOOT
Summary:	e2fs for bootdisk
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description BOOT
E2fsprogs-devel contand header files and documentation needed to
develop second extended (ext2) filesystem-specific programs. Thios package
is for bootdisk.

%prep
%setup  -q
%patch0 -p1

gunzip < %{SOURCE1} > doc/e2compr.texinfo

%build
autoconf

%if %{?BOOT:1}%{!?BOOT:0}

%configure \
	--with-root-prefix=/ \
	--disable-nls \
	--enable-compression \
	--enable-all-static \
	--disable-fsck \
	--enable-static-e2fsck \

# some problems compiling with uClibc
#%{__make} libs progs \
#	ALL_LDFLAGS="-nostdlib -s" \
#	CFLAGS="-I%{_libdir}/bootdisk%{_includedir}" \
#	LDLIBS="%{_libdir}/bootdisk%{_libdir}/crt0.o %{_libdir}/bootdisk%{_libdir}/libc.a -lgcc"

%{__make} libs
#%{__make} progs ALL_LDFLAGS="-nostdlib -s" LDLIBS="%{_libdir}/libc.a"
%{__make} progs ALL_LDFLAGS="-static -s" \
%ifarch %{ix86}
XTRA_CFLAGS="-m386"
%else
XTRA_CFLAGS=""
%endif

mv e2fsck/e2fsck e2fsck-BOOT
for i in badblocks mke2fs; do 
	mv misc/$i $i-BOOT
done

%{__make} distclean
%endif

%configure \
	--with-root-prefix=/ \
	--enable-nls \
	--enable-elf-shlibs \
	--enable-compression \
	%{?_without_static:--enable-dynamic-e2fsck} \
	--enable-fsck



%{__make} libs progs docs
cd doc
makeinfo --no-split e2compr.texinfo 
cd ..


%install
rm -rf $RPM_BUILD_ROOT
export PATH=/sbin:$PATH

%if %{?BOOT:1}%{!?BOOT:0}
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk/sbin
for i in *-BOOT; do 
  install -s $i $RPM_BUILD_ROOT%{_libdir}/bootdisk/sbin/`basename $i -BOOT`
done
%endif

%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__make} install-libs DESTDIR=$RPM_BUILD_ROOT

ln -sf e2fsck $RPM_BUILD_ROOT/sbin/fsck.ext2
ln -sf e2fsck $RPM_BUILD_ROOT/sbin/fsck.ext3
ln -sf mke2fs $RPM_BUILD_ROOT/sbin/mkfs.ext2


install doc/e2compr.info $RPM_BUILD_ROOT%{_infodir}

%post   
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun 
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post  devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /lib/lib*.so.*
%{_mandir}/man[18]/*
%{_datadir}/et
%{_datadir}/ss
%{_infodir}/e2compr.info*

%files devel
%defattr(644,root,root,755)
%doc README RELEASE-NOTES

%{_infodir}/libext2fs.info*
%{_mandir}/man3/*
%{_includedir}/*

%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{?BOOT:1}%{!?BOOT:0}
%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/bootdisk/sbin/*
%endif
