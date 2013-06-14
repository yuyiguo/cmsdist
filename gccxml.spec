### RPM external gccxml 20110825 
%define mic %(case %cmsplatf in (*_mic_*) echo true;; (*) echo false;; esac)
%if "%mic" != "true"
BuildRequires: cmake
%else
Requires: icc
%endif
Source: http://service-spi.web.cern.ch/service-spi/external/tarFiles/%n-%realversion.tgz
Patch0: gccxml-0.9.0_20100308-gcc45-iomanip
Patch1: gccxml-20110825-add-support-for-gcc-4.7

%prep
%setup -n %{n}
#patch0 -p1
%patch1 -p1
case %cmsos in 
  osx*_*_gcc421) ;;
  osx*)
perl -p -i -e 's|-no-cpp-precomp||g' GCC/CMakeLists.txt \
                                     GCC/configure.in \
                                     GCC/configure
  ;;
esac
%build
mkdir gccxml-build
cd gccxml-build
%if "%mic" == "true"
cmake -DCMAKE_CXX_COMPILER=icpc -DCMAKE_C_COMPILER=icc -DCMAKE_INSTALL_PREFIX:PATH=%i ..
%else
cmake -DCMAKE_INSTALL_PREFIX:PATH=%i ..
%endif
make %makeprocesses

%install
cd gccxml-build
make install
%define drop_files %i/share/{man,doc}

%post
find $RPM_INSTALL_PREFIX/%{pkgrel}/share -name gccxml_config -exec %relocateCmsFiles {} \;
