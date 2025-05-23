#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Locale-Maketext-Lexicon
Version  : 1.00
Release  : 33
URL      : https://cpan.metacpan.org/authors/id/D/DR/DRTECH/Locale-Maketext-Lexicon-1.00.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DRTECH/Locale-Maketext-Lexicon-1.00.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblocale-maketext-lexicon-perl/liblocale-maketext-lexicon-perl_1.00-1.debian.tar.xz
Summary  : 'Use other catalog formats in Maketext'
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: perl-Locale-Maketext-Lexicon-bin = %{version}-%{release}
Requires: perl-Locale-Maketext-Lexicon-license = %{version}-%{release}
Requires: perl-Locale-Maketext-Lexicon-man = %{version}-%{release}
Requires: perl-Locale-Maketext-Lexicon-perl = %{version}-%{release}
Requires: perl(PPI)
Requires: perl(Text::Haml)
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Locale::Maketext::Lexicon - Use other catalog formats in Maketext
VERSION
version 1.00

%package bin
Summary: bin components for the perl-Locale-Maketext-Lexicon package.
Group: Binaries
Requires: perl-Locale-Maketext-Lexicon-license = %{version}-%{release}

%description bin
bin components for the perl-Locale-Maketext-Lexicon package.


%package dev
Summary: dev components for the perl-Locale-Maketext-Lexicon package.
Group: Development
Requires: perl-Locale-Maketext-Lexicon-bin = %{version}-%{release}
Provides: perl-Locale-Maketext-Lexicon-devel = %{version}-%{release}
Requires: perl-Locale-Maketext-Lexicon = %{version}-%{release}

%description dev
dev components for the perl-Locale-Maketext-Lexicon package.


%package license
Summary: license components for the perl-Locale-Maketext-Lexicon package.
Group: Default

%description license
license components for the perl-Locale-Maketext-Lexicon package.


%package man
Summary: man components for the perl-Locale-Maketext-Lexicon package.
Group: Default

%description man
man components for the perl-Locale-Maketext-Lexicon package.


%package perl
Summary: perl components for the perl-Locale-Maketext-Lexicon package.
Group: Default
Requires: perl-Locale-Maketext-Lexicon = %{version}-%{release}

%description perl
perl components for the perl-Locale-Maketext-Lexicon package.


%prep
%setup -q -n Locale-Maketext-Lexicon-1.00
cd %{_builddir}
tar xf %{_sourcedir}/liblocale-maketext-lexicon-perl_1.00-1.debian.tar.xz
cd %{_builddir}/Locale-Maketext-Lexicon-1.00
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Locale-Maketext-Lexicon-1.00/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Locale-Maketext-Lexicon
cp %{_builddir}/Locale-Maketext-Lexicon-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Locale-Maketext-Lexicon/82a1e27b375f6af0fef88443b16725d9729e81b5 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Locale-Maketext-Lexicon/354b6c96b8e93cffdd1bfe71b950acb0d11eabb5 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xgettext.pl

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Locale::Maketext::Extract.3
/usr/share/man/man3/Locale::Maketext::Extract::Plugin::Base.3
/usr/share/man/man3/Locale::Maketext::Extract::Plugin::FormFu.3
/usr/share/man/man3/Locale::Maketext::Extract::Plugin::Generic.3
/usr/share/man/man3/Locale::Maketext::Extract::Plugin::Haml.3
/usr/share/man/man3/Locale::Maketext::Extract::Plugin::Mason.3
/usr/share/man/man3/Locale::Maketext::Extract::Plugin::PPI.3
/usr/share/man/man3/Locale::Maketext::Extract::Plugin::Perl.3
/usr/share/man/man3/Locale::Maketext::Extract::Plugin::TT2.3
/usr/share/man/man3/Locale::Maketext::Extract::Plugin::TextTemplate.3
/usr/share/man/man3/Locale::Maketext::Extract::Plugin::YAML.3
/usr/share/man/man3/Locale::Maketext::Extract::Run.3
/usr/share/man/man3/Locale::Maketext::Lexicon.3
/usr/share/man/man3/Locale::Maketext::Lexicon::Auto.3
/usr/share/man/man3/Locale::Maketext::Lexicon::Gettext.3
/usr/share/man/man3/Locale::Maketext::Lexicon::Msgcat.3
/usr/share/man/man3/Locale::Maketext::Lexicon::Tie.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Locale-Maketext-Lexicon/354b6c96b8e93cffdd1bfe71b950acb0d11eabb5
/usr/share/package-licenses/perl-Locale-Maketext-Lexicon/82a1e27b375f6af0fef88443b16725d9729e81b5

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xgettext.pl.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
