Summary: IMAP Client, roundcube installed in /opt/roundcube
%define name roundcube_plugins
Name: %{name}
%define version 1.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
URL: http://www.contribs.org
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
BuildArchitectures: noarch
BuildRoot: /var/tmp/%{name}-%{version}
Requires: e-smith-release >= 8.0
Requires: roundcube >= 1.0
Buildrequires: e-smith-devtools
AutoReqProv: no

%description
http://www.roundcube.net/
Roundcube_plugins provide a commonway to install and update plugins to roundcube

%changelog
* Sun Apr 13 2014 stephane de labrusse <stephdl@de-labrusse.fr> 1.0-1
- first release

%prep
%setup
%build

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT  > %{name}-%{version}-filelist

echo "%doc COPYING" >> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%pre
%preun
%post
%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

