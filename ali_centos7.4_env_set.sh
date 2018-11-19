#! /bin/bash
#

#
echo "LC_ALL=en_US.UTF-8
LANG=en_US.UTF-8">>/etc/environment

#
yum -y install git
sed -i "\$a vi=vim" $HOME/.bashrc
sed -i "\$a h=history" $HOME/.bashrc
echo 'alias vi=vim'>>~/.bashrc

# jdk
jdk=`rpm -qa|grep openjdk`
if test -n "$jdk";then
        echo -e "Remove openjdk manually (y|Y) ?, other input to ignore it. "
        read ans
        [ "$ans" == "y" -o "$ans" == "Y" ] && echo 0 
fi
jdk=`ls|grep jdk`
tar -xvf $jdk
jdk=`ls|grep jdk.*[0-9]$`
mv $jdk /usr/local/
sed -i "\$a export JAVA_HOME=/usr/local/${jdk}" /etc/profile
sed -i '$a export PATH=$PATH:$JAVA_HOME/bin' /etc/profile
ln -s /usr/local/$jdk/bin/java /usr/bin/java

# jenkins
jenkins=`ls|grep jenkins`
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
./configure --prefix=/usr/local/$python
sed -i "s/#_socket socketmodule.c/_socket socketmodule.c/g" Module/Setup
ssl='_ssl _ssl.c 	-DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl -L$(SSL)/lib -lssl -lcrypto'
sed -i "209a $ssl" Module/Setup 
make&&make install
echo 'export PATH=$PATH:'"/usr/local/$python/bin">> /etc/profile
cd -&& rm -rf $python

# rvm
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
\curl -sSL https://get.rvm.io | bash -s stable
echo 'export PATH=$PATH:/usr/local/rvm/bin'>> /etc/profile

# vim
cp vimrc ~/.vimrc
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

# mldonkey
mldonkey=`ls|grep mldonkey`
cp -r $mldonkey /usr/local
cd /usr/local/$mldonkey
echo y|./configure
gmake
cp /usr/local/$mldonkey/mlnet /usr/bin/mlnet

echo -e "启动mlnet后, 在~/.mldonkey/downloads.ini 修改downloads.ini=["0.0.0.0/0";]\n"
echo -e "退出后登陆获取环境变量\n"
echo -e "第一次使用vim需运行 :PlugnInstall安装插件\n" # 只有使用vim命令时，才能识别 :PlugnInstall命令, 所以使用vi时，需要让vi=vim生效
