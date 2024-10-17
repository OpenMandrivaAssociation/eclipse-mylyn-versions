%global eclipse_base        %{_libdir}/eclipse
%global install_loc         %{_datadir}/eclipse/dropins
# Taken from update site so we match upstream
#  http://download.eclipse.org/mylyn/archive/3.5.1/v20110422-0200/
%global qualifier           v20110422-0200

Name: eclipse-mylyn-versions
Summary: Eclipse Mylyn Versions
Version: 3.5.1
Release: 3
License: EPL
URL: https://eclipse.org/mylyn/versions/

# bash fetch-eclipse-mylyn-versions.sh
Source0: eclipse-mylyn-versions-R_3_5_1-fetched-src.tar.bz2
Source1: fetch-eclipse-mylyn-versions.sh

BuildArch: noarch

BuildRequires: java-devel >= 1.5.0
BuildRequires: eclipse-platform >= 0:3.4.0
BuildRequires: eclipse-pde >= 0:3.4.0
BuildRequires: eclipse-egit >= 0.10.1
BuildRequires: eclipse-mylyn-commons >= 3.5.0
Requires:      eclipse-mylyn-commons >= 3.5.0
Group: Development/Java


%description
Provides a framework for accessing team providers for Eclipse Mylyn.


# eclips-mylyn-versions-git

%package git
Summary: Mylyn Versions Connector: Git
Requires: eclipse-platform >= 0:3.4.0
Requires: eclipse-egit >= 0.10.1
Requires: eclipse-mylyn-versions = %{version}-%{release}
Group: Development/Java

%description git
Provides Git integration for Eclipse Mylyn.


# eclips-mylyn-versions-cvs

%package cvs
Summary: Mylyn Versions Connector: CVS
Requires: eclipse-platform >= 0:3.4.0
Requires: eclipse-mylyn-versions = %{version}-%{release}
Group: Development/Java

%description cvs
Provides CVS integration for Eclipse Mylyn.


%prep
%setup -q -n org.eclipse.mylyn.versions


%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.versions \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -d "mylyn-commons"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.git \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -d "egit jgit"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.cvs \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar


%install
install -d -m 755 %{buildroot}%{_datadir}/eclipse
install -d -m 755 %{buildroot}%{install_loc}/mylyn-versions
install -d -m 755 %{buildroot}%{install_loc}/mylyn-versions-git
install -d -m 755 %{buildroot}%{install_loc}/mylyn-versions-cvs

unzip -q -o -d %{buildroot}%{install_loc}/mylyn-versions \
 build/rpmBuild/org.eclipse.mylyn.versions.zip
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-versions-git \
 build/rpmBuild/org.eclipse.mylyn.git.zip
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-versions-cvs \
 build/rpmBuild/org.eclipse.mylyn.cvs.zip


# eclips-mylyn-versions

%files
%defattr(-,root,root,-)
%{install_loc}/mylyn-versions
%doc org.eclipse.mylyn.versions-feature/epl-v10.html
%doc org.eclipse.mylyn.versions-feature/license.html


# eclips-mylyn-versions-git

%files git
%defattr(-,root,root,-)
%{install_loc}/mylyn-versions-git
%doc org.eclipse.mylyn.git-feature/epl-v10.html
%doc org.eclipse.mylyn.git-feature/license.html


# eclips-mylyn-versions-cvs

%files cvs
%defattr(-,root,root,-)
%{install_loc}/mylyn-versions-cvs
%doc org.eclipse.mylyn.cvs-feature/epl-v10.html
%doc org.eclipse.mylyn.cvs-feature/license.html


