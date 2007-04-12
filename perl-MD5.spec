%define	module	MD5
%define	name	perl-%{module}
%define	version	2.03
%define	release	%mkrel 2

Summary:	The Perl interface to the RSA Message Digest Algorithm.
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
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std
%{__rm} -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc MANIFEST README
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*


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

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.02-2mdk
- buildrequires

* Tue Mar 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.02-1mdk
- 2.02

* Thu Aug 23 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.7-12mdk
- rebuild

* Thu May 17 2001 David BAUDENS <baudens@mandrakesoft.com> 1.7-11mdk
- Use %%_tmppath for BuildRoot

* Tue Sep 12 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.7-10mdk
- clean spec

* Wed Dec 15 1999 François PONS <fpons@mandrakesoft.com>
- Corrected location of man pages to /usr/lib/perl5/man.

* Tue Nov 23 1999 François PONS <fpons@mandrakesoft.com>
- Build release.

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Mon Apr 19 1999 Cristian Gafton <gafton@redhat.com>
- rebuild to catch perl version change

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Thu Jan 21 1999 Bill Nottingham <notting@redhat.com>
- build for 6.0

* Sun Jun 21 1998 Jeff Johnson <jbj@redhat.com>
- add %clean

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- added the shared lib module to the package

* Sat Apr 11 1998 Bryan C. Andregg <bandregg@redhat.com>
- First build.
