%define	major 0
%define libname %mklibname resample %{major}
%define develname %mklibname -d resample

Summary:	A real-time library for sampling rate conversion
Name:		libresample
Version:	0.1.3
Release:	%mkrel 10
License:	LGPL
Group:		System/Libraries
URL:		http://www-ccrma.stanford.edu/~jos/resample/Available_Software.html
Source0:	http://ccrma.stanford.edu/~jos/resample/%{name}-%{version}.tgz
Patch0:		libresample-shared.diff
BuildRequires:	libsndfile-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
libresample is a real-time library for sampling rate conversion.

%package	tools
Summary:	Various tools using the libresample library
Group:          Sound

%description	tools
libresample is a real-time library for sampling rate conversion.

This package contains various tools that uses the libresample library.

 * compareresample
 * resample-sndfile
 * testresample

%package -n	%{libname}
Summary:	A real-time library for sampling rate conversion
Group:          System/Libraries

%description -n	%{libname}
libresample is a real-time library for sampling rate conversion.

%package -n	%{develname}
Summary:	Static library and header files for the libevent library
Group:		Development/C
Provides:	resample-devel = %{version}-%{release}
Provides:	libresample-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n	%{develname}
libresample is a real-time library for sampling rate conversion.

This package contains the static libresample library and its header files.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0

%build
export CC="%{__cc}"
export CFLAGS="%{optflags} -fPIC"

%configure
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files tools
%defattr(-,root,root)
%{_bindir}/compareresample
%{_bindir}/resample-sndfile
%{_bindir}/testresample

%files -n %{libname}
%defattr(-,root,root)
%doc LICENSE.txt README.txt
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
