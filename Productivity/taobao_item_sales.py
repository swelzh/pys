
#coding=utf-8

import requests
import re
import json


# use proxy
# res : <Response [200]>


def open_url(keyword):
	payload = {'q':'零基础入门学习Python', "sort":"sale-desc"}
	url = 'https://s.taobao.com/search'
	res = requests.get(url, params=payload)
	return res

def main():

	keyword = input("请输入搜索关键词:")
	res = open_url(keyword)

	with open("items.txt","w",encoding='utf-8') as file:
		file.write(res.text)


if __name__ == "__main__":
	main()