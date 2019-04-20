#! /usr/bin/sh

#
yum -y install git

# python3
yum install epel-release -y
yum install https://centos7.iuscommunity.org/ius-release.rpm -y
yum install python36u -y
ln -s /bin/python3.6 /bin/python3

# pip3
yum install -y epel-release
yum -y install python36-pip
pip3 install pynvim
pip3 install -U pip3

# vim-plug
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

# noevim
mkdir /usr/local/nvim
cd /usr/local/nvim
mv /tmp/nvim.appimage .
./nvim.appimage --appimage-extract
ln -s ./squashfs-root/usr/bin/nvim /usr/local/nvim/nvim
echo 'export PATH=$PATH:/usr/local/nvim'>>/root/.bashrc
./nvim -c PlugInstall -c q -c q
./nvim -c UpdateRemotePlugins -c q -c q
