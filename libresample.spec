%define	major	0
%define libname	%mklibname resample %{major}
%define devname	%mklibname -d resample

Summary:	A real-time library for sampling rate conversion
Name:		libresample
Version:	0.1.3
Release:	13
License:	LGPLv2
Group:		System/Libraries
Url:		http://www-ccrma.stanford.edu/~jos/resample/Available_Software.html
Source0:	http://ccrma.stanford.edu/~jos/resample/%{name}-%{version}.tgz
Patch0:		libresample-shared.diff
BuildRequires:	libtool
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(samplerate)

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

%package -n	%{devname}
Summary:	Static library and header files for the libevent library
Group:		Development/C
Provides:	resample-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
This package contains the static libresample library and its header files.

%prep
%setup -q
%patch0 -p0

%build
export CC="%{__cc}"
export CFLAGS="%{optflags} -fPIC"

%configure2_5x
%make

%install
%makeinstall_std

%files tools
%{_bindir}/compareresample
%{_bindir}/resample-sndfile
%{_bindir}/testresample

%files -n %{libname}
%{_libdir}/libresample.so.%{major}*

%files -n %{devname}
%doc LICENSE.txt README.txt
%{_includedir}/*
%{_libdir}/*.so

