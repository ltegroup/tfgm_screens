Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-22.04"
  config.vm.network :forwarded_port, host: 8120, guest: 8000
  config.vm.network :forwarded_port, host: 3315, guest: 3306
  config.vm.synced_folder "./", "/vagrant", :owner=> 'vagrant', :group=>'www-data', :mount_options => ['dmode=775', 'fmode=775']
end