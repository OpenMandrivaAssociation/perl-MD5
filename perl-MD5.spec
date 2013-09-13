%define	module	MD5

Summary:	The Perl interface to the RSA Message Digest Algorithm
Name:		perl-%{module}
Version:	2.03
Release:	11
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/author/GAAS/%{module}-%{version}/
Source0:	ftp://ftp.perl.org//pub/CPAN/modules/by-module/%{module}/%{module}-%{version}.tar.bz2
Buildarch:	noarch
Buildrequires:	perl-devel

%description
The perl-MD5 package provides the MD5 module for the Perl
programming language.  MD5 is a Perl interface to the RSA Data
Security Inc. Message Digest Algorithm, which allows Perl
programs to use the algorithm.

The perl-MD5 package should be installed if any Perl programs
on your system are going to use RSA's Message Digest Algorithm.

%prep
%setup -qn %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor --defaultdeps
%make

%install
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc MANIFEST README
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*

