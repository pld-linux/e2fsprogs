# conditional build:
# _without_embed - don't build uClibc version
Summary:	Tools for the second extended (ext2) filesystem
Summary(de):	Tools für das zweite erweiterte (ext2) Dateisystem
Summary(fr):	Outils pour le système de fichiers ext2
Summary(pl):	Narzêdzia do systemu plikowego ext2
Summary(tr):	ext2 dosya sistemi için araçlar
Name:		e2fsprogs
Version:	1.25
Release:	3
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://download.sourceforge.net/pub/sourceforge/e2fsprogs/%{name}-%{version}.tar.gz
Source1:	http://opensource.captech.com/e2compr/ftp/e2compr-0.4.texinfo.gz
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		e2compr-info.patch
Patch2:		%{name}-mountlabel3.patch
URL:		http://e2fsprogs.sourceforge.net/
PreReq:		/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
%if %{!?_without_embed:1}%{?_without_embed:0}
BuildRequires:	uClibc-devel
BuildRequires:	uClibc-static
%endif

%define embed_path	/usr/lib/embed
%define embed_cc	%{_arch}-uclibc-cc
%define embed_cflags	%{rpmcflags} -Os
%define uclibc_prefix	/usr/%{_arch}-linux-uclibc

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
niepoprawnym zamkniêciu systemu), mke2fs (u¿ywany do inicjacji
wolumenów ext2), debugfs (¿ywany do sprawdzania wewnêtrznej struktury
wolumenów ext2, a tak¿e do rêcznego naprawiania b³êdów), tune2fs
(u¿ywany do modyfikacji parametrów wolumenów ext2) i kilka innych
narzêdzi do ext2.

%description -l tr
Bu paket, ext2 dosya sistemlerini yaratmak, onarmak, kontrol etmek ve
bazı parametrelerini değiştirmek için gerekli yazılımları içerir.

%package devel
Summary:	e2fs header files
Summary(de):	Header-Dateien für eine e2fs
Summary(pl):	Pliki nag³ówkowe do bibliotek e2fs
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
E2fsprogs-devel contand header files and documentation needed to
develop second extended (ext2) filesystem-specific programs.

%description -l de devel
Header-Dateien, die zur Entwicklung von ext2-Dateisystemspezifischen
Programmen erforderlich sind.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja niezbêdne do tworzenia programów
obs³uguj±cych e2fs.

%package static
Summary:	e2fs static libraries
Summary(de):	e2fs statische Libraries
Summary(pl):	Biblioteki statyczne do obs³ugi e2fs
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static libraries files needed to develop ext2 filesystem-specific
programs statically linked with e2progs libs.

%description -l de static
Libraries zur Entwicklung von ext2-Dateisystemspezifischen Programmen
erforderlich sind.

%description -l pl static
Biblioteki statyczne do ob³ugi e2fs niezbêdne do kompilacji programów
statycznie skonsolidowanych (linkowanych) z bibliotekami do e2fs.

%package embed
Summary:	e2fs for bootdisk
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description embed
E2fsprogs-devel contains header files and documentation needed to
develop second extended (ext2) filesystem-specific programs. This
package is for bootdisk.

%package devel-embed
Summary:	e2fs header files for bootdisk
Summary(de):	Header-Dateien für eine e2fs
Summary(pl):	Pliki nag³ówkowe do bibliotek e2fs
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ

%description devel-embed
E2fsprogs-devel contand header files and documentation needed to
develop second extended (ext2) filesystem-specific programs.
Botodisk version.

%prep
%setup  -q
%patch0 -p1
gunzip < %{SOURCE1} > doc/e2compr.texinfo
patch -s -p1 < %{PATCH1}
%patch2 -p1

%build
chmod u+w configure aclocal.m4
gettextize --copy --force
aclocal
autoconf

%if %{!?_without_embed:1}%{?_without_embed:0}
%configure \
	--with-root-prefix=/ \
	--disable-nls \
	--enable-compression \
	--enable-all-static \
	--disable-fsck \
	--with-cc=%{embed_cc} \
	--with-ccopts="%{embed_cflags}"
%{__make} libs
%{__make} progs
mv e2fsck/e2fsck e2fsck-embed-shared
for i in badblocks mke2fs; do 
	mv misc/$i $i-embed-shared
done
%{__make} progs ALL_LDFLAGS="-static"
mv e2fsck/e2fsck e2fsck-embed-static
for i in badblocks mke2fs; do 
	mv misc/$i $i-embed-static
done
mkdir embed-libs
cp lib/*.a embed-libs
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

%{__make} install	DESTDIR=$RPM_BUILD_ROOT
%{__make} install-libs	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C po install	DESTDIR=$RPM_BUILD_ROOT

%if %{!?_without_embed:1}%{?_without_embed:0}
install -d $RPM_BUILD_ROOT%{embed_path}/{shared,static}
install -d $RPM_BUILD_ROOT%{uclibc_prefix}/{include,lib}
for i in badblocks mke2fs e2fsck; do 
	install $i-embed-shared $RPM_BUILD_ROOT%{embed_path}/shared/$i
	install $i-embed-static $RPM_BUILD_ROOT%{embed_path}/static/$i
done
cp -a $RPM_BUILD_ROOT%{_includedir}/* $RPM_BUILD_ROOT%{uclibc_prefix}/include
cp embed-libs/* $RPM_BUILD_ROOT%{uclibc_prefix}/lib
%endif

ln -sf e2fsck $RPM_BUILD_ROOT/sbin/fsck.ext2
ln -sf e2fsck $RPM_BUILD_ROOT/sbin/fsck.ext3
ln -sf mke2fs $RPM_BUILD_ROOT/sbin/mkfs.ext2

install doc/e2compr.info $RPM_BUILD_ROOT%{_infodir}

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /lib/lib*.so.*
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

%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{!?_without_embed:1}%{?_without_embed:0}
%files embed
%defattr(644,root,root,755)
%attr(755,root,root) %{embed_path}/*/*

%files devel-embed
%{uclibc_prefix}/include/*
%{uclibc_prefix}/lib/*
%endif
