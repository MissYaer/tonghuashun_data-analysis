import urllib.request
import random
import urllib.parse
import pymysql
from bs4 import BeautifulSoup


db_host = '122.51.252.42'
db_user = 'root'
db_pass = 'MySql#Houjiji2019'
db_name = 'houjiji_site'
db_port = 3306
db_table_question = 'cms_shushi_question'
db_table_answer = 'cms_shushi_answer'
question_id = 0

my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
    ]


def main(url, i):
    try:
        randdom_header = random.choice(my_headers)
        req = urllib.request.Request(url)
        req.add_header("User-Agent", randdom_header)
        req.add_header("Cookie","searchGuide=sg; __utmz=68909069.1564586690.7.3.utmcsr=moni.10jqka.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/zyl.shtml; spversion=20130314; user=MDptb180MjQ1OTY0NTM6Ok5vbmU6NTAwOjQzNDU5NjQ1Mzo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxLDQwOzIsMSw0MDszLDEsNDA7NSwxLDQwOzgsMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDEsNDA6MjQ6Ojo0MjQ1OTY0NTM6MTU3NjA2OTc3Mzo6OjE1MTExNzU5NjA6NjA0ODAwOjA6MTVkNWVjMDZhMjM1YmZkYWMxZmQwMWM4ODdhM2FjNGU1OmRlZmF1bHRfMzox; userid=424596453; u_name=mo_424596453; escapename=mo_424596453; ticket=2f03f3d7f0956bc265352c213e408feb; historystock=002504%7C*%7C603077%7C*%7C600712%7C*%7C600779; v=An6tnp8Or95hOvv6MmJelTpByZ_Dv0Ip1IP2FyiH6kG8yxAJkE-SSaQTRiH7; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1576149938,1576236282,1576495749,1576551225; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1576551225; Hm_lvt_a9190969a435c4c490361fdf65267856=1576149938,1576236282,1576495749,1576551225; Hm_lpvt_a9190969a435c4c490361fdf65267856=1576551225; __utma=68909069.1680085010.1562858905.1576495748.1576551226.87; __utmc=68909069; __utmt=1; __utmb=68909069.1.10.1576551226")
        req.add_header("GET", url)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find('meta',attrs={'name':'keywords'})['content']
        content = soup.find_all(class_='bam_content')
        best_answer_module = soup.find_all(class_='best_answer_module')
        # 最佳答案只有一次
        best_answer = 0
        if best_answer_module:
            best_answer = 1

        question_id = save_question(i, title)
        for t in content:
            save_answer(question_id, t.string, best_answer)
            best_answer = 0
            print(t.string+'插入成功')
    except Exception as e:
        print(e)
        print('error')

def save_question(shushi_id, content):
    db = pymysql.connect(db_host, db_user, db_pass, db_name, db_port)
    cursor = db.cursor()
    sql = "INSERT INTO %s (shushi_id,content)VALUES ('%s','%s')" % (db_table_question, shushi_id, content)
    cursor.execute(sql)
    db.commit()
    db.close()
    return cursor.lastrowid

def save_answer(shushi_id, content, best_answer):
    db = pymysql.connect(db_host, db_user, db_pass, db_name, db_port)
    cursor = db.cursor()
    sql = "INSERT INTO %s (question_id,content,best_answer)VALUES ('%s','%s', %d)" % (db_table_answer, shushi_id, content, best_answer)
    cursor.execute(sql)
    db.commit()
    db.close()



if __name__ == '__main__':
    i = 10166
    while True:
        i = int(i)
        i += 1
        i = str(i)
        url = "http://www.shushi100.com/ask/"+i+".html"
        print(url)
        main(url, i)

