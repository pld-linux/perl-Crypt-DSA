
# Conditional build
%bcond_without	tests	# Do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	DSA
Summary:	Crypt::DSA Perl module - DSA signature and key generation
Summary(pl):	Modu³ Perla Crypt::DSA - generuj±cy sygnatury i klucze DSA
Name:		perl-Crypt-DSA
Version:	0.12
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7324f8d65f041b153b6b4beeaeb9a953
%if %{with tests}
BuildRequires:	perl-Crypt-Random >= 0.33
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-Math-Pari >= 2.001804
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
Requires:	perl-Crypt-Random >= 0.33
Requires:	perl-Math-Pari >= 2.001804
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional
%define		_noautoreq 'perl(Convert::PEM)' 'perl(Data::Buffer)'

%description
Crypt::DSA is an implementation of the DSA (Digital Signature
Algorithm) signature verification system. The implementation itself is
pure Perl, although the heavy-duty mathematics underneath are provided
by the Math::Pari library. This package provides DSA signing,
signature verification, and key generation. It additionally requires
Convert::PEM >= 0.04 module to read/write PEM-encoded files and
Data::Buffer >= 0.01 module to read/write SSH2 keyfiles.

%description -l pl
Crypt::DSA jest implementacj± systemu weryfikacji sygnatur DSA
(Digital Signature Alghorithm). Sama implementacja jest w czystym
Perlu, ale do ciê¿kiej matematyki korzysta z biblioteki Math::Pari.
Pakiet umo¿liwia podpisywanie i weryfikacjê sygnatur DSA oraz
generowanie kluczy. Modu³ ten wymaga dodatkowo modu³u Convert::PEM
w wersji >= 0.04 do czytania i zapisywania plików zakodowanych PEM
oraz modu³u Data::Buffer w wersji >= 0.01 do czytania i zapisywania
plików z kluczami SSH2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%{perl_vendorlib}/Crypt/DSA.pm
%{perl_vendorlib}/Crypt/DSA
%{_mandir}/man3/*
