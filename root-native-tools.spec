### RPM external root-native-tools 5.34.07
## NOCOMPILER
Source: http://cern.ch/muzaffar/root.%{realversion}.slc6.tar.gz

%prep
%setup -n root.%{realversion}.slc6

%build
%install
mkdir %i/bin
cp * %i/bin
%post
echo "ROOT_NATIVE_TOOLS_ROOT='$CMS_INSTALL_PREFIX/%{pkgrel}'" > $RPM_INSTALL_PREFIX/%{pkgrel}/etc/profile.d/init.sh
echo "ROOT_NATIVE_TOOLS_VERSION='%v'" >> $RPM_INSTALL_PREFIX/%{pkgrel}/etc/profile.d/init.sh
echo "set ROOT_NATIVE_TOOLS_ROOT='$CMS_INSTALL_PREFIX/%{pkgrel}'" > $RPM_INSTALL_PREFIX/%{pkgrel}/etc/profile.d/init.csh
echo "set ROOT_NATIVE_TOOLS_VERSION='%v'" >> $RPM_INSTALL_PREFIX/%{pkgrel}/etc/profile.d/init.csh
