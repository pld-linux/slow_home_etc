Summary:	HOME-ETC support for PLD Linux (version slow)
Summary(pl):	Wsparcie mechanizmu HOME-ETC dla PLD Linux (wersja powolna)
Name:		slow_home_etc
Version:	0.0.1
Release:	1
License:	GPL
Group:		Base
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibc-devel
BuildRequires:	libtool
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	7cd764d8e090308ad4a127542384fb0d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HOME-ETC is an idea to keep configuration files in a subdirectory
specified by user, instead of its home directory. This package
provides support for it.

%description -l pl
HOME-ETC jest pomys³em, aby przechowywaæ pliki konfiguracyjne
w podkatalogu wskazanym przez u¿ytkownika, zamiast bezpo¶rednio
w jego katalogu domowym. Pakiet ten zapewnia wsparcie dla tego
mechanizmu.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS PRZECZYTAJ_TO
%attr(755,root,root) %{_libdir}/lib*.so*
%attr(755,root,root) %{_libdir}/lib*.la
