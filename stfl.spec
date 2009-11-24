Summary:	STFL implements a curses-based widget set for text terminals
Summary(hu.UTF-8):	Az STFL egy curses-alapú widget-készletet biztosít szöveges terminálokhoz
Summary(pl.UTF-8):	Implementacja opartego na ncurses zestawu widgetów dla terminali tekstowych
Name:		stfl
Version:	0.21
Release:	2
License:	LGPL v3
Group:		Libraries
Source0:	http://www.clifford.at/stfl/%{name}-%{version}.tar.gz
# Source0-md5:	888502c3f332a0ee66e490690d79d404
URL:		http://www.clifford.at/stfl/
Patch0:		%{name}-example-dir.patch
Patch1:		%{name}-link.patch
BuildRequires:	ncurses-devel
BuildRequires:	perl-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
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

%package perl
Summary:	Perl binding for STFL
Summary(hu.UTF-8):	Perl kapcsolódás STFL-hez
Summary(pl.UTF-8):	Wiązania Perla dla STFLa
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
Perl binding for STFL.

%description perl -l hu.UTF-8
Perl kapcsolódás STFL-hez.

%description perl -l pl.UTF-8
Wiązania Perla dla STFLa.

%package python
Summary:	Python binding for STFL
Summary(hu.UTF-8):	Python kapcsolódás STFL-hez
Summary(pl.UTF-8):	Wiązania Pythona dla STFLa
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description python
Python binding for STFL.

%description python -l hu.UTF-8
Python kapcsolódás STFL-hez.

%description python -l pl.UTF-8
Wiązania Pythona dla STFLa.

%package ruby
Summary:	Ruby binding for STFL
Summary(hu.UTF-8):	Ruby kapcsolódás STFL-hez
Summary(pl.UTF-8):	Wiązania Ruby'ego dla STFLa
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ruby
Ruby binding for STFL.

%description ruby -l hu.UTF-8
Ruby kapcsolódás STFL-hez.

%description ruby -l pl.UTF-8
Wiązania Ruby'ego dla STFLa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} -j1 \
	prefix=%{_prefix} \
	CFLAGS="-Wall %{rpmcflags} -I. -D_GNU_SOURCE -fPIC" \
	LDFLAGS="%{rpmldflags}" \
	CC="%{__cc} -pthread"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
 	prefix=%{_prefix} \
 	libdir=%{_lib} \
 	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install example{,.c,.stfl} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libstfl.so*

%files devel
%defattr(644,root,root,755)
%{_includedir}/stfl.h
%{_pkgconfigdir}/stfl.pc
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/example
%{_examplesdir}/%{name}-%{version}/example.*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files perl
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/auto/stfl
%{perl_vendorarch}/*.pm
%{perl_archlib}/perllocal.pod
%{perl_vendorarch}/auto/stfl/*
%{perl_vendorarch}/example.pl
%{perl_vendorarch}/auto/stfl/.packlist

%files python
%defattr(644,root,root,755)
%{py_libdir}/site-packages/lib-dynload/_stfl.so
%{py_libdir}/site-packages/stfl.pyc

%files ruby
%defattr(644,root,root,755)
%doc ruby/example.rb
%{ruby_archdir}/stfl.so
