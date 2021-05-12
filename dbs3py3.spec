### RPM cms dbs3 py3-0
## INITENV +PATH PYTHONPATH %i/${PYTHON_LIB_SITE_PACKAGES}
## INITENV +PATH PYTHONPATH %i/x${PYTHON_LIB_SITE_PACKAGES}
## INITENV SET DBS3_SERVER_ROOT %i/
%define webdoc_files %{installroot}/%{pkgrel}/doc/
%define wmcver 1.4.9.pre1
#
Source0: git://github.com/dmwm/WMCore.git?obj=master/%{wmcver}&export=WMCore&output=/WMCore4%{n}.tar.gz
Source1: git://github.com/yuyiguo/DBS.git?obj=py2to3-20210506/%{tag}&export=DBS&output=/%{n}.tar.gz

Requires: python3 py3-sqlalchemy py3-httplib2 py3-cherrypy py3-cheetah3 yui
Requires: py3-cx-oracle py3-docutils dbs3-pycurl-client rotatelogs pystack py3-cmsmonitoring
Requires: jemalloc
BuildRequires: py3-sphinx

%prep
%setup -T -b 0 -n WMCore
%setup -D -T -b 1 -n DBS

%build
cd ../WMCore
python setup.py build_system -s wmc-web
cd ../DBS
python setup.py build_system -s dbs-web
%install
mkdir -p %i/etc/profile.d %i/{x,}{bin,lib,data,doc} %i/{x,}$PYTHON_LIB_SITE_PACKAGES
cd ../WMCore
python setup.py install_system -s wmc-web --prefix=%i
cd ../DBS
python setup.py install_system -s dbs-web --prefix=%i
find %i -name '*.egg-info' -exec rm {} \;

# Generate dependencies-setup.{sh,csh} so init.{sh,csh} picks full environment.
mkdir -p %i/etc/profile.d
: > %i/etc/profile.d/dependencies-setup.sh
: > %i/etc/profile.d/dependencies-setup.csh
for tool in $(echo %{requiredtools} | sed -e's|\s+| |;s|^\s+||'); do
  root=$(echo $tool | tr a-z- A-Z_)_ROOT; eval r=\$$root
  if [ X"$r" != X ] && [ -r "$r/etc/profile.d/init.sh" ]; then
    echo "test X\$$root != X || . $r/etc/profile.d/init.sh" >> %i/etc/profile.d/dependencies-setup.sh
    echo "test X\$?$root = X1 || source $r/etc/profile.d/init.csh" >> %i/etc/profile.d/dependencies-setup.csh
  fi
done

%post
%{relocateConfig}etc/profile.d/dependencies-setup.*sh

%files
%{installroot}/%{pkgrel}/
%exclude %{installroot}/%{pkgrel}/doc
## SUBPACKAGE webdoc
