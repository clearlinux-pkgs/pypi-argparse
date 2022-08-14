#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-argparse
Version  : 1.4.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/18/dd/e617cfc3f6210ae183374cd9f6a26b20514bbb5a792af97949c5aacddf0f/argparse-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/18/dd/e617cfc3f6210ae183374cd9f6a26b20514bbb5a792af97949c5aacddf0f/argparse-1.4.0.tar.gz
Summary  : Python command-line parsing library
Group    : Development/Tools
License  : Python-2.0
Requires: pypi-argparse-license = %{version}-%{release}
Requires: pypi-argparse-python = %{version}-%{release}
Requires: pypi-argparse-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
interfaces.
        
        The program defines what arguments it requires, and argparse will figure out
        how to parse those out of sys.argv. The argparse module also automatically
        generates help and usage messages and issues errors when users give the
        program invalid arguments.
        
        As of Python >= 2.7 and >= 3.2, the argparse module is maintained within the
        Python standard library. For users who still need to support Python < 2.7 or
        < 3.2, it is also provided as a separate package, which tries to stay
        compatible with the module in the standard library, but also supports older
        Python versions.
        
        Also, we can fix bugs here for users who are stuck on some non-current python
        version, like e.g. 3.2.3 (which has bugs that were fixed in a later 3.2.x
        release).
        
        argparse is licensed under the Python license, for details see LICENSE.txt.
        
        
        Compatibility
        -------------

%package license
Summary: license components for the pypi-argparse package.
Group: Default

%description license
license components for the pypi-argparse package.


%package python
Summary: python components for the pypi-argparse package.
Group: Default
Requires: pypi-argparse-python3 = %{version}-%{release}

%description python
python components for the pypi-argparse package.


%package python3
Summary: python3 components for the pypi-argparse package.
Group: Default
Requires: python3-core
Provides: pypi(argparse)

%description python3
python3 components for the pypi-argparse package.


%prep
%setup -q -n argparse-1.4.0
cd %{_builddir}/argparse-1.4.0
pushd ..
cp -a argparse-1.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656356379
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-argparse
cp %{_builddir}/argparse-1.4.0/doc/source/Python-License.txt %{buildroot}/usr/share/package-licenses/pypi-argparse/a6cdff8a5e3b32bfdbe19e3656e0414da538da84
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-argparse/a6cdff8a5e3b32bfdbe19e3656e0414da538da84

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
