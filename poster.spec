Summary:	Poster - a small utility to generate posters
Summary(pl):	Poster - ma³e narzêdzie do generowania plakatów
Name:		poster
Group:		Applications
Version:	19950907
Release:	0.1
Epoch:		0
License:	GPL
Source0:	http://www.geocities.com/SiliconValley/5682/%{name}.zip
# Source0-md5:	4f96357892fe6f758fab9879c575cc62
URL:		http://www.geocities.com/SiliconValley/5682/poster.html
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Poster is a small utility for making a poster - a large printed image
- from an EPS file or a one-page PS document.

%description -l pl
Poster jest ma³ym narzêdziem s³u¿±cym do tworzenia plakatów -
wielkowymiarowych obrazów - z plików EPS lub jednostronicowych
dokumentów PS.

%prep
%setup -q -c

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install poster $RPM_BUILD_ROOT%{_bindir}
install poster.1 $RPM_BUILD_ROOT%{_mandir}/man1/poster.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
