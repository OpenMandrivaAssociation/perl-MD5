%define	module	MD5
%define	name	perl-%{module}
%define	version	2.03
%define	release	%mkrel 4

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
