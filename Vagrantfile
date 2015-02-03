# -*- mode: ruby -*-
# vi: set ft=ruby :
MEMORY = 2048
CORES = 2
Vagrant.configure(2) do |config|
  config.vm.box = "chef/centos-6.5"
  config.vm.network "forwarded_port", guest: 8096, host: 8096
  config.vm.network "forwarded_port", guest: 8086, host: 8086
  config.vm.network "forwarded_port", guest: 80, host: 8888
  config.vm.provider "virtualbox" do |vb|
    vb.memory = MEMORY
    vb.cpus = CORES
  end
  config.vm.provider "vmware_fusion" do |v|
    v.vmx["memsize"] = MEMORY
    v.vmx["numvcpus"] = CORES
  end
  config.vm.provision :chef_zero do |chef|
    chef.cookbooks_path = "cookbooks"
    chef.add_recipe "eucatelemetry"
  end
  config.omnibus.chef_version = :latest
  config.berkshelf.enabled = true
  config.berkshelf.berksfile_path = "cookbooks/eucatelemetry/Berksfile"
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
  end
end
