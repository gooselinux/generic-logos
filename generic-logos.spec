Name:       generic-logos
Version:    13.0.1
Release:    3%{?dist}
Summary:    Icons and pictures

Group:      System Environment/Base
URL:        https://fedorahosted.org/generic-logos/ 
Source0:    https://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2
#The KDE Logo is under a LGPL license (no version statement)
License:    GPLv2 and LGPLv2+
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

Obsoletes:  redhat-logos
Provides:   redhat-logos = %{version}-%{release}
Provides:   system-logos = %{version}-%{release}

Conflicts:  fedora-logos
Conflicts:  anaconda-images <= 10
Conflicts:  redhat-artwork <= 5.0.5
# For _kde4_* macros:
BuildRequires: kde-filesystem


%description
The generic-logos package contains various image files which can be
used by the bootloader, anaconda, and other related tools. It can
be used as a replacement for the fedora-logos package, if you are
unable for any reason to abide by the trademark restrictions on the
fedora-logos package.

%prep
%setup -q

%build
#nothing to build

%install
rm -rf %{buildroot}

# should be ifarch i386
mkdir -p %{buildroot}/boot/grub
install -p -m 644 bootloader/splash.xpm.gz %{buildroot}/boot/grub/splash.xpm.gz
# end i386 bits

mkdir -p %{buildroot}%{_datadir}/firstboot/themes/generic
for i in firstboot/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/firstboot/themes/generic
done

mkdir -p %{buildroot}%{_datadir}/pixmaps/splash
for i in gnome-splash/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/pixmaps/splash
done

mkdir -p %{buildroot}%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/pixmaps
done

mkdir -p %{buildroot}%{_kde4_iconsdir}/Fedora-KDE/48x48/apps/
install -p -m 644 icons/Fedora/48x48/apps/* %{buildroot}%{_kde4_iconsdir}/Fedora-KDE/48x48/apps/
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536
install -p -m 644 ksplash/SolarComet-kde.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536/logo.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge/
for i in plymouth/charge/* ; do
    install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge/
done

# File or directory names do not count as trademark infringement
mkdir -p %{buildroot}%{_datadir}/icons/Fedora/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/icons/Fedora/scalable/apps/
install -p -m 644 icons/Fedora/48x48/apps/* %{buildroot}%{_datadir}/icons/Fedora/48x48/apps/
install	-p -m 644 icons/Fedora/scalable/apps/* %{buildroot}%{_datadir}/icons/Fedora/scalable/apps/

(cd anaconda; make DESTDIR=%{buildroot} install)

%post
touch --no-create %{_datadir}/icons/Fedora || :
touch --no-create %{_kde4_iconsdir}/Fedora-KDE ||:

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/Fedora || :
touch --no-create %{_kde4_iconsdir}/Fedora-KDE ||:
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  if [ -f %{_datadir}/icons/Fedora/index.theme ]; then
    gtk-update-icon-cache --quiet %{_datadir}/icons/Fedora || :
  fi
  if [ -f %{_kde4_iconsdir}/Fedora-KDE/index.theme ]; then
    gtk-update-icon-cache --quiet %{_kde4_iconsdir}/Fedora-KDE/index.theme || :
  fi
fi
fi

%posttrans
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  if [ -f %{_datadir}/icons/Fedora/index.theme ]; then
    gtk-update-icon-cache --quiet %{_datadir}/icons/Fedora || :
  fi
  if [ -f %{_kde4_iconsdir}/Fedora-KDE/index.theme ]; then
    gtk-update-icon-cache --quiet %{_kde4_iconsdir}/Fedora-KDE/index.theme || :
  fi
fi


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING COPYING-kde-logo README
%{_datadir}/firstboot/themes/*
%{_datadir}/anaconda/pixmaps/*
%{_datadir}/icons/Fedora/*/apps/*
%{_datadir}/pixmaps/*
%{_datadir}/plymouth/themes/charge/*
/usr/lib/anaconda-runtime/*.jpg
%{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536/logo.png
%{_kde4_iconsdir}/Fedora-KDE/
# should be ifarch i386
/boot/grub/splash.xpm.gz
# end i386 bits

%changelog
* Sat Jul 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 13.0.2-3
- fix %%postun scriptlet error

* Fri Jun 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 13.0.2-2
- Fedora-KDE icons are now fedora-kde-icons-theme, not kde-settings
- include icon scriplets
- drop ancient Conflicts: kdebase ...

* Tue May  4 2010 Bill Nottingham <notting@redhat.com> - 13.0.1-1
- Add logos to make firstboot work

* Mon May  3 2010 Bill Nottingham <notting@redhat.com> - 13.0-1
- Update for Fedora 13

* Sat Dec 26 2009 Fabian Affolter <fabian@bernewireless.net> - 12.2-3
- Changed SourceO to upstream link
- Added URL and README
- Added version to LGPL of the KDE logo
- Minor cosmetic layout changes

* Wed Nov  4 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 12.2-2
- kde icon installation

* Fri Oct 30 2009 Bill Nottingham <notting@redhat.com> - 12.2-1
- tweak anaconda.png/svg to match rest of icons (<duffy@redhat.com>)

* Fri Oct 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 12.1-1
- 12.1 (add generic versions of anaconda.png/svg)

* Thu Oct  1 2009 Bill Nottingham <notting@redhat.com> - 12.0-1
- update for F12 (<duffy@redhat.com>)

* Tue May 12 2009 Bill Nottingham <notting@redhat.com> - 11.0.1-1
- Add new plymouth artwork (#500239)

* Wed Apr 22 2009 Bill Nottingham <notting@redhat.com> - 11.0.0-1
- updates for Fedora 11

* Wed Dec  3 2008 Bill Nottingham <notting@redhat.com> - 10.0.2-1
- fix syslinux splash (accidentally branded)

* Tue Oct 28 2008 Bill Nottingham <notting@redhat.com> - 10.0.1-1
- incorporate KDE logo into upstream source distribution
- fix system-logo-white.png for compiz bleeding (#468258)

* Mon Oct 27 2008 Jaroslav Reznik <jreznik@redhat.com> - 10.0.0-3
- Solar Comet generic splash logo redesign

* Sun Oct 26 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 10.0.0-2
- Add (current version of) KDE logo for SolarComet KSplash theme

* Thu Oct 23 2008 Bill Nottingham <notting@redhat.com> - 10.0.0-1
- update for current fedora-logos, with Solar theme

* Fri Jul 11 2008 Bill Nottingham <notting@redhat.com> - 9.99.0-1
- add a system logo for plymouth's spinfinity plugin

* Tue Apr 15 2008 Bill Nottingham <notting@redhat.com> - 9.0.0-1
- updates for current fedora-logos (much thanks to <duffy@redhat.com>)
- remove KDE Infinity splash
 
* Mon Oct 29 2007 Bill Nottingham <notting@redhat.com> - 8.0.2-1
- Add Infinity splash screen for KDE

* Thu Sep 13 2007 Bill Nottingham <notting@redhat.com> - 7.92.1-1
- add powered-by logo (#250676)
- updated rhgb logo (<duffy@redhat.com>)

* Tue Sep 11 2007 Bill Nottinghan <notting@redhat.com> - 7.92.0-1
- initial packaging. Forked from fedora-logos, adapted from the Fedora
  Art project's Infinity theme
