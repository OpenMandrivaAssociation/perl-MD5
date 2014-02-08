%define	module	MD5
%define	name	perl-%{module}
%define	version	2.03
%define release	12

Summary:	The Perl interface to the RSA Message Digest Algorithm
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/author/GAAS/%{module}-%{version}/
Source0:	ftp://ftp.perl.org//pub/CPAN/modules/by-module/%{module}/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch:	noarch

%description
The perl-MD5 package provides the MD5 module for the Perl
programming language.  MD5 is a Perl interface to the RSA Data
Security Inc. Message Digest Algorithm, which allows Perl
programs to use the algorithm.

The perl-MD5 package should be installed if any Perl programs
on your system are going to use RSA's Message Digest Algorithm.

%prep
%setup -q -n %{module}-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor --defaultdeps
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc MANIFEST README
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.03-10mdv2012.0
+ Revision: 765477
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.03-9
+ Revision: 763971
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.03-8
+ Revision: 667225
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.03-7mdv2011.0
+ Revision: 426517
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.03-6mdv2009.0
+ Revision: 223816
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.03-5mdv2008.1
+ Revision: 180416
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 2.03-4mdv2008.0
+ Revision: 74274
- bump release

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 2.03-3mdv2008.0
+ Revision: 73533
- spec file cleansing


* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 19:44:05 (41185)
- rebuild && mkrel

* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 19:42:09 (41184)
Import perl-MD5

* Wed Apr 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.03-1mdk
- 2.03
- drop PREFIX
- use %%makeinstall_std macro
- spec cosmetics

* Fri Aug 01 2003 Ben Reser <ben@reser.org> 2.02-3mdk
- Fix ManPath
- rm buildroot in %%install not %%prep
- macroification
- fix build/install for new perl
- unpackaged perllocal.pod
- Quiet setup

