#! /usr/bin/env python3
# coding=utf-8

import time
from urllib.parse import urljoin
from selenium import webdriver
from bs4 import BeautifulSoup
from logzero import logger

domain='http://ra.sunfund.com/'
title404="您访问的页面不存在-宜人贷"
page_size404=1308

dr=webdriver.Firefox()

def scrap_url(url,orginal_url=None,scrap=True):
    """
        a页面有b页面超链接,同时b页面有a页面超链接.访问a->解析出b->访问b->解析出a
        ->访问a,不对a页面再次解析,此时scrap=False
    """
    status_code=200
    try:
        now=time.time()
        dr.get(url)

        #根据title判断/或者404页面文件都比较小
        # if dr.title==title404: status_code=404
        if len(dr.page_source)<=page_size404: status_code=404
        html=dr.page_source
        soup=BeautifulSoup(html,'html.parser')
    except Exception as e:
        dr.get_screenshot_as_base64('f{orginal_url}_to_{url}')
    finally:
        t='%.2f' %(time.time()-now)
        if status_code==200:
            mod="32m"
        elif status_code==404:
            mod="31m"
        logger.debug(f'{orginal_url} to {url} \033[0;34m {t}s \033[0m '
            f'\033[0;{mod}{status_code}\033[0m')
        logger.debug(dr.title)

    more_seeds=[]

    #有些网站的站内的超链接不是href参数提供的,需要继续在if修改
    # 有些还有外链，都是在这处理....
    if scrap and status_code==200:
        for a in soup.find_all(href=True):
            if a['href'].startswith('/'):
                more_seeds.append((urljoin(domain,a['href']),url))
    return more_seeds

def main(domain):
    seeds=scrap_url(domain)
    old_urls=[]
    while seeds:
        seed,seeds=seeds[0],seeds[1:]
        url,orginal_url=seed
        if url not in old_urls:
            more_seeds=scrap_url(url,orginal_url)
            old_urls.append(url)
        else:
            more_seeds=scrap_url(url,orginal_url,False)
        seeds.extend(more_seeds)

main(domain)
dr.quit()
