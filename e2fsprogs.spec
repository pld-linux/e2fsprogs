Summary:	Tools for the second extended (ext2) filesystem 
Summary(de):	Tools für das zweite erweiterte (ext2) Dateisystem 
Summary(fr):	Outils pour le système de fichiers ext2
Summary(pl):	Narzêdzia do systemu plikowego ext2
Summary(tr):	ext2 dosya sistemi için araçlar
Name:		e2fsprogs
Version:	1.14
Release:	3
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
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
Dieses Paket enthält eine Auswahl an Utilities zum Erstellen, Prüfen 
und zur Instandsetzung von ext2-Dateisystemen.

%description -l fr
Ce package contient de nombreux utilitaires pour créer, vérifier, et
réparer les systèmes de fichiers ext2.

%description -l pl
Pakiet ten zawiera narzêdzia do tworzenia, sprawdzania i naprawiania
wolumenów dyskowych z systemem plikowym ext2.

%description -l tr
Bu paket, ext2 dosya sistemlerini yaratmak, onarmak, kontrol etmek ve bazý
parametrelerini deðiþtirmek için gerekli yazýlýmlarý içerir.

%package devel
Summary:	e2fs header files
Summary(de):	Header-Dateien für eine e2fs
Summary(pl):	Pliki nag³ówkowe do bibliotek e2fs
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
Pliki nag³ówkowe niezbêdne do tworzenia programów obs³ugukj±cych e2fs.

%package static
Summary:	e2fs static libraries
Summary(de):	e2fs statische Libraries
Summary(pl):	Biblioteki statyczne do obs³ugi e2fs
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
Biblioteki statyczne do ob³ugi e2fs niezêbdne do kompilacji programów 
statycznie skonsolidowanych (likowanych) z bibliotekami do e2fs.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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

%changelog
* Fri May 21 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.14-3]
- some macros in use, 
- gzipping %doc,
- stripping of shared libs.

* Mon Apr 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.14-2]
- fixed coredump fsck when it does not find its argument in
  /etc/fstab (e2fsprogs-fsck.patch),
- added to package findsuper (e2fsprogs-findsuper.patch),
- recompiled on new rpm.

* Fri Mar  5 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.14-1]
- added URL,
- added Group(pl),
- removed man group from man pages.

* Mon Dec 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.12-5]
- standarized {un}registering info pages (added e2fsprogs-info.patch).

* Fri Dec 11 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.12-4]
- added gzipping man pages,
- added --with-ldopts="-s" to ./configure parameters,
- added e2fsprogs-kernel21.patch which allows compile e2fsprogs on both
  2.0.x and 2.1.x kernels.

* Sun Nov 01 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.12-2d]
- build only static binaries (for emergensy use),  
- minor changes.

* Thu Oct 08 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.12-1d]
- updated to 1.12,
- fixed pl translation.

* Mon Sep 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.12-3]
- %postun changed to %preun (during uregistering e2progs info pages in 
  %postun %{_infodir}/history.info.gz don't exist).
- removed all patches.

* Wed Sep 23 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.10-7d]
- downgraded to 1.10-7d,
- translation modified for pl,
- added static subpackage,
- added %defattr support,
- fixed files permissions,
- removed at now tr, de, fr trnanslation -> generated SIGSEGV ;(
- minor modifications of the spec file.

* Sat Aug 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
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
  devel subpackage.

* Thu Jun 25 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.10-7]
- build against GNU libc-2.1, 
- added a fsck patch,
- start at RH spec.
