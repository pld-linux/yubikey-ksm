Summary:	The YubiKey Key Storage Module
Name:		yubikey-ksm
Version:	1.5
Release:	0.1
License:	BSD
Group:		Applications/System
URL:		http://code.google.com/p/yubikey-ksm/
Source0:	http://yubikey-ksm.googlecode.com/files/%{name}-%{version}.tgz
Patch0:		%{name}-Makefile.patch
BuildRequires:	perl-generators
Requires:	php(core)
Requires:	php(mcrypt)
Requires:	php(pdo)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The YubiKey Key Storage Module (YK-KSM) provides a AES key storage
facility for use with a YubiKey validation server.

%prep
%setup -q
%patch0 -p0
cp .htaccess htaccess

%build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	etcprefix=$RPM_BUILD_ROOT%{_sysconfdir}/ykksm \
	binprefix=$RPM_BUILD_ROOT%{_bindir} \
	phpprefix=$RPM_BUILD_ROOT%{_datadir}/ykksm \
	docprefix=$RPM_BUILD_ROOT%{_docdir}/ykksm

rm -rf $RPM_BUILD_ROOT%{_docdir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/ykksm/.htaccess

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/ykksm/ykksm-config.php
%dir %{_sysconfdir}/ykksm/
%attr(755,root,root) %{_bindir}/ykksm-*
%{_datadir}/ykksm
%doc doc/* ykksm-db.sql htaccess
