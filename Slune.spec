Summary:	A 3D action car game
Summary(pl):	Samochodowa gra akcji 3D
Name:		Slune
Version:	0.7
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.gna.org/slune/%{name}-%{version}.tar.bz2
# Source0-md5:	f5c47d42de7bd16cac1cab21928e0231
Source1:	%{name}.desktop
URL:		http://home.gna.org/oomadness/en/slune/index.html
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	libvorbis-devel
Requires:	Soya
Requires:	python-EditObj
Requires:	python-Py2Play
Requires:	python-PyOpenAL
Requires:	python-pyvorbis
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
A game where the player, as a Penguin named Tux, try to help fit the
AIDS epidemic in Africa.

%description -l pl
Gra, w której gracz, jako pingwin Tux, próbuje powstrzymaæ epidemiê
AIDS w Afryce.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

rm -f $RPM_BUILD_ROOT%{_datadir}/slune/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/slune
%{_desktopdir}/*.desktop
