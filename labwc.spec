%global forgeurl https://github.com/%{name}/%{name}
 
Name:       labwc
Version:    0.6.6
Release:    1
Summary:    Openbox alternative for Wayland
License:    GPL-2.0-only
URL:        https://github.com/labwc/labwc
Source0:    https://github.com/labwc/labwc/archive/%{version}/%{name}-%{version}.tar.gz
 
BuildRequires: meson
 
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libinput) >= 1.14
BuildRequires: pkgconfig(librsvg-2.0) >= 2.46
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(scdoc)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wlroots)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xkbcommon)
 
Requires:   xwayland
 
# Upstream recommendations
# https://github.com/labwc/labwc#6-integration
Recommends: bemenu                      %dnl # Launchers
Recommends: swaylock                    %dnl # Screen locker
Suggests:   fuzzel wofi                 %dnl # Launchers
Suggests:   grim                        %dnl # Screen-shooter
Suggests:   kanshi wlr-randr            %dnl # Output managers
Suggests:   swaybg                      %dnl # Background image
Suggests:   lavalauncher waybar yambar  %dnl # Panel
 
# Downstream usefull stuff which already packaged in Fedora
Suggests:   wdisplays                   %dnl # GUI display configurator for wlroots compositors
  
 
%description
Labwc stands for Lab Wayland Compositor, where lab can mean any of the
following:
 
  * sense of experimentation and treading new ground
  * inspired by BunsenLabs and ArchLabs
  * your favorite pet
 
Labwc is a wlroots-based window-stacking compositor for wayland, inspired by
openbox.
 
It is light-weight and independent with a focus on simply stacking windows
well and rendering some window decorations. It takes a no-bling/frills
approach and says no to features such as icons (except window buttons),
animations, decorative gradients and any other options not required to
reasonably render common themes. It relies on clients for panels, screenshots,
wallpapers and so on to create a full desktop environment.
 
Labwc tries to stay in keeping with wlroots and sway in terms of general
approach and coding style.
 
Labwc has no reliance on any particular Desktop Environment, Desktop Shell or
session. Nor does it depend on any UI toolkits such as Qt or GTK.
 
 
%prep
%autosetup -p1
 
%build
%meson \
    -Dxwayland=enabled
%meson_build
 
%install
%meson_install
%find_lang %{name}
 
%files -f %{name}.lang
%license LICENSE
%doc NEWS.md
%{_bindir}/%{name}
%{_datadir}/wayland-sessions/%{name}.desktop
%{_docdir}/%{name}/*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
