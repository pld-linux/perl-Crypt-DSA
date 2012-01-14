#
# Conditional build
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	DSA
Summary:	Crypt::DSA Perl module - DSA signature and key generation
Summary(pl.UTF-8):	Moduł Perla Crypt::DSA - generujący sygnatury i klucze DSA
Name:		perl-Crypt-DSA
Version:	1.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0a64dcd77e796ebacad4c6af2df74b57
URL:		http://search.cpan.org/dist/Crypt-DSA/
%if %{with tests}
BuildRequires:	perl-Data-Buffer >= 0.01
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-File-Which >= 0.05
BuildRequires:	perl-Math-BigInt >= 1.78
BuildRequires:	perl-Math-BigInt-GMP
%endif
BuildRequires:	perl-Convert-PEM >= 0.07
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-File-Which >= 0.05
Requires:	perl-Math-BigInt >= 1.78
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

%description -l pl.UTF-8
Crypt::DSA jest implementacją systemu weryfikacji sygnatur DSA
(Digital Signature Alghorithm). Sama implementacja jest w czystym
Perlu, ale do ciężkiej matematyki korzysta z biblioteki Math::Pari.
Pakiet umożliwia podpisywanie i weryfikację sygnatur DSA oraz
generowanie kluczy. Moduł ten wymaga dodatkowo modułu Convert::PEM w
wersji >= 0.04 do czytania i zapisywania plików zakodowanych PEM oraz
modułu Data::Buffer w wersji >= 0.01 do czytania i zapisywania plików
z kluczami SSH2.

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
%doc Changes README
%{perl_vendorlib}/Crypt/DSA.pm
%{perl_vendorlib}/Crypt/DSA
%{_mandir}/man3/*
