import requests
import bs4
import re

res = requests.get("https://movie.douban.com/top250")


"""
<div class="hd">
    <a href="https://movie.douban.com/subject/1292052/" class="">
        <span class="title">肖申克的救赎</span>
        <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
		<span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
    </a>
    <span class="playable">[可播放]</span>
</div>
"""

# soup = bs4.BeautifulSoup(res.text, "html.parser")
# targets = soup.find_all("div",class_="hd")
# for each in targets:
#     print(each.a.span.text)		#获取到a标签的第一个span的text


# 使用代理 
# res : <Response [200]>
def open_url(url):
	headers = {'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
	res = requests.get(url,headers=headers)
	return res



#找出多少个页面：10个页面
def find_depth(res):
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	# 在文档树中,使用 .next_sibling 和 .previous_sibling 属性来查询兄弟节点:
	depth = soup.find('span', class_='next').previous_sibling.previous_sibling.text
	return int(depth)


def find_movies(res):
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	#电影名
	movies = []
	targets = soup.find_all("div",class_="hd")
	for each in targets:
		movies.append(each.a.span.text)

	#评分
	ranks = []
	targets = soup.find_all("div",class_="star")
	
	for each in targets:
		ranks.append('评分: %s' % each.find('span',class_='rating_num').text)

	# 资料
	messages = []
	targets = soup.find_all("div",class_="bd")
	for each in targets:
		try:
			messages.append(each.p.text.split('\n')[1].strip() + each.p.text.split('\n')[2].strip())
		except:
			continue

	result = []
	length = len(movies)
	for i in range(length):
		result.append(movies[i] + ranks[i]  + messages[i] + '\n')

	return result


#main函数
def main():
	host = "https://movie.douban.com/top250"
	res = open_url(host)
	depth = find_depth(res)

	result = []
	for i in range(depth):
		url = host + '/?start=' + str(25*i)
		# print(url)
		res = open_url(url)
		result.extend(find_movies(res))

	with open("豆瓣TOP250电影.txt","w",encoding="utf8") as f:
		for each in result:
			f.write(each)



if __name__ == "__main__":
	main()


