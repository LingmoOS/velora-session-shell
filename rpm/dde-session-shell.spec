Name:           dde-session-shell
Version:        1.0.0
Release:        1%{?dist}
Summary:        DDE Session Shell for Lingmo OS
License:        GPL-3.0-or-later
URL:            https://github.com/LingmoOS/dde-session-shell
Source0:        dde-session-shell-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(dtk6core)
BuildRequires:  pkgconfig(dtk6gui)
BuildRequires:  pkgconfig(dtk6widget)

%description
DDE Session Shell provides the session management UI for
the Lingmo desktop environment, including lock screen and login.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE*
%{_bindir}/dde-session-shell
%{_libexecdir}/dde-session-shell/
%{_libdir}/dde-session-shell/
%{_datadir}/dde-session-shell/
%{_datadir}/dbus-1/services/*.service

%changelog
* Tue Jun 18 2025 LingmoOS Build System <dev@lingmo.os> - %{version}-1
- Initial RPM packaging for local source build
