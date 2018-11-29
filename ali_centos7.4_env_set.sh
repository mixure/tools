#! /bin/bash

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
