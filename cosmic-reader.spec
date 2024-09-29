Name:           cosmic-reader
Version:        0.1.0+git20240926
Release:        0
Summary:        COSMIC PDF reader
License:        GPL-3.0-only
Group:          Reader
URL:            https://github.com/pop-os/cosmic-reader
# Source0:        https://github.com/pop-os/cosmic-screenshot/archive/epoch-%{version}-alpha.2/%{name}-epoch-%{version}-alpha.2.tar.gz
Source0:        cosmic-reader-master.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -n cosmic-reader-master -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%cargo_build

%install
install -Dm0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}
