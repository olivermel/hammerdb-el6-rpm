#!/usr/bin/env bash

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

if [ "$SCRIPTPATH" = "/tmp" ] ; then
       SCRIPTPATH=/vagrant
   fi
  
  mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS}
 ln -sf $SCRIPTPATH/SPECS $HOME/rpmbuild/SPECS
echo '%_topdir '$HOME'/rpmbuild' > $HOME/.rpmmacros
cd $HOME/rpmbuild/SOURCES
wget https://sourceforge.net/projects/hammerora/files/HammerDB/HammerDB-2.19/HammerDB-2.19-Linux-x86-64-Install/download
chmod +x /home/vagrant/rpmbuild/SOURCES/download
bash -x/home/vagrant/rpmbuild/SOURCES/download
