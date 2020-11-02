#
# spec file for package skelcd-control-SMO
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           skelcd-control-MicroOS
Version:        5.0.0
Release:        0
Summary:        The SUSEM MicroOS Installation Control file
License:        MIT
Group:          Metapackages
#
######################################################################
URL:            https://github.com/yast/skelcd-control-SMO
Source:         skelcd-control-SMO-%{version}.tar.bz2
# xmllint
BuildRequires:  libxml2-tools
# xsltproc
BuildRequires:  libxslt-tools
# RNG schema
BuildRequires:  yast2-installation-control
# Generic Yast packages needed for the installer
Requires:       autoyast2
Requires:       yast2-add-on
Requires:       yast2-buildtools
Requires:       yast2-caasp >= 4.2.1
Requires:       yast2-devtools
Requires:       yast2-fcoe-client
Requires:       yast2-registration >= 4.2.27
# For creating the AutoYast profile at the end of installation (bnc#887406)
Requires:       yast2-firewall
# instsys_cleanup
Requires:       yast2-installation >= 3.1.217.9
Requires:       yast2-iscsi-client
Requires:       yast2-kdump
Requires:       yast2-multipath
Requires:       yast2-network >= 3.1.42
Requires:       yast2-nfs-client
Requires:       yast2-ntp-client
Requires:       yast2-proxy
# Install and enable xrdp by default (FATE#320363)
Requires:       yast2-rdp
Requires:       yast2-services-manager
Requires:       yast2-slp
######################################################################
#
# Here is the list of Yast packages which are needed in the
# installation system (inst-sys) for the Yast installer
#
# branding
# FIXME Requires:       yast2-qt-branding-SLE
Requires:       yast2-theme
Requires:       yast2-trans-stats
Requires:       yast2-tune
Requires:       yast2-update
Requires:       yast2-users
Requires:       yast2-x11
# Ruby debugger in the inst-sys (FATE#318421)
Requires:       rubygem(%{rb_default_ruby_abi}:byebug)
# Ensure no two skelcd-control-* packages can be installed in the same time,
# an OBS check reports a file conflict for the /CD1/control.xml file from
# the other packages.
Conflicts:      product_control
Provides:       product_control
Provides:       system-installation() = SMO
# Architecture specific packages
#
%ifarch %{ix86} x86_64
Requires:       yast2-vm
%endif

# avoid file conflict with SLES package
Obsoletes:	skelcd-control-leanos

%description
This package contains the control file used for SUSE MicroOS installation.

%prep

%setup -q -n skelcd-control-SMO-%{version}

%build
%make_build -C control

%check
%make_build -C control check

%install
#
# Add control file
#
mkdir -p %{buildroot}%{_prefix}/lib/skelcd/CD1
install -m 644 control/control.SMO.xml %{buildroot}%{_prefix}/lib/skelcd/CD1/control.xml

# install LICENSE (required by build service check)
mkdir -p %{buildroot}/%{_docdir}/%{name}
install -m 644 LICENSE %{buildroot}/%{_docdir}/%{name}

%files
%defattr(644,root,root,755)
%{_prefix}/lib/skelcd
%doc %dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/LICENSE

%changelog
