Summary:	The YubiKey Key Storage Module
Summary(pl.UTF-8):	YubiKey Key Storage Module - moduł przechowywania kluczy
Name:		yubikey-ksm
Version:	1.15
Release:	1
License:	BSD
Group:		Applications/System
Source0:	https://developers.yubico.com/yubikey-ksm/Releases/%{name}-%{version}.tgz
# Source0-md5:	b1040524edb0b52899154920716f3f66
Patch0:		%{name}-Makefile.patch
URL:		https://developers.yubico.com/yubikey-ksm/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core)
Requires:	php(mcrypt)
Requires:	php(pdo)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear	ykksm-.*

%description
The YubiKey Key Storage Module (YK-KSM) provides a AES key storage
facility for use with a YubiKey validation server.

%description -l pl.UTF-8
YubiKey Key Storage Module (YK-KSM) pozwala na przechowywanie kluczy
AES w użyciu wraz z serwerem sprawdzających poprawność YubiKey.

%prep
%setup -q
%patch0 -p1
cp .htaccess htaccess

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	etcprefix=$RPM_BUILD_ROOT%{_sysconfdir}/ykksm \
	binprefix=$RPM_BUILD_ROOT%{_bindir} \
	phpprefix=$RPM_BUILD_ROOT%{_datadir}/ykksm \
	manprefix=$RPM_BUILD_ROOT%{_mandir}/man1 \
	docprefix=$RPM_BUILD_ROOT%{_docdir}/ykksm

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/ykksm
%{__rm} $RPM_BUILD_ROOT%{_datadir}/ykksm/.htaccess

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README doc/*.txt ykksm-db.sql htaccess
%dir %{_sysconfdir}/ykksm
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ykksm/ykksm-config.php
%attr(755,root,root) %{_bindir}/ykksm-*
%{_datadir}/ykksm
%{_mandir}/man1/ykksm-*.1*
