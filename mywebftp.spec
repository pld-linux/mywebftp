Summary:	Little PHP Tool to manage your webspace, through a web browser
Summary(pl):	Aplikacja w PHP do zarz±dzania przestrzeni± WWW poprzez przegl±darkê
Name:		mywebftp
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/mywebftp/%{name}%{version}.zip
# Source0-md5:	82e9ece26f7e3d3f9a8121908b8de90c
URL:		http://sourceforge.net/projects/mywebftp/
Requires:	php-pcre
Requires:	webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_mywebftpdir	/home/services/httpd/html/mywebftp

%description
MyWebFTP is a little PHP Tool that allows you to manage you files and
directories on your webspace, through a web browser. Usefull when you
are behind a restrictive proxy and more handy than an heavy software
FTP Client. Uses only PHP file functions..

%description -l pl
MyWebFTP to ma³e narzêdzie w PHP, które pozwala na zarz±dzanie poprzez
przegl±darkê, plikami i katalogami znajduj±cymi sie w okre¶lonej
przestrzni WWW. Program ten staje siê bardzo przydatny dla u¿ytkowników
znajduj±cych siê za restrykcyjnym proxy, gdy¿ u¿ywa tylko funkcji PHP.

%prep
%setup -q -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mywebftpdir}

cp -af mywebftp/* $RPM_BUILD_ROOT%{_mywebftpdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_mywebftpdir}
%{_mywebftpdir}/images/
%{_mywebftpdir}/lang/
%{_mywebftpdir}/style
%{_mywebftpdir}/*.php
%{_mywebftpdir}/README.txt
