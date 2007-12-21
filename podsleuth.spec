%define name podsleuth
%define version 0.6.1
%define release %mkrel 1

Summary: Extract metadata from Apple iPods
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://banshee-project.org/files/%name/%{name}-%{version}.tar.bz2
License: BSD
Group: System/Libraries
Url: http://banshee-project.org/PodSleuth
BuildRequires: mono-devel
BuildRequires: hal-devel
BuildRequires: ndesk-dbus
BuildRequires: libsgutils-devel
Requires: hal

%description
PodSleuth is a tool to discover detailed model information about an
Apple (TM) iPod (TM). Its primary role is to be run as a callout by
HAL (http://freedesktop.org/wiki/Software_2fhal) because root access
is needed to scan the device for required information. When the model
information is discovered, it is merged into HAL as properties for
other applications to use.

%prep
%setup -q

%build
%configure2_5x
make

%install
rm -rf %{buildroot}
%makeinstall_std
%if %_lib != lib
mv %buildroot%_prefix/lib/podsleuth %buildroot%_libdir/
%endif
mkdir -p %buildroot/var/cache/podsleuth

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS
%_bindir/podsleuth
%_libdir/hal/hal-podsleuth
%_libdir/pkgconfig/podsleuth.pc
%_libdir/podsleuth
%_datadir/hal/fdi/policy/20thirdparty/20-podsleuth.fdi
%dir /var/cache/podsleuth

