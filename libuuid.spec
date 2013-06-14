### RPM external libuuid 2.22.2
%define mic %(case %cmsplatf in (*_mic_*) echo true;; (*) echo false;; esac)
%define host %{_host}
%define xcompiler %{nil}
%define xtra_args %{nil}
%if "%mic" == "true"
Requires: icc
%define host x86_64-k1om-linux
%define xcompiler CXX="icpc -fPIC -mmic"  CC="icc -fPIC -mmic" 
%define xtra_args --without-ncurses
%endif
Source: http://www.kernel.org/pub/linux/utils/util-linux/v2.22/util-linux-%{realversion}.tar.gz
Patch0: libuuid-2.22.2-disable-get_uuid_via_daemon
%define keep_archives true

%prep
%setup -n util-linux-%{realversion}
%patch0 -p1

%build
%{xcompiler} ./configure $([ $(uname) == Darwin ] && echo --disable-shared) \
            --libdir=%{i}/lib64 \
            --prefix="%{i}" \
            --build="%{_build}" \
            --host=%{host} \
            --disable-silent-rules \
            --disable-tls \
            --disable-rpath \
            --disable-libblkid \
            --disable-libmount \
            --disable-mount \
            --disable-losetup \
            --disable-fsck \
            --disable-partx \
            --disable-mountpoint \
            --disable-fallocate \
            --disable-unshare \
            --disable-eject \
            --disable-agetty \
            --disable-cramfs \
            --disable-wdctl \
            --disable-switch_root \
            --disable-pivot_root \
            --disable-kill \
            --disable-utmpdump \
            --disable-rename \
            --disable-login \
            --disable-sulogin \
            --disable-su \
            --disable-schedutils \
            --disable-wall \
            --disable-makeinstall-setuid \
            --enable-libuuid %{xtra_args}

make %{makeprocesses} uuidd

%install
# There is no make install action for the libuuid libraries only
mkdir -p %{i}/lib64
cp -p %{_builddir}/util-linux-%{realversion}/.libs/libuuid.a* %{i}/lib64
%ifos linux
cp -p %{_builddir}/util-linux-%{realversion}/.libs/libuuid.so* %{i}/lib64
%endif
mkdir -p %{i}/include
make install-uuidincHEADERS

%define drop_files %{i}/man
