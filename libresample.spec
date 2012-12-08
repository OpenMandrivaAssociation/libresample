%define	major 0
%define libname %mklibname resample %{major}
%define develname %mklibname -d resample

Summary:	A real-time library for sampling rate conversion
Name:		libresample
Version:	0.1.3
Release:	%mkrel 11
License:	LGPL
Group:		System/Libraries
URL:		http://www-ccrma.stanford.edu/~jos/resample/Available_Software.html
Source0:	http://ccrma.stanford.edu/~jos/resample/%{name}-%{version}.tgz
Patch0:		libresample-shared.diff
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(samplerate)
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


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-10mdv2011.0
+ Revision: 661523
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-9mdv2011.0
+ Revision: 602603
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-8mdv2010.1
+ Revision: 520901
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1.3-7mdv2010.0
+ Revision: 425697
- rebuild

* Sat Dec 27 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-6mdv2009.1
+ Revision: 320062
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1.3-5mdv2009.0
+ Revision: 222973
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-4mdv2008.1
+ Revision: 178935
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 02 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-2mdv2008.0
+ Revision: 58162
- rename the subpackage containing binaries

* Thu Aug 02 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-1mdv2008.0
+ Revision: 58111
- fix one missing build deps
- try another trick to make it build
- de-activating parts of this package to make it pass the friggin bs
- fix build (#1)
- Import libresample



* Wed Aug 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-1mdv2008.0
- initial mandriva package
