# generated by cabal-rpm-2.2.2 --standalone
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%undefine with_ghc_prof
%undefine with_haddock
%global without_prof 1
%global without_haddock 1
%global debug_package %{nil}

Name:           compare-fonts
Version:        0.1.0
Release:        1%{?dist}
Summary:        GTK tool to compare 2 fonts

License:        GPL-3.0-or-later
Url:            https://github.com/juhp/compare-fonts
# Begin cabal-rpm sources:
Source0:        https://github.com/juhp/compare-fonts/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# End cabal-rpm sources
Patch0:         gi-pango-1.0.29-f40.patch

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-gi-gtk-devel
#BuildRequires:  ghc-gi-gtk-declarative-devel
#BuildRequires:  ghc-gi-gtk-declarative-app-simple-devel
BuildRequires:  ghc-gi-pango-devel
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-simple-cmd-devel
BuildRequires:  ghc-simple-cmd-args-devel
BuildRequires:  ghc-simple-prompt-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  help2man
BuildRequires:  cabal-install
# for missing dep 'gi-gtk-declarative':
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-gi-glib-devel
BuildRequires:  ghc-gi-gobject-devel
BuildRequires:  ghc-haskell-gi-devel
BuildRequires:  ghc-haskell-gi-base-devel
BuildRequires:  ghc-haskell-gi-overloading-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-unordered-containers-devel
# for missing dep 'gi-gtk-declarative-app-simple':
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-gi-gdk-devel
BuildRequires:  ghc-gi-glib-devel
BuildRequires:  ghc-gi-gobject-devel
BuildRequires:  ghc-haskell-gi-devel
BuildRequires:  ghc-haskell-gi-base-devel
BuildRequires:  ghc-haskell-gi-overloading-devel
BuildRequires:  ghc-pipes-devel
# for missing dep 'pipes-concurrency':
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-pipes-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-void-devel
# End cabal-rpm deps
BuildRequires:  git-core

%description
Compare two fonts next to each other on some sample text.


%prep
# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup
%if 0%{?fedora} < 41
%autopatch -p1
%endif


%build
# Begin cabal-rpm build:
%global cabal_install %{_bindir}/cabal
%cabal_install update
%if %{defined rhel} && 0%{?rhel} < 9
%cabal_install sandbox init
%cabal_install install
%endif
# End cabal-rpm build


%install
# Begin cabal-rpm install
mkdir -p %{buildroot}%{_bindir}
%if %{defined fedora} || 0%{?rhel} >= 9
%ghc_set_gcc_flags
%cabal_install install --install-method=copy --enable-executable-stripping --installdir=%{buildroot}%{_bindir}
%else
for i in .cabal-sandbox/bin/*; do
strip -s -o %{buildroot}%{_bindir}/$(basename $i) $i
done
%endif

set noclobber
mkdir -p %{buildroot}%{bash_completions_dir}
%{buildroot}%{_bindir}/%{name} --bash-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{bash_completions_dir}/%{name}

mkdir -p %{buildroot}%{_mandir}/man1/
help2man --no-info %{buildroot}%{_bindir}/%{name} > %{buildroot}%{_mandir}/man1/%{name}.1
# End cabal-rpm install


%files
# Begin cabal-rpm files:
%license COPYING
%doc ChangeLog.md README.md
%{_bindir}/%{name}
%{bash_completions_dir}/%{name}
%{_mandir}/man1/%{name}.1*
# End cabal-rpm files


%changelog
* Mon Nov 11 2024 Jens Petersen <juhpetersen@gmail.com> - 0.1.0-1
- spec file generated by cabal-rpm-2.2.2
