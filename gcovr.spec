Name:           gcovr
Version:        3.3
Release:        6%{?dist}
Summary:        A code coverage report generator using GNU gcov

License:        BSD
URL:            http://gcovr.com/
Source0:        https://github.com/gcovr/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Fix HTML reports for Python 3 (rhbz#1428277)
# From: https://github.com/gcovr/gcovr/pull/163
Patch0001:      0001-re-enable-HTML-reports-under-Python3.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       %{_bindir}/gcov

BuildArch:      noarch

%description
Gcovr provides a utility for managing the use of the GNU gcov utility
and generating summarized code coverage results.

This command is inspired by the Python coverage.py package, which provides
a similar utility in Python. The gcovr command produces either compact
human-readable summary reports, machine readable XML reports
(in Cobertura format) or simple HTML reports. Thus, gcovr can be viewed
as a command-line alternative to the lcov utility, which runs gcov and
generates an HTML-formatted report.


%prep
%autosetup -p1


%build
%py3_build


%install
%py3_install

# python metadata is useless and empty
rm -rf %{buildroot}%{python3_sitelib}

%files
%license LICENSE.txt
%doc README.md CHANGELOG.txt doc/guide.txt
%{_bindir}/gcovr

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 06 2017 Neal Gompa <ngompa13@gmail.com> - 3.3-4
- Fix HTML reports for Python 3 (#1428277)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb  2 2017 Neal Gompa <ngompa13@gmail.com> - 3.3-2
- Address review comments (#1418804)
- Switch to Python 3


* Thu Feb  2 2017 Neal Gompa <ngompa13@gmail.com> - 3.3-1
- Initial package
