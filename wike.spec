%undefine _debugsource_packages
%global appid com.github.hugolabe.Wike
%define oname Wike

Name:		wike
Version:	3.2.0	
Release:	1
URL:		https://github.com/hugolabe/Wike
Source0:	https://github.com/hugolabe/Wike/archive/%{version}/%{oname}-%{version}.tar.gz
Summary:	Wikipedia reader for the GNOME desktop	
License:	GPLv3+
Group:		Applications/Internet
 
BuildRequires:	appstream
BuildRequires:  pkgconfig(gtk4)
BuildRequires: 	libadwaita-common
BuildRequires: 	pkgconfig(libadwaita-1)  
BuildRequires:  gettext
BuildRequires:	desktop-file-utils
BuildSystem:	meson

Requires: typelib(WebKit)
Requires: webkit

%description
Wike is a Wikipedia reader for the GNOME Desktop. 
Provides access to all the content of this online encyclopedia 
in a native application, with a simpler and 
distraction-free view of articles.

%install
%meson_install
%find_lang %{name}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop

%files -f %{name}.lang
%{_bindir}/wike
%{_datadir}/wike/
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/com.github.hugolabe.*
%{_datadir}/gnome-shell/search-providers/com.github.hugolabe.Wike.SearchProvider.ini
%{_datadir}/metainfo/*.xml
%{_datadir}/dbus-1/services/*.service
