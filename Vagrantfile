# Defines our Vagrant environment
#
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

 # create hammerdb node (change this to new project)

  config.vm.define :hammerdb do |hammerdb_config|
      hammerdb_config.vm.box = "bento/centos-6.7"
      hammerdb_config.vm.hostname = "hammerdb"
      hammerdb_config.vm.network :private_network, ip: "192.168.1.9"
      hammerdb_config.vm.provider "virtualbox" do |vb|
      hammerdb_config.ssh.forward_agent = true
      hammerdb_config.ssh.forward_x11 = true
      end 
      hammerdb_config.vm.provision :shell, path: "bootstrap-hammerdb.sh", privileged: false
  end 

end
