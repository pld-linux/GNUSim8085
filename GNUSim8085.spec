Summary:	Graphical simulator for the Intel 8085 microprocessor
Summary(pl):	Graficzny symulator mikroprocesora Intel 8085
Name:		GNUSim8085
Version:	1.2.89
Release:	4
License:	GPL
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/gnusim8085/%{name}-%{version}.tar.bz2
# Source0-md5:	fe51e74cc1698e8a0548d3865fb7afee
Source1:	%{name}.desktop
Patch0:		%{name}-link.patch
URL:		http://sourceforge.net/projects/gnusim8085/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUSim8085 is a graphical simulator plus assembler with debugger for
the Intel 8085 microprocessor.

%description -l pl
GNUSim8085 jest graficznym symulatorem wraz z asemblerem i debugerem
dla mikroprocesora Intel 8085.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}/* \
	$RPM_BUILD_ROOT%{_pixmapsdir}

cp -rf doc/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_examplesdir}/%{name}
%{_pixmapsdir}/*.png
