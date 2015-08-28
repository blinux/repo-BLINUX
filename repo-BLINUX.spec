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
Version:        3.0
Release:        0
Summary:        BLinux repository
License:        BSD-2-Clause
Group:          System Environment/Base

Source0:	blinux-dup
Source1:	blinux-dup.service
Source2:	zypp.conf
Source3:        blinux.repo
Source4:        vlc.repo
Source5:        nvidia.repo
Source6:	opensuse-distribution-non-oss.repo
Source7:	opensuse-distribution-oss.repo
Source8:	opensuse-update-non-oss.repo
Source9:	opensuse-update-oss.repo

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
/usr/bin/systemctl enable blinux-dup.service
mkdir /var/lib/blinux-dup/
touch /var/lib/blinux-dup/runme

%install
mkdir -p %{buildroot}/%{_sysconfdir}/zypp/repos.d/
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/usr/lib/systemd/system/
install -D -p -m 755 %{SOURCE0} %{buildroot}/%{_sbindir}/
install -D -p -m 644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/
install -D -p -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/zypp/
install -D -p -m 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/zypp/repos.d/
install -D -p -m 644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/zypp/repos.d/
install -D -p -m 644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/zypp/repos.d/
install -D -p -m 644 %{SOURCE6} %{buildroot}/%{_sysconfdir}/zypp/repos.d/
install -D -p -m 644 %{SOURCE7} %{buildroot}/%{_sysconfdir}/zypp/repos.d/
install -D -p -m 644 %{SOURCE8} %{buildroot}/%{_sysconfdir}/zypp/repos.d/
install -D -p -m 644 %{SOURCE9} %{buildroot}/%{_sysconfdir}/zypp/repos.d/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/blinux-dup
/usr/lib/systemd/system/blinux-dup.service
%{_sysconfdir}/zypp/zypp.conf
%{_sysconfdir}/zypp/repos.d/blinux.repo
%{_sysconfdir}/zypp/repos.d/vlc.repo
%{_sysconfdir}/zypp/repos.d/nvidia.repo
%{_sysconfdir}/zypp/repos.d/opensuse-distribution-non-oss.repo
%{_sysconfdir}/zypp/repos.d/opensuse-distribution-oss.repo
%{_sysconfdir}/zypp/repos.d/opensuse-update-non-oss.repo
%{_sysconfdir}/zypp/repos.d/opensuse-update-oss.repo

%changelog
* Mon Aug 17 2015 Emmanuel Vadot <elbarto@bocal.org> - 3.0-0
- Update to Daiquiri Doritos

* Mon Dec 22 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.0-0
- Add Chartreuse Curly file

* Mon Oct 06 2014 Emmanuel Vadot <elbarto@bocal.org> - 0.1-0
- Package creation
