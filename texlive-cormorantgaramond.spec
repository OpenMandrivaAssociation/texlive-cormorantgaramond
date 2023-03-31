Name:		texlive-cormorantgaramond
Version:	64411
Release:	2
Summary:	Cormorant Garamond family of fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cormorantgaramond
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cormorantgaramond.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cormorantgaramond.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Cormorant Garamond family of fonts, designed by
Christian Thalman of Catharsis Fonts. The family includes
light, regular, medium, semi-bold, and bold weights, with
italics.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/cormorantgaramond
%{_texmfdistdir}/fonts/vf/catharsis/cormorantgaramond
%{_texmfdistdir}/fonts/type1/catharsis/cormorantgaramond
%{_texmfdistdir}/fonts/truetype/catharsis/cormorantgaramond
%{_texmfdistdir}/fonts/tfm/catharsis/cormorantgaramond
%{_texmfdistdir}/fonts/map/dvips/cormorantgaramond
%{_texmfdistdir}/fonts/enc/dvips/cormorantgaramond
%doc %{_texmfdistdir}/doc/fonts/cormorantgaramond

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
