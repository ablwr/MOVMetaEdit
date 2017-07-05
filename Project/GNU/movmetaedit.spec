# Copyright (c) 2010 info@mediaarea.net
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

# norootforbuild

%define movmetaedit_version		0.1

Name:			movmetaedit
Version:		%movmetaedit_version
Release:		1
Summary:		(To be filled) (CLI)
Group:			Productivity/Multimedia/Other
License:		GPL
URL:			http://mediainfo.sourceforge.net/
Packager:		Jerome Martinez <info@mediaarea.net>
Source0:		movmetaedit_%{version}-1.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  libzen-devel
BuildRequires: 	gcc-c++
BuildRequires:	pkgconfig
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif
BuildRequires:  automake
BuildRequires:  autoconf
%if 0%{?mageia}
BuildRequires:  sane-backends-iscan
BuildRequires:  libuuid-devel
%endif

%description
movmetaedit CLI (Command Line Interface)

MOV MetaEdit provides this service:

(To be filled)

%package gui
Summary:	(To be filled) (GUI)
Group:		Productivity/Multimedia/Other

%if 0%{?fedora_version} >= 23
BuildRequires:	qt-devel
%else
BuildRequires:	libqt4-devel
%endif

%if 0%{?fedora_version} == 99
BuildRequires: gnu-free-sans-fonts
%endif

%if 0%{?suse_version} ||  0%{?opensuse_version}
Requires:	libqt4 >= 4.0.0
Requires:	libqt4-x11 >= 4.0.0
%endif

%description gui
movmetaedit GUI (Graphical User Interface)

MOV MetaEdit provides this service:

(To be filled)

This package contains the graphical user interface

%prep
%setup -q -n movmetaedit

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"

# build CLI
pushd Project/GNU/CLI
	%__chmod +x autogen
	./autogen
	%if 0%{?mageia} > 5
		%configure --disable-dependency-tracking
	%else
		%configure
	 %endif

	%__make %{?jobs:-j%{jobs}}
popd

# now build GUI
pushd Project/Qt
	qmake
	%__make %{?jobs:-j%{jobs}}
popd

%install
pushd Project/GNU/CLI
	%__make install DESTDIR=%{buildroot}
popd

pushd Project/Qt
	%__install -m 755 movmetaedit-gui %{buildroot}%{_bindir}/movmetaedit-gui
popd

# icon
#%__install -dm 755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
#%__install -m 644 Source/Resource/Image/FADGI/Logo128.png \
#	%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
#%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
#%__install -m 644 Source/Resource/Image/FADGI/Logo.png \
#	%{buildroot}%{_datadir}/pixmaps/%{name}.png

# menu-entry
#%__install -dm 755 %{buildroot}/%{_datadir}/applications
#%__install -m 644 Project/GNU/GUI/movmetaedit-gui.desktop \
#	%{buildroot}/%{_datadir}/applications
#%if 0%{?suse_version}
#  %suse_update_desktop_file -n movmetaedit-gui AudioVideo AudioVideoEditing
#%endif
#%__install -dm 755 %{buildroot}/%{_datadir}/apps/konqueror/servicemenus
#%__install -m 644 Project/GNU/GUI/movmetaedit-gui.kde3.desktop \
#	%{buildroot}/%{_datadir}/apps/konqueror/servicemenus/movmetaedit-gui.desktop
#%if 0%{?suse_version}
#  %suse_update_desktop_file -n %{buildroot}/%{_datadir}/apps/konqueror/servicemenus/movmetaedit-gui.desktop AudioVideo AudioVideoEditing
#%endif
#%__install -dm 755 %{buildroot}/%{_datadir}/kde4/services/ServiceMenus/
#%__install -m 644 Project/GNU/GUI/movmetaedit-gui.kde4.desktop \
#	%{buildroot}/%{_datadir}/kde4/services/ServiceMenus/movmetaedit-gui.desktop
#%if 0%{?suse_version}
#  %suse_update_desktop_file -n %{buildroot}/%{_datadir}/kde4/services/ServiceMenus/movmetaedit-gui.desktop AudioVideo AudioVideoEditing
#%endif

%clean
[ -d "%{buildroot}" -a "%{buildroot}" != "" ] && %__rm -rf "%{buildroot}"

%files
%defattr(-,root,root,-)
%doc License.html
%{_bindir}/movmetaedit

%files gui
%defattr(-,root,root,-)t
%doc License.html
%{_bindir}/movmetaedit-gui
#%{_datadir}/applications/*.desktop
#%{_datadir}/pixmaps/*.png
#%dir %{_datadir}/icons/hicolor
#%dir %{_datadir}/icons/hicolor/128x128
#%dir %{_datadir}/icons/hicolor/128x128/apps
#%{_datadir}/icons/hicolor/128x128/apps/*.png
#%dir %{_datadir}/apps
#%dir %{_datadir}/apps/konqueror
#%dir %{_datadir}/apps/konqueror/servicemenus
#%{_datadir}/apps/konqueror/servicemenus/*.desktop
#%dir %{_datadir}/kde4
#%dir %{_datadir}/kde4/services
#%dir %{_datadir}/kde4/services/ServiceMenus
#%{_datadir}/kde4/services/ServiceMenus/*.desktop

%changelog
* Sun Jan 01 2017 Jerome Martinez <info@mediaarea.net> - 0.1-0
- See History.txt for more info and real dates