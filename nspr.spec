### RPM external nspr 4.8.9
%define mic %(case %cmsplatf in (*_mic_*) echo true;; (*) echo false;; esac)
%if "%mic" == "true"
Requires: icc
%endif
Source: https://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v%{realversion}/src/%n-%{realversion}.tar.gz
Patch0: nspr-4.8.9-mic

%prep
%setup -n %n-%{realversion}
%if "%mic" == "true"
%patch0 -p1
%endif

%build
pushd mozilla/nsprpub
  case %{cmsplatf} in
   *_mic_* )
    CXX="icpc -fPIC -mmic"  CC="icc -fPIC -mmic" ./configure --disable-static --prefix %i --enable-64bit --host=x86_64-k1om-linux
     ;;
   * )
     ./configure --disable-static --prefix %i --enable-64bit
     ;;
  esac
  make %makeprocesses
popd

%install
pushd mozilla/nsprpub
  make install
popd
%define strip_files %i/lib
