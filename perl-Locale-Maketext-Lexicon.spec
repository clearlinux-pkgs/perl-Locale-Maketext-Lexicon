#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Locale-Maketext-Lexicon
Version  : 1.00
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/D/DR/DRTECH/Locale-Maketext-Lexicon-1.00.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DRTECH/Locale-Maketext-Lexicon-1.00.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblocale-maketext-lexicon-perl/liblocale-maketext-lexicon-perl_1.00-1.debian.tar.xz
Summary  : 'Use other catalog formats in Maketext'
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: perl-Locale-Maketext-Lexicon-bin = %{version}-%{release}
Requires: perl-Locale-Maketext-Lexicon-license = %{version}-%{release}
Requires: perl-Locale-Maketext-Lexicon-man = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Locale::Maketext::Lexicon - Use other catalog formats in Maketext
VERSION
version 1.00

%package bin
Summary: bin components for the perl-Locale-Maketext-Lexicon package.
Group: Binaries
Requires: perl-Locale-Maketext-Lexicon-license = %{version}-%{release}
Requires: perl-Locale-Maketext-Lexicon-man = %{version}-%{release}

%description bin
bin components for the perl-Locale-Maketext-Lexicon package.


%package dev
Summary: dev components for the perl-Locale-Maketext-Lexicon package.
Group: Development
Requires: perl-Locale-Maketext-Lexicon-bin = %{version}-%{release}
Provides: perl-Locale-Maketext-Lexicon-devel = %{version}-%{release}

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


%prep
%setup -q -n Locale-Maketext-Lexicon-1.00
cd ..
%setup -q -T -D -n Locale-Maketext-Lexicon-1.00 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Locale-Maketext-Lexicon-1.00/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Locale-Maketext-Lexicon
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Locale-Maketext-Lexicon/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Locale-Maketext-Lexicon/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Extract.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Extract/Plugin/Base.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Extract/Plugin/FormFu.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Extract/Plugin/Generic.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Extract/Plugin/Haml.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Extract/Plugin/Mason.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Extract/Plugin/PPI.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Extract/Plugin/Perl.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Extract/Plugin/TT2.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Extract/Plugin/TextTemplate.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Extract/Plugin/YAML.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Extract/Run.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Lexicon.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Lexicon/Auto.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Lexicon/Gettext.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Lexicon/Msgcat.pm
/usr/lib/perl5/vendor_perl/5.28.1Locale/Maketext/Lexicon/Tie.pm

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
/usr/share/package-licenses/perl-Locale-Maketext-Lexicon/LICENSE
/usr/share/package-licenses/perl-Locale-Maketext-Lexicon/deblicense_copyright

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xgettext.pl.1
