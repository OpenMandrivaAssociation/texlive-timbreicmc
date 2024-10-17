Name:		texlive-timbreicmc
Version:	49740
Release:	2
Summary:	Typeset documents with ICMC/USP watermarks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/timbreicmc
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/timbreicmc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/timbreicmc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/timbreicmc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
With this package you can typeset documents with ICMC/USP Sao
Carlos watermarks. ICMC is acronym for "Instituto de Ciencias
Matematicas e de Computacao" of the "Universidade de Sao Paulo"
(USP), in the city of Sao Carlos-SP, Brazil.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/timbreicmc
%{_texmfdistdir}/tex/latex/timbreicmc
%doc %{_texmfdistdir}/doc/latex/timbreicmc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
