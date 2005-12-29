Summary:	Fast Changeset Tool
Summary(pl):	Fast Changeset Tool - narzêdzie do zestawów zmian
Name:		fastcst
Version:	0.6.5
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://www.zedshaw.com/projects/fastcst/%{name}-%{version}.tar.bz2
# Source0-md5:	6efc500b9692eb4f70b9e28fe96ddb33
URL:		http://www.zedshaw.com/projects/fastcst/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
Requires:	ruby-RMail
Requires:	ruby-guid
Requires:	ruby-pluginfactory
%ruby_mod_ver_requires_eq
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fast suffix-tree based changeset tool.

%description -l pl
Szybkie narzêdzie do zestawów zmian oparte na drzewie przyrostków
(suffiksów).

%prep
%setup -q

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc lib --inline-source
rdoc --ri lib -o ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%attr(755,root,root) %{_bindir}/fcst
%attr(755,root,root) %{ruby_archdir}/suffix_array.so
%{ruby_rubylibdir}/sadelta.rb
%{ruby_rubylibdir}/fastcst
%{ruby_ridir}/*
