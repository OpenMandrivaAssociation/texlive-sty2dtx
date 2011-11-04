# revision 21295
# category Package
# catalog-ctan /support/sty2dtx
# catalog-date 2011-02-02 18:52:18 +0100
# catalog-license gpl3
# catalog-version 2.1
Name:		texlive-sty2dtx
Version:	2.1
Release:	1
Summary:	Create a .dtx file from a .sty file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/sty2dtx
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sty2dtx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sty2dtx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-sty2dtx.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/sty2dtx
%{_texmfdistdir}/scripts/sty2dtx/sty2dtx.pl
%doc %{_texmfdistdir}/doc/support/sty2dtx/README
%doc %{_tlpkgobjdir}/*.tlpobj

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
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
