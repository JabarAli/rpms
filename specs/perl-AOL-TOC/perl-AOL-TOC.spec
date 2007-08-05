# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AOL-TOC
%define real_version 0.340

Summary: AOL-TOC module for perl
Name: perl-AOL-TOC
Version: 0.34
Release: 1.2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AOL-TOC/

Source: http://search.cpan.org/CPAN/authors/id/J/JH/JHARDING/AOL-TOC-%{real_version}.tar.gz
#Source: http://www.cpan.org/modules/by-module/AOL/AOL-TOC-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Perl extension for interfacing with AOL's AIM service.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/*

%changelog
* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 0.340-1
- Initial package. (using DAR)
