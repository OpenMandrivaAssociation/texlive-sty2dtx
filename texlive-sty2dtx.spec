# revision 29743
# category Package
# catalog-ctan /support/sty2dtx
# catalog-date 2012-11-07 20:43:20 +0100
# catalog-license gpl3
# catalog-version 2.3
Name:		texlive-sty2dtx
Version:	2.3
Release:	7
Summary:	Create a .dtx file from a .sty file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/sty2dtx
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sty2dtx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sty2dtx.doc.tar.xz
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
%{_texmfdistdir}/scripts/sty2dtx/sty2dtx.pl
%doc %{_mandir}/man1/sty2dtx.1*
%doc %{_texmfdistdir}/doc/man/man1/sty2dtx.man1.pdf
%doc %{_texmfdistdir}/doc/support/sty2dtx/README
%doc %{_texmfdistdir}/doc/support/sty2dtx/sty2dtx.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

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
