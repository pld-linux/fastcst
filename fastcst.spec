%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
Summary:	Fast Changeset Tool
Name:		fastcst
Version:	0.5.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.zedshaw.com/projects/fastcst/%{name}-%{version}.tar.bz2
# Source0-md5:	c5f11c44c7290131b3569bf32a80b89e
URL:		http://www.zedshaw.com/projects/fastcst/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
Requires: ruby-RMail
Requires: ruby-pluginfactory
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fast suffix-tree based changeset tool.

%prep
%setup -q -n %{name}-%{version}

%build

rm lib/pluginfactory.rb

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
%{ruby_rubylibdir}/guid.rb
%{ruby_rubylibdir}/sadelta.rb
%{ruby_rubylibdir}/fastcst
%{ruby_ridir}/*
