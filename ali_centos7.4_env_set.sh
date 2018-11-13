#! /bin/bash

# 'source xxx.sh' run this script 

profile=/etc/profile

# solving "-bash: warning: setlocale: LC_CTYPE: cannot change locale (UTF-8): No such file or directory" alert
echo 'LC_ALL=en_US.UTF-8
LANG=en_US.UTF-8'>>/etc/environment

# set Java
jdk=`ls |grep jdk`
tar -xvf $jdk
jdk=`ls |grep jdk[0-9]`
cp -r $jdk /usr/local/
echo "export JAVA_HOME=/usr/local/$jdk" >> $profile
sed -i '$a export PATH=$PATH:${JAVA_HOME}/bin' $profile
ln -s /usr/local/$jdk/bin/java /usr/bin/java # jenkins use /usr/bin/java
rm -rf $jdk
unset jdk

# set jenkins
jenkins=`ls|grep jenk`
rpm -ivh $jenkins
/etc/init.d/jenkins start
unset jenkins

# set Python
yum -y install ncurses ncurses-devel  
yum install openssl openssl-devel -y
python=`ls|grep Python`
tar -xvf $python
python=`ls|grep Python.*[0-9]$`
cd $python&&./configure --prefix=/usr/local/$python

setup=Modules/Setup
sed -i 's/#_socket socketmodule.c/_socket socketmodule.c/g' $setup
l=`grep -n '#_ssl _ssl.c' $setup  |cut -d ':' -f 1` # awsome...... god.
txt=`sed -n "$l,$[$l+2]p" $setup`
sed -i "$l,$[l+2]d" $setup
txt=`echo $txt|sed 's/#//g'`
sed -i "${l}a $txt" $setup

make&&make install
echo 'export PATH=$PATH:'"/usr/local/${python}/bin">> $profile
cd -
rm -rf $python
unset setup
unset python

# set rvm
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
\curl -sSL https://get.rvm.io | bash -s stable
echo 'export PATH=$PATH:/usr/local/rvm/bin'>> $profile

# set vim
echo 'alias vi=vim'>>~/.bashrc
yum -y install git
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
cp vimrc ~/.vimrc
echo '------------------------------------------------'
echo -e "run ':PluginInstall' using vim at the first time"
echo '------------------------------------------------'

#
echo 'alias h=history'>>~/.bashrc

#
. $profile&&. ~/.bashrc
unset profile
