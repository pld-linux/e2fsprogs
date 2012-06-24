Summary:	Tools for the second extended (ext2) filesystem 
Summary(de):	Tools f�r das zweite erweiterte (ext2) Dateisystem 
Summary(fr):	Outils pour le syst�me de fichiers ext2
Summary(pl):	Narz�dzia do systemu plikowego ext2
Summary(tr):	ext2 dosya sistemi i�in ara�lar
Name:		e2fsprogs
Version:	1.14
Release:	2
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source:		ftp://tsx-11.mit.edu/pub/linux/packages/ext2fs/%{name}-%{version}.tar.gz
Patch0:		e2fsprogs-info.patch
Patch1:		e2fsprogs-fsck.patch
Patch2:		e2fsprogs-findsuper.patch
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
Biblioteki statyczne do obsugi e2fs niezbdne do kompilacji program�w 
statycznie skonsolidowanych (likowanych) z bibliotekami do e2fs.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
	--enable-elf-shlibs \
	--with-ldopts="-s"

make libs progs docs

%install
rm -rf $RPM_BUILD_ROOT
export PATH=/sbin:$PATH

make install DESTDIR=$RPM_BUILD_ROOT
make install-libs DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/lib/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man{1,8}/*

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
/usr/sbin/*
%{_bindir}/*
/lib/lib*.so.*.*
%attr(644,root,root) %{_mandir}/man[18]/*

%files devel
%defattr(644, root, root, 755)
%doc README RELEASE-NOTES
%{_infodir}/libext2fs.info*
/usr/include/*
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Mon Apr 19 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.14-2]
- fixed coredump fsck when it does not find its argument in
  /etc/fstab (e2fsprogs-fsck.patch),
- added to package findsuper (e2fsprogs-findsuper.patch),
- recompiled on new rpm.

* Fri Mar  5 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.14-1]
- added URL,
- added Group(pl),
- removed man group from man pages.

* Mon Dec 27 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.12-5]
- standarized {un}registering info pages (added e2fsprogs-info.patch).

* Fri Dec 11 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.12-4]
- added gzipping man pages,
- added --with-ldopts="-s" to ./configure parameters,
- added e2fsprogs-kernel21.patch which allows compile e2fsprogs on both
  2.0.x and 2.1.x kernels.

* Mon Sep 28 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.12-3]
- %postun changed to %preun (during uregistering e2progs info pages in 
  %postun %{_infodir}/history.info.gz don't exist).
- removed all patches.

* Sat Aug 15 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.10-7]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- added pl translation,
- fixed %post{un},
- added "rm -rf $RPM_BUILD_ROOT" on bigin %install,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added stripping shared libraries,
- fiew simplification in %files and %install,
- added %post{un} sections with registration info pages for libext2fs in
  devel subpackage,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- include <asm/types.h> to match kernel types in utils

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Wed Oct 01 1997 Erik Troan <ewt@redhat.com>
- fixed broken llseek() prototype 

* Wed Aug 20 1997 Erik Troan <ewt@redhat.com>
- added patch to prototype llseek

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
