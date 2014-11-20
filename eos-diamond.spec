%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress
Summary: The EOS Diamond Storage bundle
Name: eos-diamond
Version: 1.1
Release: 1
License: GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Group: Applications/File
URL: https://github.com/cern-eos/eos-diamond
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch 

Requires: radosfs >= 0.5.1
Requires: radosfs-tools >= 0.5.1
Requires: xrootd-rados-oss >= 0.1.2
Requires: xrootd-diamond-ofs >= 0.1.2
Requires: xrootd-auth-change-uid >= 0.1.0

%description
This bundle RPM provides the relevant XRootD and CEPH plug-ins to run an EOS Diamond Storage service.
%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc


%changelog
* Fri Nov  7 2014 root <root@xrados.cern.ch> - diamond 1.0
- Initial build.

