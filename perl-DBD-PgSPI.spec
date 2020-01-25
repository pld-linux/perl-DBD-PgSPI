#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%define	pdir	DBD
%define	pnam	PgSPI
Summary:	DBD::PgSPI - PostgreSQL database driver for the DBI module
Summary(pl.UTF-8):	DBD::PgSPI - sterownik bazy danych PostgreSQL dla modułu DBI
Name:		perl-DBD-PgSPI
Version:	0.02
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cbbaf3cc3a92979aba854910a825ed2f
URL:		http://search.cpan.org/dist/DBD-PgSPI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	postgresql-backend-devel >= 0:8.2.4-3
Requires:	postgresql-module-plperl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IF YOU ARE LOOKING FOR A WAY TO ACCESS POSTGRESQL DATABASE FROM A PERL
SCRIPT RUNNING OUTSIDE OF YOUR DATABASE, LOOK AT DBD::Pg, YOU CANNOT 
USE THIS MODULE. THIS MODULE IS ONLY INTENDED FOR USE BY STORED PROCEDURES
WRITTEN IN 'plperl' PROGRAMMING LANGUAGE RUNNING INSIDE POSTGRESQL.

DBD::PgSPI is a Perl module which works with the DBI module to provide
access to PostgreSQL database from within pl/perl functions inside the
database.

%description -l pl.UTF-8
W CELU DOSTĘPU DO BAZY DANYCH POSTGRESQL Z POZIOMU SKRYPTÓW PERLOWYCH
DZIAŁAJĄCYCH POZA BAZĄ NALEŻY UŻYĆ DBD::Pg, NIE MOŻNA UŻYĆ TEGO
MODUŁU. TEN MODUŁ SŁUŻY WYŁĄCZNIE DO UŻYWANIA PRZEZ PROCEDURY
WBUDOWANE NAPISANE W JĘZYKU 'plperl' DZIAŁAJĄCE WEWNĄTRZ POSTGRESQL-a.

DBD::PgSPI to moduł Perla działający z modułem DBI dający dostęp do
bazy danych PostgreSQL z poziomu funkcji języka pl/perl wewnątrz bazy
danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MDBI::DBD -MExtUtils::MakeMaker -we 'WriteMakefile(NAME=>"DBD::PgSPI", OBJECT=>"PgSPI\$(OBJ_EXT) dbdimp\$(OBJ_EXT)",  INC=>"-I'`pg_config --includedir-server`' -I" . dbd_dbi_arch_dir(),)' \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/DBD/*.pm
%dir %{perl_vendorarch}/auto/DBD/PgSPI
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/PgSPI/*.so
%{_mandir}/man3/*
