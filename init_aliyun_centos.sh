#! /bin/bash
#

#
echo "LC_ALL=en_US.UTF-8
LANG=en_US.UTF-8">>/etc/environment

# set alias
file_name=~/.bashrc
sed -i '$a alias ls="ls -F"' $file_name
sed -i '$a alias h=history' $file_name

# set vim
sed -i '$a alias vi=vim' $file_name
curl -o ~/.vimrc https://raw.githubusercontent.com/mixure/tools/master/vimrc_aliyun_centos
yum -y install git
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

# set docker
curl -o /etc/yum.repos.d/docker-ce.repo  https://mirrors.ustc.edu.cn/docker-ce/linux/centos/docker-ce.repo
yum -y install docker-ce
systemctl daemon-reload && systemctl restart docker

# jdk
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
sed -i '205s/#//g;210,212s/#//g' Modules/Setup
make && make install
sed -i '$a export PATH=$PATH:'"/usr/local/$python/bin" /etc/profile
cd -
rm -rf $python

# rvm
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
\curl -sSL https://get.rvm.io | bash -s stable
echo 'export PATH=$PATH:/usr/local/rvm/bin'>>/etc/profile

# mldonkey
mldonkey=`ls|grep mldonkey`
mv  $mldonkey /usr/local/
cd /usr/local/$mldonkey
./configure  # 编译过程中需要手动输入y
gmake
cp /usr/local/$mldonkey/mlnet /usr/bin/mlnet # mlnet启动后, 生成 ~/.mldonkey/download.ini 中修改allow_ip 可外网访问
