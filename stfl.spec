Summary:	STFL implements a curses-based widget set for text terminals.
Name:		stfl
Version:	0.19
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://www.clifford.at/stfl/%{name}-%{version}.tar.gz
# Source0-md5:	2e7859da0ed1f867dfec52f50eedd5d9
URL:		http://www.clifford.at/stfl/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
STFL is a library which implements a curses-based widget set for 
text terminals.

%package devel
Summary:	Header files for develop STFL-based application
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%description devel
This package includes the header files and libraries necessary to
develop applications that use STFL.

%prep
%setup -q
#%patch0 -p1

%build

%{__make} prefix=/usr

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install prefix=/usr\
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING
%defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}
%{_libdir}/lib%{name}*

%files devel
%dir %{_includedir}
%{_includedir}/stfl.h
