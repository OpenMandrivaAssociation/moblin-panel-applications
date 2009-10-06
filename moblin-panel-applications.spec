Name: moblin-panel-applications
Summary: Applications panel for Moblin
Group: Graphical desktop/Other 
Version: 0.0.2
License: LGPL 2.1
URL: http://www.moblin.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: clutter-devel
BuildRequires: gtk2-devel
BuildRequires: gnome-menus-devel
BuildRequires: nbtk-devel
BuildRequires: mutter-moblin
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

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc COPYING NEWS AUTHORS README ChangeLog
%exclude %{_libdir}/debug
%{_libexecdir}/*
%{_datadir}/*
