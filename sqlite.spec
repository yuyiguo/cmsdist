### RPM external sqlite 3.7.10
%define mic %(case %cmsplatf in (*_mic_*) echo true;; (*) echo false;; esac)
%if "%mic" == "true"
Requires: icc
%endif
Source: http://www.sqlite.org/sqlite-autoconf-3071000.tar.gz

%prep
%setup -n sqlite-autoconf-3071000

%build
case %{cmsplatf} in
   *_mic_* )
    CXX="icpc -fPIC -mmic"  CC="icc -fPIC -mmic" ./configure --prefix=%i --disable-tcl --disable-static --host=x86_64-k1om-linux
     ;;
   * )
     ./configure --prefix=%i --disable-tcl --disable-static
     ;;
esac
make %makeprocesses

%install
make install
rm -rf %i/lib/pkgconfig
%define strip_files %i/lib
