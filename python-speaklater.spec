%global tarName speaklater

Name:           python-%{tarName}
Version:        1.3
Release:        1
Summary:        Implements a lazy string for python useful for use with get-text

Group:          Development/Python
License:        BSD
URL:            http://github.com/mitsuhiko/speaklater
Source0:        http://pypi.python.org/packages/source/s/speaklater/speaklater-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel

%description
A module that provides lazy strings for translations. Basically you get an
object that appears to be a string but changes the value every time the value
is evaluated based on a callable you provide.

%prep
%setup -qn %{tarName}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/speaklater*
%doc PKG-INFO



