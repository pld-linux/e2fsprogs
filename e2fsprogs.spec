Summary:     Tools for the second extended (ext2) filesystem 
Summary(de): Tools für das zweite erweiterte (ext2) Dateisystem 
Summary(fr): Outils pour le système de fichiers ext2
Summary(pl): Narzedzia do systemu plikowego ext2
Summary(tr): ext2 dosya sistemi için araçlar
Name:        e2fsprogs
Version:     1.12
Release:     3
Copyright:   GPL
Group:       Utilities/System
Source:      ftp://tsx-11.mit.edu/pub/linux/packages/ext2fs/%{name}-%{version}.tar.gz
Buildroot:   /tmp/%{name}-%{version}-root

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
Summary:     e2fs header files
Summary(de): Header-Dateien für eine e2fs
Summary(pl): Pliki nag³ówkowe do bibliotek e2fs
Group:       Development/Libraries
Prereq:      /sbin/install-info
Requires:    %{name} = %{version}

%description devel
Header files needed to develop ext2 filesystem-specific programs.

%description -l de devel
Header-Dateien, die zur Entwicklung von ext2-Dateisystemspezifischen
Programmen erforderlich sind.

%description devel
Pliki nag³ówkowe niezbêdne do tworzenia programów obs³ugukj±cych e2fs.

%package static
Summary:     e2fs static libraries
Summary(de): e2fs statische Libraries
Summary(pl): biblioteki statyczne do obs³ugi e2fs
Group:       Development/Libraries
Requires:    %{name}-devel = %{version}

%description static
Static libraries files needed to develop ext2 filesystem-specific
programs statically linked with e2progs libs.

%description -l de static
Libraries zur Entwicklung von ext2-Dateisystemspezifischen
Programmen erforderlich sind.

%description -l pl static
Biblioteki statyczne do obsugi e2fs niezbdne do kompilacji programów 
statycznie skonsolidowanych (likowanych) z bibliotekami do e2fs.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure --enable-elf-shlibs

make libs progs docs

%install
rm -rf $RPM_BUILD_ROOT

export PATH=/sbin:$PATH                                                         
make install DESTDIR="$RPM_BUILD_ROOT"                                          
make install-libs DESTDIR="$RPM_BUILD_ROOT"                                     

strip $RPM_BUILD_ROOT/lib/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   devel
/sbin/install-info /usr/info/history.info.gz /etc/info-dir \
--entry="* libext2fs: (libext2fs)                        The EXT2FS library."

%preun devel
/sbin/install-info --delete /usr/info/history.info.gz /etc/info-dir \
--entry="* libext2fs: (libext2fs)                        The EXT2FS library."

%files
%defattr(755, root, root)
/sbin/*
/usr/sbin/*
/usr/bin/*
/lib/lib*.so.*.*
%attr(644, root,  man) /usr/man/man[18]/*

%files devel
%defattr(644, root, root, 755)
%doc README RELEASE-NOTES
/usr/info/libext2fs.info*
/usr/include/
/usr/lib/lib*.so

%files static
%attr(644, root, root) /usr/lib/lib*.a

%changelog
* Mon Sep 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.12-3]
- %postun changed to %preun (during uregistering e2progs info pages in 
  %postun /usr/info/history.info.gz don't exist).
- removed all patches.

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
  devel subpackage,
- added %attr and %defattr macros in %files (allow build package from
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
