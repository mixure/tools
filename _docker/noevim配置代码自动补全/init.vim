scriptencoding utf-8
set encoding=utf-8

"let g:python3_host_prog='/root/local/venv36/bin/python3'
call plug#begin('~/.local/share/nvim/plugged')

if has('nvim')
  Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
else
  Plug 'Shougo/deoplete.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif

Plug 'zchee/deoplete-jedi' "  Python 补全
Plug 'takkii/Bignyanco'   " Ruby补全
Plug 'vim-airline/vim-airline' " 状态栏插件
Plug 'vim-airline/vim-airline-themes' " 切换 vim-airline 主题
Plug 'jiangmiao/auto-pairs'
Plug 'scrooloose/nerdcommenter'
Plug 'sbdchd/neoformat'
Plug 'davidhalter/jedi-vim'
Plug 'git://github.com/scrooloose/nerdtree.git'
Plug 'morhetz/gruvbox'
call plug#end()

let g:deoplete#enable_at_startup = 1
autocmd InsertLeave,CompleteDone * if pumvisible() == 0 | pclose | endif

"let g:airline_theme='<simple>' # 配置出题

let g:jedi#completions_enabled = 0
let g:jedi#use_splits_not_buffers = "right"


set nocp
set nu
set ic
set is
set hls

autocmd vimenter * NERDTree
let NERDTreeWinPos=1

colorscheme gruvbox
set background=dark
autocmd FileType ruby set tabstop=2 |set shiftwidth=2 "tabstop表示Tab代表2个空格的宽度
autocmd FileType python set tabstop=4 |set shiftwidth=4
set expandtab "表示Tab自动转换成空格
set autoindent "表示换行后自动缩进
set smartindent "智能对齐
set mouse=a
set listchars=tab:>-,trail:-,space:* "空格显示为点
set list
