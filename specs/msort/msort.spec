# $Id$
# Authority: dries
# Upstream: Bill Poser <billposer$alum,mit,edu>

Summary: Sort files in sophisticated ways
Name: msort
Version: 8.17
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://www.billposer.org/Software/msort.html

Source: http://www.billposer.org/Software/Downloads/msort-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: tre-devel

%description
Msort is a program for sorting files in sophisticated ways. Records need not 
be single lines. Key fields may be selected by position, tag, or character 
range. For each key, distinct exclusions, multigraphs, substitutions. and a 
sort order may be defined. Comparisons may be lexicographic, numeric, by 
string length, date, or time. Optional keys are supported. Msort uses the 
Unicode character set and provides full Unicode case-folding. The basic 
program has a somewhat complex command line interface, but may be driven 
by an optional GUI.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING Doc/* INSTALL NEWS README
%doc %{_mandir}/man1/msort.1*
%{_bindir}/msg
%{_bindir}/msort

%changelog
* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 8.17-1
- Updated to release 8.17.

* Sun Feb 19 2006 Dries Verachtert <dries@ulyssis.org> - 8.16-1
- Updated to release 8.16.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 8.15-1
- Updated to release 8.15.

* Mon Feb 06 2006 Dries Verachtert <dries@ulyssis.org> - 8.13-1
- Updated to release 8.13.

* Wed Nov 02 2005 Dries Verachtert <dries@ulyssis.org> - 8.10-1
- Updated to release 8.10.

* Tue Oct 18 2005 Dries Verachtert <dries@ulyssis.org> - 8.9-1
- Initial package.
