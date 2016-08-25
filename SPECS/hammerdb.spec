##########################
# Set global SPEC variables
############################
%global _version 2.19

###############
# Set metadata
###############

Name:    hammerdb%{suffix}
Version: %{_version}
Release: 1%{?dist}
Summary: An open source database load testing and benchmarking tool for Oracle, SQL, DB2, TimesTen, PostgreSQL and more.

Group:   Development/Tools
License: GNU General Public License
URL:     https://sourceforge.net
Source:  https://sourceforge.net/projects/hammerora/files/HammerDB/HammerDB-2.19/HammerDB-2.19-Linux-x86-64-Install/download 
Obsoletes: hammerdb%{suffix} <= 2.19
Provides: hammerdb%{suffix} = 2.19
Requires: mysql-devel, ibm-data-db2

%description

HammerDB is an open source database load testing and benchmarking tool for Oracle, SQL Server, DB2, TimesTen, PostgreSQL, Greenplum, Postgres Plus Advanced Server, MySQL,  Redis and Trafodion SQL on Hadoop


#####################
# Build requirements
#####################
BuildRoot: %(mktemp -ud %{_tmppath}/build/%{name}-%{version}-%{release}-XXXXXX)


########################################################
# PREP and SETUP
# The prep directive removes existing build directory
# and extracts source code so we have a fresh code base
# -n defines the name of the directory
#######################################################

###%prep

#%setup -q -n %{name}-%{version}
###%setup -n hammerdb-master

###########################################################
# BUILD
# The build directive does initial prep for building,
# then runs the configure script and then make to compile.
# Compiled code is placed in %{buildroot}
###########################################################



%install
export LD_LIBRARY_PATH=/usr/lib64
mkdir -p %{buildroot}/usr/local/src
pushd %{buildroot}/usr/local/src
wget https://sourceforge.net/projects/hammerora/files/HammerDB/HammerDB-2.19/HammerDB-2.19-Linux-x86-64-Install/download
echo $PWD
chmod a+x %{buildroot}/usr/local/src/download
exec %{buildroot}/usr/local/src/download
rm %{buildroot}/usr/local/src/download


###########################################################
# INSTALL
# This directive is where the code is actually installed
# in the %{buildroot} folder in preparation for packaging.
###########################################################

%clean
[ -d "%{buildroot}" -a "%{buildroot}" != "/" ] && rm -rf %{buildroot}


%files
%defattr(-,root,root,-)

#/opt/HammerDB-2.19
/usr/local/src/download

%doc



%changelog

