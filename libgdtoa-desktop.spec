%global     gituser     10110111
%global     gitname     gdtoa-desktop
# 0.1.20180730 release
%global     gitdate     20201221
%global     commit      698924a1637897a1a78377e082bb0066696a6b34
%global     shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       libgdtoa-desktop
Version:    0.1.20180730^%{gitdate}g%{shortcommit}
Release:    1%{?dist}
Summary:    Binary-decimal floating-point conversion library
License:    MIT
URL:        https://github.com/10110111/gdtoa-desktop

%global     common_desc %{expand:
gdtoa-desktop is an adaptation of the binary<->decimal floating-point conversion library by
David M. Gay to common desktop/server operating systems like Ubuntu and Fedora.
This adaptation's main objective is to provide an easy way to build the original upstream library
in the configuration well-suited for the target systems -- with locale and multithreading support,
and without conflicts with the system libraries like glibc.}

Source0:    https://github.com/%{gituser}/%{gitname}/archive/%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  cmake

%description
%{common_desc}

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{common_desc}
The %{name}-devel package contains libraries and header files for developing applications that use %{name}.

%prep
%autosetup -n %{gitname}-%{commit} -p1

%build
%cmake .
make -C %{__cmake_builddir} %{?_smp_mflags}

%install
DESTDIR=%{buildroot} PREFIX="%{_prefix}" LIBDIRARCH=%{_lib} \
make -C %{__cmake_builddir} install

%files
%{_libdir}/libgdtoa-desktop.so

%files devel
%{_includedir}/gdtoa-desktop/*
%{_libdir}/pkgconfig/*

%changelog
* Mon Mar 25 2024 Pekka Oinas <peoinas@protonmail.com> - 0.1.20180730^20201221g698924a
- Initial build
