### RPM external xz 5.0.3
%define mic %(case %cmsplatf in (*_mic_*) echo true;; (*) echo false;; esac)
%if "%mic" == "true"
Requires: icc
%endif
Source: http://tukaani.org/%n/%n-%realversion.tar.bz2

%prep
%setup -n %n-%realversion
perl -p -i -e '/LZMA_PROG_ERROR\s+=/ && s/,$//' src/liblzma/api/lzma/base.h


%build
case %{cmsplatf} in
   *_mic_* )
    CXX="icpc -fPIC -mmic"  CC="icc -fPIC -mmic" ./configure CFLAGS='-fPIC -Ofast' --prefix=%i --disable-static --host=x86_64-k1om-linux
     ;;
   * )
     ./configure CFLAGS='-fPIC -Ofast' --prefix=%i --disable-static
     ;;
esac
make %makeprocesses

%install
make %makeprocesses install
rm -rf %i/lib/pkgconfig
%define strip_files %i/lib
%define drop_files %i/share
