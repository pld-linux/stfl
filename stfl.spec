Summary:	STFL implements a curses-based widget set for text terminals
Summary(pl.UTF-8):	Implementacja opartego na ncurses zestawu widgetów dla terminali tekstowych
Name:		stfl
Version:	0.19
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.clifford.at/stfl/%{name}-%{version}.tar.gz
# Source0-md5:	2e7859da0ed1f867dfec52f50eedd5d9
Patch0:		%{name}-libdir.patch
URL:		http://www.clifford.at/stfl/
BuildRequires:	ncurses-devel
BuildRequires:	perl-devel
BuildRequires:	python-devel
BuildRequires:	ruby-devel
BuildRequires:	swig-perl
BuildRequires:	swig-python
BuildRequires:	swig-ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
STFL is a library which implements a curses-based widget set for text
terminals.

%description -l pl.UTF-8
STFL jest biblioteką udostępniającą implementacją opartego na ncurses
zestawu widgetów dla terminali tekstowych.

%package devel
Summary:	Header files for STFL library
Summary(pl.UTF-8):	Pliki nagłówekowe biblioteki STFL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for STFL library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki STFL.

%package static
Summary:	Static STFL library
Summary(pl.UTF-8):	Statyczna biblioteka STFL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static STFL library.

%description static -l pl.UTF-8
Statyczna biblioteka STFL.

%package perl
Summary:	Perl binding for STFL
Summary(pl.UTF-8):	Wiązania Perla dla STFLa
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
Perl binding for STFL.

%description perl -l pl.UTF-8
Wiązania Perla dla STFLa.

%package python
Summary:	Python binding for STFL
Summary(pl.UTF-8):	Wiązania Pythona dla STFLa
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description python
Python binding for STFL.

%description python -l pl.UTF-8
Wiązania Pythona dla STFLa.

%package ruby
Summary:	Ruby binding for STFL
Summary(pl.UTF-8):	Wiązania Ruby'ego dla STFLa
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ruby
Ruby binding for STFL.

%description ruby -l pl.UTF-8
Wiązania Ruby'ego dla STFLa.

%prep
%setup -q
%patch0 -p1
%{__sed} -i 's,$(prefix)/lib,/%{_libdir},g' python/Makefile.snippet
%{__sed} -i 's,$(prefix)/lib,/%{_libdir},g' ruby/Makefile.snippet


%build
%{__make} -j1 \
	CC="%{__cc} -pthread" \
	CFLAGS="%{rpmcflags} %{rpmldflags} -I. -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	prefix=%{_prefix} \
	libdir=%{_lib} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING

%files devel
%defattr(644,root,root,755)
%{_includedir}/stfl.h

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

%files python
%defattr(644,root,root,755)
%{py_libdir}/lib-dynload/_stfl.so
%{py_libdir}/*

%files ruby
%defattr(644,root,root,755)
%{ruby_archdir}/stfl.so
