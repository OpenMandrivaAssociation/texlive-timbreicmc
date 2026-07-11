%global tl_name timbreicmc
%global tl_revision 49740

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Typeset documents with ICMC/USP watermarks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/timbreicmc
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/timbreicmc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/timbreicmc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/timbreicmc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
With this package you can typeset documents with ICMC/USP Sao Carlos
watermarks. ICMC is acronym for "Instituto de Ciencias Matematicas e de
Computacao" of the "Universidade de Sao Paulo" (USP), in the city of Sao
Carlos-SP, Brazil.

