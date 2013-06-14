### RPM external ncurses 5.5
%define mic %(case %cmsplatf in (*_mic_*) echo true;; (*) echo false;; esac)
%if "%mic" == "true"
Requires: icc
%endif
Source: http://ftp.gnu.org/pub/gnu/ncurses/%{n}-%{v}.tar.gz

%build
case %{cmsplatf} in
   *_mic_* )
     CXX="icpc -fPIC -mmic" CC="icc -fPIC -mmic" ./configure --prefix=%i --with-shared --enable-symlinks --host=x86_64-k1om-linux
     sed -i -e 's|cd c++ && $(MAKE) $(CF_MFLAGS) $@||' Makefile
     ;;
   * )
     ./configure --prefix=%i --with-shared --enable-symlinks
     ;;
esac
make

