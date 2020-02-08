import requests
import time
import os
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = BASE_DIR + '/clientdata/data/'

if __name__ == "__main__":

    a = 0
    j_paht = path + 'poet.song.' + str(a*1000) + '.json'
    f =  open(j_paht, 'r')
    while f:
        print(str(a))
        try:
            json_str = f.read()
            data = json.loads(json_str)
            data_json = data
            for item_t in data_json:
                author = item_t["author"]
                paragraphs_list = item_t["paragraphs"]
                paragraphs = ''
                for str_0 in paragraphs_list:
                    paragraphs = paragraphs + str_0

                strains_list = item_t["strains"]
                strains = ''
                for str_1 in strains_list:
                    strains = strains + str_1

                title = item_t["title"]


                '''
                chapterlist_path cover_path insert
                '''
                params_p = {
                    "value":'',
                    "author": author,
                    "content": paragraphs,
                    "strains": strains,
                    "title": title
                }
                url_p = 'http://127.0.0.1:8000/song/shi/'
                headers_p = {
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                    'Cache-Control': 'no-cache',
                }

                rsp = requests.post(url_p, headers=headers_p, data=params_p)
                print(rsp)

        except Exception as e:
            print(e)
            pass
        a = a + 1
        t = a * 1000
        j_paht = path + 'poet.song.' + str(t) + '.json'
        time.sleep(2)
        f = open(j_paht, 'r')

