Summary:	A pluggable command-line tool
Summary(pl.UTF-8):	Narzędzie linii poleceń z obsługą wtyczek
Name:		python-PasteScript
Version:	1.7.3
Release:	0.2
Group:		Libraries/Python
License:	X11/MIT
Source0:	http://cheeseshop.python.org/packages/source/P/PasteScript/PasteScript-%{version}.tar.gz
# Source0-md5:	9101a3a23809d3413b39ba8b75dd0bce
URL:		http://pythonpaste.org/script/
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 0.6-0.a9.1
%pyrequires_eq	python-modules
Patch0:		%{name}-template_dir_assemble.patch
Requires:	python-Beaker >= 0.7.5
Requires:	python-cheetah
Requires:	python-FormEncode >= 0.7.0
Requires:	python-decorator >= 2.1.0
Requires:	python-Mako >= 0.1.8
Requires:	python-nose >= 0.9.3
Requires:	python-Routes >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a pluggable command-line tool. It includes some built-in
features:
- Create file layouts for packages. For instance:
   $ paste create  --template=basic_package MyPackage 
  will create a setuptools-ready file layout.
- Serving up web applications, with configuration based on
  paste.deploy.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzie linii poleceń z obsługą wtyczek. Niektóre
możliwości ma wbudowane:
- tworzenie plików dla pakietów, na przykład:
   $ paste create  --template=basic_package MyPackage 
  utworzy plik dla setuptools.
- możliwość użycia w aplikacjach WWW z konfiguracją opartą na
  paste.deploy.

%prep
%setup -q -n PasteScript-%{version}
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -and -not -path *templates* | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/
%attr(755,root,root) %{_bindir}/paster
%{py_sitescriptdir}/paste/script
%{py_sitescriptdir}/Paste*
