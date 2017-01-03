import re
import urllib.request

def open_url(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36')
	page = urllib.request.urlopen(req)
	html = page.read().decode('utf-8')


	return html


def getimg(html):
	p = r'src="[^"]+\.jpg"'
	#p = r'<img id="dlg_pi_img"[/s/S]+src="[^"]+\.jpg"'
	imglist = re.findall(p,html)

	print(imglist.__len__())
	


	for each in imglist:
		print(each)


if __name__ == '__main__':
	url = "http://tieba.baidu.com/p/2125393131#!/l/p1"
	getimg(open_url(url))
