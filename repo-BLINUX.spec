#-
# Copyright 2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:		repo-BLINUX
Version:        2.0
Release:        1 
Summary:        BLinux repository
License:        BSD-2-Clause
Group:          System Environment/Base

Source0:        blinux-chartreuse-curly.repo
Source1:	opensuse-13.1-distribution-non-oss.repo
Source2:	opensuse-13.1-distribution-oss.repo	
Source3:	opensuse-13.1-update-non-oss.repo
Source4:	opensuse-13.1-update-oss.repo
Source5:	zypp.conf

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Packager:       Emmanuel Vadot <elbarto@bocal.org>
Url:            http://www.blinux.fr
Vendor:		Blinux

%description
Blinux repositories files

%prep

%build

%post

%install
mkdir -p %{buildroot}/%{_sysconfdir}/zypp/repos.d/
install -D -p -m 755 %{SOURCE0} %{buildroot}/%{_sysconfdir}/zypp/repos.d/
install -D -p -m 755 %{SOURCE1} %{buildroot}/%{_sysconfdir}/zypp/repos.d/
install -D -p -m 755 %{SOURCE2} %{buildroot}/%{_sysconfdir}/zypp/repos.d/
install -D -p -m 755 %{SOURCE3} %{buildroot}/%{_sysconfdir}/zypp/repos.d/
install -D -p -m 755 %{SOURCE4} %{buildroot}/%{_sysconfdir}/zypp/repos.d/
install -D -p -m 755 %{SOURCE5} %{buildroot}/%{_sysconfdir}/zypp/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/zypp/repos.d/blinux-chartreuse-curly.repo
%{_sysconfdir}/zypp/repos.d/opensuse-13.1-distribution-non-oss.repo
%{_sysconfdir}/zypp/repos.d/opensuse-13.1-distribution-oss.repo
%{_sysconfdir}/zypp/repos.d/opensuse-13.1-update-non-oss.repo
%{_sysconfdir}/zypp/repos.d/opensuse-13.1-update-oss.repo
%{_sysconfdir}/zypp/zypp.conf

%changelog
* Mon Dec 22 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.0-0
- Add Chartreuse Curly file

* Mon Oct 06 2014 Emmanuel Vadot <elbarto@bocal.org> - 0.1-0
- Package creation
