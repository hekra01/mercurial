%global emacs_lispdir %{_datadir}/emacs/site-lisp

%global pythonver %(python -c 'import sys;print ".".join(map(str, sys.version_info[:2]))')


Summary: A fast, lightweight Source Control Management system
Name: mercurial
Version: 3.4.2
Release: 0
License: GPLv2+
Group: Development/Tools
URL: http://mercurial.selenic.com/
Source0: %{name}-%{version}.tar.gz

BuildRequires: make, gcc, gettext
BuildRequires: python >= 2.7, python-devel
Requires: python >= 2.7
# The hgk extension uses the wish tcl interpreter, but we don't enforce it
#Requires: tk

%description
Mercurial is a fast, lightweight source control management system designed
for efficient handling of very large distributed projects.

%prep
%setup -q

%build
make build

%install
rm -rf $RPM_BUILD_ROOT
make install-bin DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} MANDIR=%{_mandir}

install -m 755 contrib/hgk $RPM_BUILD_ROOT%{_bindir}/
install -m 755 contrib/hg-ssh $RPM_BUILD_ROOT%{_bindir}/

bash_completion_dir=$RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
mkdir -p $bash_completion_dir
install -m 644 contrib/bash_completion $bash_completion_dir/mercurial.sh

zsh_completion_dir=$RPM_BUILD_ROOT%{_datadir}/zsh/site-functions
mkdir -p $zsh_completion_dir
install -m 644 contrib/zsh_completion $zsh_completion_dir/_mercurial

mkdir -p $RPM_BUILD_ROOT%{emacs_lispdir}
install -m 644 contrib/mercurial.el $RPM_BUILD_ROOT%{emacs_lispdir}/
install -m 644 contrib/mq.el $RPM_BUILD_ROOT%{emacs_lispdir}/

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/mercurial/hgrc.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc CONTRIBUTORS COPYING doc/README doc/hg*.txt doc/hg*.html *.cgi contrib/*.fcgi
#%doc %attr(644,root,root) %{_mandir}/man?/hg*
#%doc %attr(644,root,root) contrib/*.svg
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_mercurial
%{_libdir}/python2.7/site-packages
%dir %{_datadir}/emacs/site-lisp/
%{_datadir}/emacs/site-lisp/mercurial.el
%{_datadir}/emacs/site-lisp/mq.el
%{_bindir}/hg
%{_bindir}/hgk
%{_bindir}/hg-ssh
%dir %{_sysconfdir}/bash_completion.d/
%config(noreplace) %{_sysconfdir}/bash_completion.d/mercurial.sh
%dir %{_sysconfdir}/mercurial
%dir %{_sysconfdir}/mercurial/hgrc.d

