%global tl_name cormorantgaramond
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.601
Release:	%{tl_revision}.1
Summary:	Cormorant Garamond family of fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cormorantgaramond
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cormorantgaramond.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cormorantgaramond.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Cormorant Garamond family of fonts, designed by Christian Thalman of
Catharsis Fonts. The family includes light, regular, medium, semi-bold,
and bold weights, with italics.

