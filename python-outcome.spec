%global _empty_manifest_terminate_build 0
Name:		python-outcome
Version:	1.1.0
Release:	1
Summary:	Capture the outcome of Python function calls.
License:	MIT or Apache-2.0
URL:		https://github.com/python-trio/outcome
Source0:	https://files.pythonhosted.org/packages/88/b5/9ccedd89d641dcfa5771f636a8a2e99f9d98b09f511f4f870d382ef2b007/outcome-1.1.0.tar.gz
BuildArch:	noarch

Requires:	python3-attrs

%description
Capture the outcome of Python function calls. Extracted from the Trio project.

%package -n python3-outcome
Summary:	Capture the outcome of Python function calls.
Provides:	python-outcome
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-outcome
Capture the outcome of Python function calls. Extracted from the Trio project.

%package help
Summary:	Development documents and examples for outcome
Provides:	python3-outcome-doc
%description help
Capture the outcome of Python function calls. Extracted from the Trio project.

%prep
%autosetup -n outcome-1.1.0

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-outcome -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Dec 17 2021 Python_Bot <Python_Bot@openeuler.org> - 1.1.0-1
- Package Init
