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
