Summary:	Proprietary data files for freecnc
Summary(pl.UTF-8):	Komercyjne pliki gry dla freecnc
Name:		freecnc-data
Version:	0.1
Release:	0.1
# not sure
License:	Commercial
Group:		X11/Applications/Games
Source0:	ftp://ftp.westwood.com/pub/cc1/previews/demo/cc1demo1.zip
# NoSource0-md5:	7d770d38618e20796fbe642037f08de5
Source1:	ftp://ftp.westwood.com/pub/cc1/previews/demo/cc1demo2.zip
# NoSource1-md5:	bbe489d259c4e6d6cadb4a2544b764aa
Source2:	ftp://ftp.westwood.com/pub/redalert/previews/demo/ra95demo.zip
# NoSource2-md5:	b44ab9ec1bc634ea755587d1988e3722
NoSource:	0
NoSource:	1
NoSource:	2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeCNC will be a free implementation of the Command & Conquer Game
Engine written in SDL. It will support the original C&C graphics and
audio, as well as Red Alert's data files.

%description -l pl.UTF-8
FreeCNC będzie wolnodostępną, napisaną w SDL implementacją silnika gry
Command & Conquer. Będzie wspierać grafikę i efekty dźwiękowe zarówno
z plików gry Command & Conquer jak i Red Alert.

%prep
%setup -q -c -a1 -a2
for i in *.MIX *.AUD; do
	mv $i `echo $i | tr A-Z a-z`;
done

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/freecnc
install *.mix *.aud $RPM_BUILD_ROOT%{_datadir}/freecnc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DEMOMAN.TXT FAQ.TXT README.TXT
%{_datadir}/freecnc/*
