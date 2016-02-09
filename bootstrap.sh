#!/usr/bin/env bash

sudo yum -y groupinstall 'Development Tools'
sudo yum -y install java-1.7.1*
sudo yum -y install vim
sudo yum -y install libselinux*
sudo yum -y install yum localinstall http://yum.postgresql.org/9.4/redhat/rhel-6-x86_64/pgdg-centos94-9.4-1.noarch.rpm
sudo yum -y install postgresql9*
sudo yum -y install tree
sudo yum -y install xclock
sudo yum -y install xorg-x11*
sudo yum -y groupinstall 'X Window System'
sudo yum -y install libXScrnSaver-1.2.2-2.el6.x86_64

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
