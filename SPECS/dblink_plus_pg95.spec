# SPEC file for dblink_plus
# Copyright(C) 2016 NIPPON TELEGRAPH AND TELEPHONE CORPORATION

%define _pgdir   /usr/pgsql-9.5
%define _bindir  %{_pgdir}/bin
%define _libdir  %{_pgdir}/lib
%define _datadir %{_pgdir}/share/extension

## Set general information
Summary:    PostgreSQL module to connect PostgreSQL/Oracle
Name:       dblink_plus
Version:    1.0.2
Release:    1%{?dist}
License:    BSD
Group:      Applications/Databases
Source0:    %{name}-%{version}.tar.gz
URL:        http://interdbconnect.sourceforge.net/dblink_plus/dblink_plus-ja.html
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Vendor:     NIPPON TELEGRAPH AND TELEPHONE CORPORATION
#Following is needed to remove auto-discovery of oci library files(not under RPM package management)
AutoReqProv: no

## We use postgresql-devel package
BuildRequires:  postgresql95-devel
Requires:  postgresql95-libs

## Description
%description
dblink_plus is a PostgreSQL module which supports connections to other databases.
It is similar to contrib/dblink except that it can connect to Oracle, MySQL and sqlite3. 

## prework
%prep
%setup -q -n %{name}-%{version}

## Set variables for build environment
%build
USE_PGXS=1 make %{?_smp_mflags} MYSQL=0 SQLITE3=0

## Set variables for install
%install
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}
install -m 755 dblink_plus.so %{buildroot}%{_libdir}/dblink_plus.so
install -d %{buildroot}%{_datadir}
install -m 755 dblink_plus.sql %{buildroot}%{_datadir}/dblink_plus.sql
install -m 755 dblink_plus--1.0.2.sql %{buildroot}%{_datadir}/dblink_plus--1.0.2.sql
install -m 755 dblink_plus.control %{buildroot}%{_datadir}/dblink_plus.control
install -m 755 uninstall_dblink_plus.sql %{buildroot}%{_datadir}/uninstall_dblink_plus.sql
install -m 755 COPYRIGHT %{buildroot}%{_datadir}/COPYRIGHT_dblink_plus


%clean
rm -rf %{buildroot}

%files
%defattr(755,root,root)
%{_libdir}/dblink_plus.so
%{_datadir}/dblink_plus.sql
%{_datadir}/dblink_plus--1.0.2.sql
%{_datadir}/dblink_plus.control
%{_datadir}/uninstall_dblink_plus.sql
%{_datadir}/COPYRIGHT_dblink_plus

# History.
%changelog
* Tue Mar 29  2016 - NTT OSS Center <furutani.kaname@lab.ntt.co.jp> 1.0.2-1
initial packaging
