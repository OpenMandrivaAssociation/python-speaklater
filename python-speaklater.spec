%global tarName speaklater

Name:           python-%{tarName}
Version:        1.3
Release:        6
Summary:        Implements a lazy string for python useful for use with get-text

Group:          Development/Python
License:        BSD
URL:            https://github.com/mitsuhiko/speaklater
Source0:        http://pypi.python.org/packages/source/s/speaklater/speaklater-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools

%description
A module that provides lazy strings for translations. Basically you get an
object that appears to be a string but changes the value every time the value
is evaluated based on a callable you provide.

%package -n python2-%{tarName}

Summary:        Implements a lazy string for python useful for use with get-text
%description -n python2-%{tarName}
A module that provides lazy strings for translations. Basically you get an
object that appears to be a string but changes the value every time the value
is evaluated based on a callable you provide.

%prep
%setup -qn %{tarName}-%{version}

cp -a . %py2dir
%build
python setup.py build

pushd %py2dir
python2 setup.py build

%install
python setup.py install --root=%{buildroot}

pushd %py2dir
python2 setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/*
%doc PKG-INFO

%files -n python2-%{tarName}
%{py2_puresitedir}/speaklater*
%doc PKG-INFO
