#! /bin/bash
#

#
yum -y install git

#
echo "vi=vim">>$HOME/.bashrc
echo "h=histroy">>$HOME/.bashrc

#
echo "LC_ALL=en_US.UTF-8
LANG=en_US.UTF-8">>/etc/environment

# jdk, openjdk的判断没用，压根系统默认不携带
openjdk=`rpm -qa|grep openjdk`
if test -n "$openjdk" ;then
	read -p "1. Remove openjdk manually (y|Y)?
2. Other key to ignore it. " ans
	[ "$ans" == "Y" -o "$ans" == "y" ] && exit 0
fi
jdk=$(ls|grep jdk)
tar -xvf $jdk
jdk=`ls|grep jdk.*[0-9]$`
mv $jdk /usr/local/
sed -i "\$a export JAVA_HOME=/usr/local/$jdk" /etc/profile	 
sed -i '$a export PATH=$PATH:$JAVA_HOME/bin' /etc/profile
ln -s /usr/local/$jdk/bin/java /usr/bin/java

# jenkins
jenkins=$(ls|grep jenkins)
rpm -ivh $jenkins --nosignature
sed -i 's/JENKINS_USER="jenkins"/JENKINS_USER="root"/g' /etc/sysconfig/jenkins
systemctl start jenkins
/sbin/chkconfig jenkins on

# python
yum -y install ncurses ncurses-devel  
yum -y install openssl openssl-devel
python=`ls|grep Python`
tar -xvf $python
python=`ls|grep Python.*[0-9]$`
cd $python
./configure --prefix=/usr/local/${python}
sed -i '205s/#//g' Modules/Setup
sed -i '210,212s/#//g' Modules/Setup
make && make install
sed -i '$a export PATH=$PATH:'"/usr/local/$python/bin" /etc/profile
cd -
rm -rf $python

# rvm
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
\curl -sSL https://get.rvm.io | bash -s stable
echo 'export PATH=$PATH:/usr/local/rvm/bin'>>/etc/profile

# vim
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
cp vimrc ~/.vimrc  # 第一次执行使用 :PluginInstall 安装插件；:PluginInstall 只在 vim中可使用

# docker
yum -y install docker
systemctl  start docker.service
systemctl  enable docker.service

# mldonkey
mldonkey=`ls|grep mldonkey`
mv  $mldonkey /usr/local/
cd /usr/local/$mldonkey
./configure  # 编译过程中需要手动输入y
gmake
cp /usr/local/$mldonkey/mlnet /usr/bin/mlnet # mlnet启动后, 生成 ~/.mldonkey/download.ini 中修改allow_ip 可外网访问

