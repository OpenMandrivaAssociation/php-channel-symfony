Summary:	The symfony project PEAR channel
Name:		php-channel-symfony
Version:	1.3
Release:	%mkrel 1
Group:		Development/PHP
License:	MIT
URL:		http://pear.symfony-project.com/
Source0:	http://pear.symfony-project.com/channel.xml
BuildRequires:	php-pear
Requires:	php-pear
Requires(post): php-pear
Requires(postun): php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package adds The symfony project PEAR channel which allows PEAR packages
from this channel to be installed.

%prep

%setup -q -c -T

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/packages

install -m0644 %{SOURCE0} %{buildroot}%{_datadir}/pear/packages/pear.symfony-project.com.xml

%post
if [ $1 -eq  1 ] ; then
    %{_bindir}/pear channel-add %{_datadir}/pear/packages/pear.symfony-project.com.xml > /dev/null || :
else
    %{_bindir}/pear channel-update %{_datadir}/pear/packages/.xml > /dev/null ||:
fi

%postun
if [ $1 -eq 0 ] ; then
    %{_bindir}/pear channel-delete pear.symfony-project.com > /dev/null || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/pear/packages/pear.symfony-project.com.xml

