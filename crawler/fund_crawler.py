# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url_format = 'http://stocks.sina.cn/fund/?code={}&vt=4'


def get_fund_info(fund_id):
    fund_info = {}
    url = url_format.format(fund_id)
    r = requests.get(url)
    assert(r.status_code == 200)
    soup = BeautifulSoup(r.text)
    title = soup.find('title').string
    fund_info['title'] = title
    raw_basic_infos = soup.find_all('div', class_='stock_content')
    for basic_info in raw_basic_infos:
        name_tag = basic_info.find('span', class_='stock_info_name')
        value_tag = basic_info.find('span', class_='stock_info_value')
        if '单位净值' in name_tag.string:
            fund_info['value'] = float(value_tag.string)
        if '净值增长率' in name_tag.string:
            fund_info['growth_rate'] = value_tag.string
        print(name_tag.string, value_tag.string)

    return fund_info

if __name__ == "__main__":
    print(get_fund_info(161725))
