
#coding=utf-8

import requests

import json


# use proxy
# res : <Response [200]>

def get_hot_comments(res):
	comments_json = json.loads(res.text)
	hot_comments = comments_json['hotComments']
	with open('hot_comments.txt','w',encoding='utf-8') as file:
		for each in hot_comments:
			file.write(each['user']['nickname'] + ':\n\n')
			file.write(each['content'] + '\n')
			file.write('-----------------')

def open_url(url):

	name_id = url.split('=')[1]

	headers = {
		'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
		'referer' : 'https://music.163.com/mv?id=%s'%name_id
	}
	params = '5rQqUfSpZHUBGZTT7RHwXQGSk6027W1rnwhrIZAjftW0mQpVXr22pHheB7evjG7nvM6ew61PYpW9V4vQY7U/FchgGQXMbmmbVTO47M5lJOf+tPezBG/7aKf4bRsBfKmPYtyaNbq1XMONwJua7zLQoRFlrwrBpwxx712FTp+6gV2vEUf4ZiPnkABLqenfmkmX'
	encSecKey = '13daab603a7accec4786055bf1f1b06abf882e9ee394096a688e6bad09fb70f0fdd1e88d6d75e51747260ccceddcb3f97fd03c58c92890b4d4539b81109acec781f2b68a9e4687da34d7da53bb79542bdc247c59ca40531e96c614269d53e8b5b7d9b5f513138411a4db1c2139372401e83135cbbfcd6d6931c042988b6b2a2c'
	data = {
		'params':params,
		'encSecKey':encSecKey
	}
	
	# target_url = 'https://music.163.com/weapi/v1/resource/comments/R_MV_5_%s?csrf_token='%song_id
	target_url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(name_id)
	res = requests.post(target_url,headers=headers, data=data)

	return res


def main():
	url = input("请输入链接地址")
	res = open_url(url)
	get_hot_comments(res)

	with open("网易云音乐评论.json","w",encoding="utf-8") as f:
		f.write(res.text)


if __name__ == "__main__":
	main()