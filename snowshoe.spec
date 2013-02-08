%define git 20130208

Name: snowshoe
Version: 0.1
Release: 0.%git.1
# Created w/ "git archive" from
# ssh://USER@codereview.qt-project.org:29418/qt-apps/snowshoe.git
Source0: snowshoe-%version-%git.tar.gz
Group: Networking/WWW
Summary: Qt 5/WebKit 2 based web browser
License: GPLv2.1
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5WebKit)
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
Requires: %{_lib}qt5sql5-sqlite

%description
Qt 5/WebKit 2 based web browser

%prep
%setup -q -n %name
%_prefix/lib/qt5/bin/qmake snowshoe.pro

%build
%make STRIP=true

%install
%make install INSTALL_ROOT="%buildroot" STRIP=true

%files
%_bindir/*
%_datadir/applications/*
%_datadir/pixmaps/*
