%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	DSA
Summary:	Crypt::DSA Perl module - DSA signature and key generation
Summary(pl):	Modu� Perla Crypt::DSA - generuj�cy sygnatury i klucze DSA
Name:		perl-Crypt-DSA
Version:	0.12
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7324f8d65f041b153b6b4beeaeb9a953
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Crypt-Random >= 0.33
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-Math-Pari >= 2.001804
BuildRequires:	rpm-perlprov >= 4.1-13
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
Crypt::DSA jest implementacj� systemu weryfikacji sygnatur DSA
(Digital Signature Alghorithm). Sama implementacja jest w czystym
Perlu, ale do ci�kiej matematyki korzysta z biblioteki Math::Pari.
Pakiet umo�liwia podpisywanie i weryfikacj� sygnatur DSA oraz
generowanie kluczy. Modu� ten wymaga dodatkowo modu�u Convert::PEM
w wersji >= 0.04 do czytania i zapisywania plik�w zakodowanych PEM
oraz modu�u Data::Buffer w wersji >= 0.01 do czytania i zapisywania
plik�w z kluczami SSH2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

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
