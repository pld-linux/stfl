Summary:	STFL implements a curses-based widget set for text terminals
Summary(hu.UTF-8):	Az STFL egy curses-alapú widget-készletet biztosít szöveges terminálokhoz
Summary(pl.UTF-8):	Implementacja opartego na ncurses zestawu widgetów dla terminali tekstowych
Name:		stfl
Version:	0.24
Release:	10
License:	LGPL v3
Group:		Libraries
Source0:	http://www.clifford.at/stfl/%{name}-%{version}.tar.gz
# Source0-md5:	98c764ccc8f13ed05ea22559d7116b96
Patch0:		%{name}-example-dir.patch
Patch1:		%{name}-link.patch
Patch2:		python-install.patch
Patch3:		python-bin.patch
URL:		http://www.clifford.at/stfl/
BuildRequires:	ncurses-devel >= 5
BuildRequires:	perl-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	ruby-devel
BuildRequires:	swig-perl
BuildRequires:	swig-python
BuildRequires:	swig-ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
STFL is a library which implements a curses-based widget set for text
terminals.

%description -l hu.UTF-8
Az STFL egy curses-alapú widget-készletet biztosít szöveges
terminálokhoz.

%description -l pl.UTF-8
STFL jest biblioteką udostępniającą implementacją opartego na ncurses
zestawu widgetów dla terminali tekstowych.

%package devel
Summary:	Header files for STFL library
Summary(hu.UTF-8):	Az STFL könyvtár fejlesztői fájljai
Summary(pl.UTF-8):	Pliki nagłówekowe biblioteki STFL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for STFL library.

%description devel -l hu.UTF-8
Az STFL könyvtár fejlesztői fájljai.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki STFL.

%package static
Summary:	Static STFL library
Summary(hu.UTF-8):	Statikus STFL könyvtár
Summary(pl.UTF-8):	Statyczna biblioteka STFL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static STFL library.

%description static -l hu.UTF-8
Statikus STFL könyvtár.

%description static -l pl.UTF-8
Statyczna biblioteka STFL.

%package -n perl-%{name}
Summary:	Perl binding for STFL
Summary(hu.UTF-8):	Perl kapcsolódás STFL-hez
Summary(pl.UTF-8):	Wiązania Perla dla STFL-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	stfl-perl

%description -n perl-%{name}
Perl binding for STFL.

%description -n perl-%{name} -l hu.UTF-8
Perl kapcsolódás STFL-hez.

%description -n perl-%{name} -l pl.UTF-8
Wiązania Perla dla STFL-a.

%package -n python-%{name}
Summary:	Python binding for STFL
Summary(hu.UTF-8):	Python kapcsolódás STFL-hez
Summary(pl.UTF-8):	Wiązania Pythona dla STFL-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	stfl-python

%description -n python-%{name}
Python binding for STFL.

%description -n python-%{name} -l hu.UTF-8
Python kapcsolódás STFL-hez.

%description -n python-%{name} -l pl.UTF-8
Wiązania Pythona dla STFL-a.

%package -n ruby-%{name}
Summary:	Ruby binding for STFL
Summary(hu.UTF-8):	Ruby kapcsolódás STFL-hez
Summary(pl.UTF-8):	Wiązania Ruby'ego dla STFL-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	stfl-ruby

%description -n ruby-%{name}
Ruby binding for STFL.

%description -n ruby-%{name} -l hu.UTF-8
Ruby kapcsolódás STFL-hez.

%description -n ruby-%{name} -l pl.UTF-8
Wiązania Ruby'ego dla STFL-a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
echo 'LDLIBS=-ltinfow' >> Makefile.cfg

%build
%{__make} -j1 \
	prefix="" \
	libdir=%{_libdir} \
	CFLAGS="-Wall %{rpmcppflags} %{rpmcflags} -I. -D_GNU_SOURCE -fPIC" \
	LDFLAGS="%{rpmldflags}" \
	CC="%{__cc} -pthread" \
	PYTHON="%{__python}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_libdir}/lib-dynload

%{__make} -j1 install \
	prefix=%{_prefix} \
	libdir=%{_lib} \
	RUBYARCHDIR=$RPM_BUILD_ROOT%{ruby_vendorarchdir} \
	DESTDIR=$RPM_BUILD_ROOT \
	PYTHON="%{__python}"

/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}

%{__mv} $RPM_BUILD_ROOT%{py_sitedir}/lib-dynload/_stfl.so \
	$RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install example{,.c,.stfl} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libstfl.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libstfl.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstfl.so
%{_includedir}/stfl.h
%{_pkgconfigdir}/stfl.pc
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/example
%{_examplesdir}/%{name}-%{version}/example.*

%files static
%defattr(644,root,root,755)
%{_libdir}/libstfl.a

%files -n perl-%{name}
%defattr(644,root,root,755)
%doc perl5/example.pl
%{perl_vendorarch}/stfl.pm
%dir %{perl_vendorarch}/auto/stfl
%attr(755,root,root) %{perl_vendorarch}/auto/stfl/stfl.so

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_stfl.so
%{py_sitedir}/stfl.py[co]

%files -n ruby-%{name}
%defattr(644,root,root,755)
%doc ruby/example.rb
%attr(755,root,root) %{ruby_vendorarchdir}/stfl.so
