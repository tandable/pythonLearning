import urllib.request
import os

def url_open(url):
	req = urllib.request.Request(url)
	req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36")
	response = urllib.request.urlopen(url)
	html = response.read()

	return html

def get_page(url):
	html = url_open(url).decode("utf-8")
	big = html.find("result")
	a = html.find("www.espn.com/nba/team/photos/_/name/gs/photoId",big)+47
	b = html.find(">", a)-1

	return html[a:b]

def next_page(url):
	html = url_open(url).decode("utf-8")
	area = html.find('class=\"result\"')
	a = html.find("<a href=",area)
	b = html.find(">", a)

	return html[a+11:b-1]

def find_img(url,img_url):
	
	html = url_open(url).decode("utf-8")

	area = html.find('class=\"result\"')
	a = html.find("<img src=", area)
	b = html.find(">", a, a+255)
	if b != -1:
		img_url.append(html[a+10:b-2])
	
	print(img_url.__len__())
	return img_url


def save_imgs(folder, img_addrs):
	for each in img_addrs:
		filename = each.split('%')[-1].split('&')[0]
		with open(filename,'wb') as f:
			img = url_open(each)
			f.write(img)

def nba(folder = "warriors", pages = 10):
	os.mkdir(folder)
	os.chdir(folder)

	url = "http://www.espn.com/nba/team/photos/_/name/gs"
	page_num = int(get_page(url))
	img_url = []

	page_url = "http://www.espn.com/nba/team/photos/_/name/gs/photoId/" + str(page_num)

	for i in range(pages):
		img_addrs = find_img(page_url,img_url)
		next_addrs = "http://" + str(next_page(page_url))
		page_url = next_addrs
	for each in img_addrs:
		print(each)

	save_imgs(folder, img_addrs)

if __name__ == '__main__':
	nba()
