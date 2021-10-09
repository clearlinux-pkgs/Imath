#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Imath
Version  : 3.1.1
Release  : 10
URL      : https://github.com/AcademySoftwareFoundation/Imath/archive/v3.1.1/Imath-3.1.1.tar.gz
Source0  : https://github.com/AcademySoftwareFoundation/Imath/archive/v3.1.1/Imath-3.1.1.tar.gz
Summary  : Python bindings for the Imath libraries
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Imath-filemap = %{version}-%{release}
Requires: Imath-lib = %{version}-%{release}
Requires: Imath-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : python3
BuildRequires : python3-dev

%description
[![License](https://img.shields.io/github/license/AcademySoftwareFoundation/Imath)](LICENSE.md)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2799/badge)](https://bestpractices.coreinfrastructure.org/projects/2799)
[![Build Status](https://dev.azure.com/academysoftwarefoundation/Academy%20Software%20Foundation/_apis/build/status/academysoftwarefoundation.Imath)](https://dev.azure.com/academysoftwarefoundation/Academy%20Software%20Foundation/_build?definitionId=4&_a=summary)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=AcademySoftwareFoundation_Imath&metric=alert_status)](https://sonarcloud.io/dashboard?id=AcademySoftwareFoundation_Imath)

%package dev
Summary: dev components for the Imath package.
Group: Development
Requires: Imath-lib = %{version}-%{release}
Provides: Imath-devel = %{version}-%{release}
Requires: Imath = %{version}-%{release}

%description dev
dev components for the Imath package.


%package filemap
Summary: filemap components for the Imath package.
Group: Default

%description filemap
filemap components for the Imath package.


%package lib
Summary: lib components for the Imath package.
Group: Libraries
Requires: Imath-license = %{version}-%{release}
Requires: Imath-filemap = %{version}-%{release}

%description lib
lib components for the Imath package.


%package license
Summary: license components for the Imath package.
Group: Default

%description license
license components for the Imath package.


%prep
%setup -q -n Imath-3.1.1
cd %{_builddir}/Imath-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633755085
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v4 -m64 "
export CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -m64 "
export FFLAGS="$FFLAGS -march=x86-64-v4 -m64 "
export FCFLAGS="$FCFLAGS -march=x86-64-v4 -m64 "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../clr-build-avx2;
make test || :
cd ../clr-build-avx512;
make test || :

%install
export SOURCE_DATE_EPOCH=1633755085
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Imath
cp %{_builddir}/Imath-3.1.1/LICENSE.md %{buildroot}/usr/share/package-licenses/Imath/ce40fed41edcb2473538bb84f85ff79e585760b5
pushd clr-build-avx2
%make_install_v3  || :
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
pushd clr-build-avx512
%make_install_v4  || :
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/Imath/ImathBox.h
/usr/include/Imath/ImathBoxAlgo.h
/usr/include/Imath/ImathColor.h
/usr/include/Imath/ImathColorAlgo.h
/usr/include/Imath/ImathConfig.h
/usr/include/Imath/ImathEuler.h
/usr/include/Imath/ImathExport.h
/usr/include/Imath/ImathForward.h
/usr/include/Imath/ImathFrame.h
/usr/include/Imath/ImathFrustum.h
/usr/include/Imath/ImathFrustumTest.h
/usr/include/Imath/ImathFun.h
/usr/include/Imath/ImathGL.h
/usr/include/Imath/ImathGLU.h
/usr/include/Imath/ImathInt64.h
/usr/include/Imath/ImathInterval.h
/usr/include/Imath/ImathLine.h
/usr/include/Imath/ImathLineAlgo.h
/usr/include/Imath/ImathMath.h
/usr/include/Imath/ImathMatrix.h
/usr/include/Imath/ImathMatrixAlgo.h
/usr/include/Imath/ImathNamespace.h
/usr/include/Imath/ImathPlane.h
/usr/include/Imath/ImathPlatform.h
/usr/include/Imath/ImathQuat.h
/usr/include/Imath/ImathRandom.h
/usr/include/Imath/ImathRoots.h
/usr/include/Imath/ImathShear.h
/usr/include/Imath/ImathSphere.h
/usr/include/Imath/ImathTypeTraits.h
/usr/include/Imath/ImathVec.h
/usr/include/Imath/ImathVecAlgo.h
/usr/include/Imath/half.h
/usr/include/Imath/halfFunction.h
/usr/include/Imath/halfLimits.h
/usr/lib64/cmake/Imath/ImathConfig.cmake
/usr/lib64/cmake/Imath/ImathConfigVersion.cmake
/usr/lib64/cmake/Imath/ImathTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Imath/ImathTargets.cmake
/usr/lib64/libImath-3_1.so
/usr/lib64/libImath.so
/usr/lib64/pkgconfig/Imath.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-Imath

%files lib
%defattr(-,root,root,-)
/usr/lib64/libImath-3_1.so.29
/usr/lib64/libImath-3_1.so.29.1.0
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Imath/ce40fed41edcb2473538bb84f85ff79e585760b5
