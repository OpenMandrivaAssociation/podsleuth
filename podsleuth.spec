%define name podsleuth
%define version 0.6.7
%define release %mkrel 5

Summary: Extract metadata from Apple iPods
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.banshee-project.org/%name/%version/%{name}-%{version}.tar.bz2
License: BSD
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://banshee-project.org/PodSleuth
BuildRequires: mono-devel
BuildRequires: hal-devel
BuildRequires: ndesk-dbus-devel
BuildRequires: libsgutils-devel
Requires: hal

%description
PodSleuth is a tool to discover detailed model information about an
Apple (TM) iPod (TM). Its primary role is to be run as a callout by
HAL (http://freedesktop.org/wiki/Software_2fhal) because root access
is needed to scan the device for required information. When the model
information is discovered, it is merged into HAL as properties for
other applications to use.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
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
mkdir -p %buildroot/var/cache/podsleuth
mkdir -p %buildroot%_libdir/hal/scripts
mv %buildroot%_libdir/hal/hal-podsleuth %buildroot%_libdir/hal/scripts

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS
%config(noreplace) %_sysconfdir/dbus-1/system.d/podsleuth.conf
%_bindir/podsleuth
%_libdir/hal/scripts/hal-podsleuth
#gw this must be in /usr/lib as referenced by the hal script
%_prefix/lib/podsleuth
%_datadir/hal/fdi/policy/20thirdparty/20-podsleuth.fdi
%dir /var/cache/podsleuth

%files devel
%_libdir/pkgconfig/podsleuth.pc


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.7-3mdv2011.0
+ Revision: 667796
- mass rebuild

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 0.6.7-2mdv2011.0
+ Revision: 567918
- split out devel package
- update devel deps

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.6.7-1mdv2011.0
+ Revision: 550290
- update to new version 0.6.7

* Wed Jan 27 2010 Götz Waschk <waschk@mandriva.org> 0.6.6-1mdv2010.1
+ Revision: 497464
- new version
- update file list

* Thu Oct 15 2009 Götz Waschk <waschk@mandriva.org> 0.6.5-1mdv2010.0
+ Revision: 457510
- new version
- drop patch

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.6.4-3mdv2010.0
+ Revision: 426736
- rebuild

* Thu Apr 23 2009 Götz Waschk <waschk@mandriva.org> 0.6.4-2mdv2009.1
+ Revision: 368800
- fix directory on x86_64 (bug #50229)

* Wed Jan 21 2009 Götz Waschk <waschk@mandriva.org> 0.6.4-1mdv2009.1
+ Revision: 332156
- update to new version 0.6.4

* Tue Oct 21 2008 Götz Waschk <waschk@mandriva.org> 0.6.3-1mdv2009.1
+ Revision: 296087
- new version
- make it build with new libsgutils

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Mon Jun 09 2008 Götz Waschk <waschk@mandriva.org> 0.6.2-1mdv2009.0
+ Revision: 217019
- new version

* Thu Feb 21 2008 Götz Waschk <waschk@mandriva.org> 0.6.1-2mdv2008.1
+ Revision: 173500
- move hal callout to the right directory

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Fri Dec 21 2007 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdv2008.1
+ Revision: 136181
- import podsleuth


* Fri Dec 21 2007 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdv2008.1
- initial package

