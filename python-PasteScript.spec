Summary:	A pluggable command-line tool
Summary(pl):	Narzêdzie linii poleceñ z obs³ug± wtyczek
Name:		python-PasteScript
Version:	1.0
Release:	1
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://cheeseshop.python.org/packages/source/P/PasteScript/PasteScript-%{version}.tar.gz
# Source0-md5:	5ea4a56bc757685aaadddafbe0d64244
URL:		http://pythonpaste.org/script/
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 0.6-0.a9.1
%pyrequires_eq	python-modules
Requires:	python-cheetah
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

%description -l pl
Ten pakiet zawiera narzêdzie linii poleceñ z obs³ug± wtyczek. Niektóre
mo¿liwo¶ci ma wbudowane:
- tworzenie plików dla pakietów, na przyk³ad:
   $ paste create  --template=basic_package MyPackage 
  utworzy plik dla setuptools.
- mo¿liwo¶æ u¿ycia w aplikacjach WWW z konfiguracj± opart± na
  paste.deploy.

%prep
%setup -q -n PasteScript-%{version}

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
