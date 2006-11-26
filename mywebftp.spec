# TODO
# - webapps
Summary:	Little PHP Tool to manage your webspace, through a web browser
Summary(pl):	Aplikacja w PHP do zarz±dzania przestrzeni± WWW poprzez przegl±darkê
Name:		mywebftp
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/mywebftp/%{name}%{version}.zip
# Source0-md5:	82e9ece26f7e3d3f9a8121908b8de90c
Source1:	%{name}.conf
URL:		http://mywebftp.sourceforge.net/
BuildRequires:	unzip
Requires:	php(pcre)
Requires:	webserver
Requires:	webserver(php)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_mywebftpdir	%{_datadir}/%{name}
%define		_sysconfdir	/etc/%{name}

%description
MyWebFTP is a little PHP Tool that allows you to manage you files and
directories on your webspace, through a web browser. Usefull when you
are behind a restrictive proxy and more handy than an heavy software
FTP Client. Uses only PHP file functions..

%description -l pl
MyWebFTP to ma³e narzêdzie w PHP, które pozwala na zarz±dzanie poprzez
przegl±darkê plikami i katalogami znajduj±cymi siê w okre¶lonej
przestrzeni WWW. Program ten staje siê bardzo przydatny dla
u¿ytkowników znajduj±cych siê za restrykcyjnym proxy, gdy¿ u¿ywa tylko
funkcji PHP.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mywebftpdir} \
	$RPM_BUILD_ROOT{%{_sysconfdir},/etc/httpd}

cp -af mywebftp/* $RPM_BUILD_ROOT%{_mywebftpdir}
rm -f $RPM_BUILD_ROOT%{_mywebftpdir}/config.php

install mywebftp/config.php $RPM_BUILD_ROOT%{_sysconfdir}
ln -sf %{_sysconfdir}/config.php $RPM_BUILD_ROOT%{_mywebftpdir}/config.php

install %{SOURCE1} $RPM_BUILD_ROOT/etc/httpd/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*%{name}.conf" /etc/httpd/httpd.conf; then
	echo "Include /etc/httpd/%{name}.conf" >> /etc/httpd/httpd.conf
elif [ -d /etc/httpd/httpd.conf ]; then
	ln -sf /etc/httpd/%{name}.conf /etc/httpd/httpd.conf/99_%{name}.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
	/usr/sbin/apachectl restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	umask 027
	if [ -d /etc/httpd/httpd.conf ]; then
		rm -f /etc/httpd/httpd.conf/99_%{name}.conf
	else
		grep -v "^Include.*%{name}.conf" /etc/httpd/httpd.conf > \
			/etc/httpd/httpd.conf.tmp
		mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
		if [ -f /var/lock/subsys/httpd ]; then
			/usr/sbin/apachectl restart 1>&2
		fi
	fi
fi

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%config(noreplace) %verify(not md5 mtime size) /etc/httpd/%{name}.conf
%dir %{_mywebftpdir}
%{_mywebftpdir}/images
%{_mywebftpdir}/lang
%{_mywebftpdir}/style
%{_mywebftpdir}/*.php
%{_mywebftpdir}/README.txt
