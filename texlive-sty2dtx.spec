Name:		texlive-sty2dtx
Version:	64967
Release:	2
Summary:	Create a .dtx file from a .sty file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/sty2dtx
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sty2dtx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sty2dtx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-sty2dtx.bin = %{EVRD}

%description
The package provides a Perl script that converts a .sty file
(LaTeX package) to .dtx format (documented LaTeX source), by
surrounding macro definitions with macro and macrocode
environments. The macro name is automatically inserted as an
argument to the macro environemnt. Code lines outside macro
definitions are wrapped only in macrocode environments. Empty
lines are removed. The script should not be thought to be fool
proof and 100% accurate but rather as a good start to the
business of making a .dtx file from an undocumented style file.
Full .dtx files are generated. A template based on the skeleton
file from 'dtxtut' is used. User level macros are added
automatically to the 'Usage' section of the .dtx file. A
corresponding .ins file can be generated as well.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/sty2dtx
%{_texmfdistdir}/scripts/sty2dtx
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/support/sty2dtx

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/sty2dtx/sty2dtx.pl sty2dtx
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
