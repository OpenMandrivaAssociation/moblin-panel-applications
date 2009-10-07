Name: moblin-panel-applications
Summary: Applications panel for Moblin
Group: Graphical desktop/Other 
Version: 0.0.2
License: LGPL 2.1
URL: http://www.moblin.org
Release: %mkrel 2
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: clutter-devel
BuildRequires: gtk2-devel
BuildRequires: gnome-menus-devel
BuildRequires: nbtk-devel
BuildRequires: moblin-panel-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common

%description
Moblin applications panel for Moblin

%prep
%setup -q 

%build
NOCONFIGURE=nil ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING NEWS AUTHORS README ChangeLog
%{_libexecdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/*service
