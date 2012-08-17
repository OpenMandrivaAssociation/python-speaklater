%global tarName speaklater

Name:           python-%{tarName}
Version:        1.2 
Release:        1
Summary:        Implements a lazy string for python useful for use with get-text
Group:          Development/Python
License:        BSD
URL:            http://github.com/mitsuhiko/speaklater
Source0:        http://pypi.python.org/packages/source/s/%{tarName}/%{tarName}-%{version}.tar.gz
BuildArch:      noarch
%py_requires -d

%description
A module that provides lazy strings for translations. Basically you get an
object that appears to be a string but changes the value every time the value
is evaluated based on a callable you provide.

%prep
%setup -qn %{tarName}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot}

%files
%{python_sitelib}/speaklater*
%doc PKG-INFO
