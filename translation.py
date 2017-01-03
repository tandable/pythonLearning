import urllib.request
import urllib.parse
import json
import time
while True:

	content = input("请输入想要翻译的内容(输入end结束):")
	if content == "end":
		break



	url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link"
	data = {}
	data["type"] = "AUTO"
	data["i"] = content
	data["doctype"] = "json"
	data["xmlVersion"] = "1.8"
	data["keyfrom"] = "fanyi.web"
	data["ue"] = "UTF-8"
	data["action"] = "FY_BY_CLICKBUTTON"
	data["typoResult"] = "true"

	data = urllib.parse.urlencode(data).encode("utf-8")

	req = urllib.request.Request(url,data)
	req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36")

	response = urllib.request.urlopen(req)
	html = response.read().decode("utf-8")

	target = json.loads(html)
	print(target["translateResult"][0][0]["src"]+"的翻译是："+target["translateResult"][0][0]["tgt"])
	print(target["smartResult"]["entries"][1]+"\n"+target["smartResult"]["entries"][2])
	print(req.headers)
	time.sleep(5)
