# HAMMERDB 2.19 RPM built for RHEL 6.5

**Description**:  HammerDB is a graphical open source database load testing and benchmarking tool for Linux and Windows to test databases running on any operating system. HammerDB is automated, multi-threaded and extensible with dynamic scripting support

  - **Technology stack**: 

    HammerDB supports Oracle, SQL Server, DB2, TimesTen, PostgreSQL, Greenplum, Postgres Plus Advanced Server, MySQL,  Redis and Trafodion SQL on Hadoop. HammerDB includes complete built-in workloads based on industry standard benchmarks as well as capture and replay for the Oracle database.


=======

## Dependencies

The build process for the hammerdb rpm only requires the devel (x86_64) packages. 
And this hammerdb package is intended for an x86_64 system.

## Installation

Build RPM using Vagrant
1. The repo is cloned into a local sandbox
2. Run "vagrant up" to build the VM.
3. Run "vagrant ssh" to connect to VM.
4. Run "rpmbuild -ba SPECS/hammerdb.spec" to build the hammerdb rpm package.

Build RPM on server
1. Once repo is cloned, run "sh ./bootstrap.sh"
2. cd to ~/rpmbuild 
3. Run "rpmbuild -ba /SPECS/hammerdb.spec"

Installing the RPM 
Install the built RPM by running "sudo yum install RPMS/x86_64/hammerdb-1.06-1.el6.x86_64.rpm"

## Configuration

    Edit the SPEC file (SPEC/hammerdb.spec) to make necessary changes to the build configuration

=======


## Known issues

    There are no known issues related to this build process.

## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.


## Getting involved

For general instructions on _how_ to contribute, please refer to [CONTRIBUTING](CONTRIBUTING.md).


----

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)


----

## Credits and references

See below links for more information and community support.
    http://hammerora.sourceforge.net/document.html
