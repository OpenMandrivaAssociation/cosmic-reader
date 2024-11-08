Name:           cosmic-reader
Version:        0.1.0+git20241022
Release:        0
Summary:        COSMIC PDF reader
License:        GPL-3.0-only
Group:          Reader
URL:            https://github.com/pop-os/cosmic-reader
# Source0:        https://github.com/pop-os/cosmic-screenshot/archive/epoch-%{version}-alpha.2/%{name}-epoch-%{version}-alpha.2.tar.gz
Source0:        cosmic-reader-master.tar.gz
Source1:        vendor.tar.xz
#Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -n cosmic-reader-master -a1 -p1
%cargo_prep -v vendor
cat >>.cargo/config.toml <<EOF
[source."git+https://github.com/DioxusLabs/taffy?rev=7781c70"]
git = "https://github.com/DioxusLabs/taffy"
rev = "7781c70"
replace-with = "vendored-sources"

[source."git+https://github.com/jackpot51/rust-atomicwrites"]
git = "https://github.com/jackpot51/rust-atomicwrites"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-text.git"]
git = "https://github.com/pop-os/cosmic-text.git"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/glyphon.git?tag=iced-0.14-dev"]
git = "https://github.com/pop-os/glyphon.git"
tag = "iced-0.14-dev"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/libcosmic.git"]
git = "https://github.com/pop-os/libcosmic.git"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/smithay-clipboard?tag=pop-dnd-5"]
git = "https://github.com/pop-os/smithay-clipboard"
tag = "pop-dnd-5"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/softbuffer?tag=cosmic-4.0"]
git = "https://github.com/pop-os/softbuffer"
tag = "cosmic-4.0"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/window_clipboard.git?tag=pop-0.13"]
git = "https://github.com/pop-os/window_clipboard.git"
tag = "pop-0.13"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/winit.git?tag=iced-xdg-surface-0.13"]
git = "https://github.com/pop-os/winit.git"
tag = "iced-xdg-surface-0.13"
replace-with = "vendored-sources"

[source."git+https://github.com/wash2/accesskit?tag=iced-xdg-surface-0.13"]
git = "https://github.com/wash2/accesskit"
tag = "iced-xdg-surface-0.13"
replace-with = "vendored-sources"
EOF

%build
%cargo_build

%install
install -Dm0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}
