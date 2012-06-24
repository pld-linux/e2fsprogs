Summary:	Tools for the second extended (ext2) filesystem 
Summary(de):	Tools f�r das zweite erweiterte (ext2) Dateisystem 
Summary(fr):	Outils pour le syst�me de fichiers ext2
Summary(pl):	Narz�dzia do systemu plikowego ext2
Summary(tr):	ext2 dosya sistemi i�in ara�lar
Name:		e2fsprogs
Version:	1.15
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source:		ftp://tsx-11.mit.edu/pub/linux/packages/ext2fs/%{name}-%{version}.tar.gz
Patch0:		e2fsprogs-info.patch
URL:		http://web.mit.edu/tytso/www/linux/e2fsprogs.html
Buildroot:	/tmp/%{name}-%{version}-root

%description
This package includes a number of utilities for creating, checking,
and repairing ext2 filesystems.

%description -l de
Dieses Paket enth�lt eine Auswahl an Utilities zum Erstellen, Pr�fen 
und zur Instandsetzung von ext2-Dateisystemen.

%description -l fr
Ce package contient de nombreux utilitaires pour cr�er, v�rifier, et
r�parer les syst�mes de fichiers ext2.

%description -l pl
Pakiet ten zawiera narz�dzia do tworzenia, sprawdzania i naprawiania
wolumen�w dyskowych z systemem plikowym ext2.

%description -l tr
Bu paket, ext2 dosya sistemlerini yaratmak, onarmak, kontrol etmek ve baz�
parametrelerini de�i�tirmek i�in gerekli yaz�l�mlar� i�erir.

%package devel
Summary:	e2fs header files
Summary(de):	Header-Dateien f�r eine e2fs
Summary(pl):	Pliki nag��wkowe do bibliotek e2fs
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Prereq:		/sbin/install-info
Requires:	%{name} = %{version}

%description devel
Header files needed to develop ext2 filesystem-specific programs.

%description -l de devel
Header-Dateien, die zur Entwicklung von ext2-Dateisystemspezifischen
Programmen erforderlich sind.

%description devel
Pliki nag��wkowe niezb�dne do tworzenia program�w obs�ugukj�cych e2fs.

%package static
Summary:	e2fs static libraries
Summary(de):	e2fs statische Libraries
Summary(pl):	Biblioteki statyczne do obs�ugi e2fs
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries files needed to develop ext2 filesystem-specific
programs statically linked with e2progs libs.

%description -l de static
Libraries zur Entwicklung von ext2-Dateisystemspezifischen
Programmen erforderlich sind.

%description -l pl static
Biblioteki statyczne do ob�ugi e2fs niez�bdne do kompilacji program�w 
statycznie skonsolidowanych (likowanych) z bibliotekami do e2fs.

%prep
%setup  -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--enable-elf-shlibs \
	--with-ldopts="-s" \
	--infodir=%{_infodir}

make libs progs docs

%install
rm -rf $RPM_BUILD_ROOT
export PATH=/sbin:$PATH

make install DESTDIR=$RPM_BUILD_ROOT
make install-libs DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}
mv $RPM_BUILD_ROOT/usr/man/man{1,8} $RPM_BUILD_ROOT%{_mandir}

strip --strip-unneeded $RPM_BUILD_ROOT/lib/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man{1,8}/* README RELEASE-NOTES

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post  devel
/sbin/install-info %{_infodir}/libext2fs.info.gz /etc/info-dir

%preun devel
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/libext2fs.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
/sbin/*
%{_sbindir}/*
%{_bindir}/*
/lib/lib*.so.*
%attr(644,root,root) %{_mandir}/man[18]/*

%files devel
%defattr(644,root,root,755)
%doc {README,RELEASE-NOTES}.gz

%{_infodir}/libext2fs.info*
%{_includedir}/*

%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
