Summary:	Breakout/Arkanoid style arcade game
Summary(pl.UTF-8):	Gra w stylu Breakouta/Arkanoida
Name:		lbreakouthd
Version:	1.1.8
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://downloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	d0af6085ca948059cb46145285c57b18
Patch0:		%{name}-format.patch
Patch1:		%{name}-desktop.patch
URL:		https://lgames.sourceforge.net/LBreakout2
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	SDL2_image-devel >= 2.0
BuildRequires:	SDL2_mixer-devel >= 2.0
BuildRequires:	SDL2_ttf-devel >= 2.0
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/games

%description
LBreakout is a breakout game with nice graphics, effects and sound.
You can play it either with mouse or keyboard and you can create your
own levels.

%description -l pl.UTF-8
LBreakout to gra breakout z przyjemną grafiką, efektami i dźwiękiem.
Można grać myszą lub klawiaturą oraz tworzyć własne poziomy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e 's,\$(datadir)/icons,$(datadir)/pixmaps,' Makefile.am

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changelog README TODO
%attr(2755,root,games) %{_bindir}/lbreakouthd
%{_datadir}/lbreakouthd
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/lbreakouthd.hscr
%{_desktopdir}/lbreakouthd.desktop
%{_pixmapsdir}/lbreakouthd.png
