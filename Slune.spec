Summary:	A 3D action car game
Summary(pl.UTF-8):	Samochodowa gra akcji 3D
Name:		Slune
Version:	1.0.14
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://download.gna.org/slune/%{name}-%{version}.tar.bz2
# Source0-md5:	d6ea52b12e92e35582e180e61e61cdc4
Source1:	%{name}.desktop
URL:		http://home.gna.org/oomadness/en/slune/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	libvorbis-devel
BuildRequires:	python-devel >= 2.2
Requires:	python-EditObj
Requires:	python-Py2Play
Requires:	python-Soya >= 0.14-0.rc1
Requires:	python-pyvorbis
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
A game where the player, as a Penguin named Tux, tries to help fit the
AIDS epidemic in Africa.

%description -l pl.UTF-8
Gra, w której gracz, jako pingwin Tux, próbuje powstrzymać epidemię
AIDS w Afryce.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

python setup.py install \
	--root=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install	images/slune.48.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

rm -f $RPM_BUILD_ROOT%{_datadir}/slune/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/slune
%{_desktopdir}/*.desktop
%{_pixmapsdir}/%{name}.png
