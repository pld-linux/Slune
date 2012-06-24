%define _rc     rc1
Summary:	A 3D action car game
Summary(pl):	Samochodowa gra akcji 3D
Name:		Slune
Version:	1.0.12
Release:	0.%{_rc}.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.gna.org/slune/%{name}-%{version}%{_rc}.tar.bz2
# Source0-md5:	ba523c653e0be5f07400061694006718
Source1:	%{name}.desktop
Patch0:		%{name}-slune_bin.patch
URL:		http://home.gna.org/oomadness/en/slune/index.html
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	libvorbis-devel
Requires:	python-EditObj
Requires:	python-Py2Play
Requires:	python-PyOpenAL
Requires:	python-Soya >= 0.9
Requires:	python-pyvorbis
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
A game where the player, as a Penguin named Tux, tries to help fit the
AIDS epidemic in Africa.

%description -l pl
Gra, w kt�rej gracz, jako pingwin Tux, pr�buje powstrzyma� epidemi�
AIDS w Afryce.

%prep
%setup -q -n %{name}-%{version}%{_rc}
%patch0 -p1

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
%doc AUTHORS CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/slune
%{_desktopdir}/*.desktop
%{_pixmapsdir}/%{name}.png
