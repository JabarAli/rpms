# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Archive-Zip

Summary: Archive-Zip module for perl
Name: perl-Archive-Zip
Version: 1.16
Release: 1.2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Archive-Zip/

Source: http://www.cpan.org/modules/by-module/Archive/Archive-Zip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(Compress::Zlib) >= 1.08
Requires: perl >= 0:5.00503, perl(Compress::Zlib) >= 1.08

%description
The Archive::Zip module allows a Perl program to create, manipulate,
read, and write Zip archive files.

Zip archives can be created, or you can read from existing zip files.
Once created, they can be written to files, streams, or strings.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### FIXME: Change to real perl location. (Please fix upstream)
%{__perl} -pi -e 's|^#!/.*bin/perl|#!%{__perl}|i;' examples/*.pl

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README TODO docs/* examples/
%doc %{_mandir}/man?/*
%{_bindir}/crc32
%dir %{perl_vendorlib}/Archive/
%{perl_vendorlib}/Archive/Zip.pm
%{perl_vendorlib}/Archive/Zip.pod
%{perl_vendorlib}/Archive/Zip/

%changelog
* Wed Jul 13 2005 Dag Wieers <dag@wieers.com> - 1.16-1
- Updated to release 1.16.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.09-0
- Updated to release 1.09.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 1.05-0
- Initial package. (using DAR)
