import urllib.request
import random
from bs4 import BeautifulSoup
import pymysql
import time
import urllib.parse
import datetime

my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
    ]

db_host = '127.0.0.1'
db_user = 'root'
db_pass = '123456'
db_name = 'tonghuashun'
db_port = 3307
db_table_name = str(datetime.datetime.now().year)+"_"+str(datetime.datetime.now().month)+"_"+str(datetime.datetime.now().day)+"_"+str(datetime.datetime.now().hour)+"_"+str(datetime.datetime.now().minute)+"_"+str(datetime.datetime.now().second)

def main(url):
    randdom_header = random.choice(my_headers)

    req = urllib.request.Request(url)

    req.add_header("User-Agent", randdom_header)
    req.add_header("Cookie","searchGuide=sg; __utmz=68909069.1564586690.7.3.utmcsr=moni.10jqka.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/zyl.shtml; spversion=20130314; user=MDptb180MjQ1OTY0NTM6Ok5vbmU6NTAwOjQzNDU5NjQ1Mzo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxLDQwOzIsMSw0MDszLDEsNDA7NSwxLDQwOzgsMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDEsNDA6MjQ6Ojo0MjQ1OTY0NTM6MTU3NjA2OTc3Mzo6OjE1MTExNzU5NjA6NjA0ODAwOjA6MTVkNWVjMDZhMjM1YmZkYWMxZmQwMWM4ODdhM2FjNGU1OmRlZmF1bHRfMzox; userid=424596453; u_name=mo_424596453; escapename=mo_424596453; ticket=2f03f3d7f0956bc265352c213e408feb; historystock=002504%7C*%7C603077%7C*%7C600712%7C*%7C600779; v=An6tnp8Or95hOvv6MmJelTpByZ_Dv0Ip1IP2FyiH6kG8yxAJkE-SSaQTRiH7; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1576149938,1576236282,1576495749,1576551225; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1576551225; Hm_lvt_a9190969a435c4c490361fdf65267856=1576149938,1576236282,1576495749,1576551225; Hm_lpvt_a9190969a435c4c490361fdf65267856=1576551225; __utma=68909069.1680085010.1562858905.1576495748.1576551226.87; __utmc=68909069; __utmt=1; __utmb=68909069.1.10.1576551226")
    req.add_header("GET", url)

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    t_list = soup.find_all(class_='paihang_business_userid')
    deal_data(t_list)

def deal_data(t_list):
    # 消息头数据
    headers = {
        'Cache-Control': 'max-age=0',
        'Origin': 'https://passport.csdn.net',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Referer': 'https://passport.csdn.net/account/login?from=http://www.csdn.net',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'Cookie': 'searchGuide=sg; __utmz=68909069.1564586690.7.3.utmcsr=moni.10jqka.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/zyl.shtml; spversion=20130314; Hm_lvt_a9190969a435c4c490361fdf65267856=1575081241,1575277733,1575292799,1575419712; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1575081241,1575277733,1575292799,1575419712; __utma=68909069.1680085010.1562858905.1575296324.1575419712.66; __utmc=68909069; __utmt=1; user=MDptb180MjQ1OTY0NTM6Ok5vbmU6NTAwOjQzNDU5NjQ1Mzo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxLDQwOzIsMSw0MDszLDEsNDA7NSwxLDQwOzgsMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDEsNDA6MjQ6Ojo0MjQ1OTY0NTM6MTU3NTQxOTcyMzo6OjE1MTExNzU5NjA6NjA0ODAwOjA6MWZkMTQxNjM2NDBkMWJiZDE1ZTM3MWI5ODc0Y2QxNGZhOmRlZmF1bHRfMzox; userid=424596453; u_name=mo_424596453; escapename=mo_424596453; ticket=716a16d7f0c4c1588e78798dec8681ac; historystock=600678%7C*%7C000034%7C*%7C002504%7C*%7C000785; v=AgbV9tf2p_e2knOSIKtBARstUfeLZ0ouHKt-hfAv8ikE86ihWPeaMew7zpnD; Hm_lpvt_a9190969a435c4c490361fdf65267856=1575419972; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1575419973; __utmb=68909069.15.10.1575419712'
    }
    create_table()
    for t in t_list:
        get_user(t,headers)
        links = 'http://moni.10jqka.com.cn/' + t.get('userid')
        req = urllib.request.Request(links)
        randdom_header = random.choice(my_headers)
        req.add_header("User-Agent", randdom_header)
        req.add_header("Cookie","searchGuide=sg; __utmz=68909069.1564586690.7.3.utmcsr=moni.10jqka.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/zyl.shtml; spversion=20130314; historystock=000785%7C*%7C002552%7C*%7C002057%7C*%7C600093; __utma=68909069.1680085010.1562858905.1574656997.1574774519.57; __utmc=68909069; __utmt=1; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1574311658,1574383197,1574656997,1574774520; Hm_lvt_a9190969a435c4c490361fdf65267856=1574311658,1574383197,1574656997,1574774522; user=MDptb180MjQ1OTY0NTM6Ok5vbmU6NTAwOjQzNDU5NjQ1Mzo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxLDQwOzIsMSw0MDszLDEsNDA7NSwxLDQwOzgsMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDEsNDA6MjQ6Ojo0MjQ1OTY0NTM6MTU3NDc3NDYyNzo6OjE1MTExNzU5NjA6NjA0ODAwOjA6MWRlMjA5ZjJmOTQyNjcxMDBiM2FiOThjMTMzNGJmNDU2OmRlZmF1bHRfMzox; userid=424596453; u_name=mo_424596453; escapename=mo_424596453; ticket=7148da0940c9ddea187a3a1020c37528; v=Aif0EY79NuNmu7JvzqpQfuJWsFDyrPuOVYB_AvmUQ7bd6EkGAXyL3mVQD1MK; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1574774736; Hm_lpvt_a9190969a435c4c490361fdf65267856=1574774736; __utmb=68909069.6.10.1574774519")
        print(links)
        req.add_header("GET", links)
        time.sleep(3)
        try:
            response2 = urllib.request.urlopen(req)
            html = response2.read().decode('utf-8')
            soup = BeautifulSoup(html, "html.parser")
            i = 0
            share_user = []
            share_data = []
            for t in soup.find_all('td'):
                db = pymysql.connect(db_host, db_user, db_pass, db_name, db_port)
                cursor = db.cursor()
                i = i + 1
                if i <= 10:
                    if i % 2 == 0:
                        share_user.append(str(t.string))
                if i > 30:
                    share_data.append(str(t.string))
                    if i % 10 == 0:
                        result = check_user(share_data, share_user)
                        if result == False:
                            continue
                        sql = save_data(share_data, share_user)
                        cursor.execute(sql)
                        db.commit()
                        db.close()
                        share_data = []
        except Exception as e:
            print(e)
            print('error')

def check_user(share_data, share_user):
    # 不赌博
    #if share_data[1][-1] == '退':
    #    return False
    #if int(share_user[2][0:2]) != 10:
    #    if int(share_user[2][0:2]) < 70:
    #        return False
    if share_data[1] == '买入':
        return False
    if share_data[1] == '卖出':
        return False
    if share_data[3] == '买入':
        return False
    if share_data[3] == '卖出':
        return False
    share_id = str(share_data[0])
    first_number = share_id[0:1]
    if first_number == '3':
        return False
    return True

def get_user(t, headers):
    postData = {
        "masterid": t.get('userid'),
        "mastername": t.get('username'),
        "masterusrid": t.get('usrid')
    }
    postData = bytes(urllib.parse.urlencode(postData), encoding='utf8')
    url2 = 'http://moni.10jqka.com.cn/moni/index/tracemaster4business'
    request = urllib.request.Request(url2, headers=headers, data=postData, method='POST')
    urllib.request.urlopen(request)


def save_data(share_data, share_user):
    sql = "INSERT INTO %s (share_id,share_name,have_number,have_time,profit_loss_cost, \
                                           present_price, today_gains, stock_market_capitalization, profit_loss_ratio,floating_p_l,create_time,warehouse_position,success,count_number,user_add_time) \
                                           VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
           (
            db_table_name,
            share_data[0],
            share_data[1],
            share_data[2],
            share_data[3],
            share_data[4],
            share_data[5],
            share_data[6],
            share_data[7],
            share_data[8],
            share_data[9],
            int(time.time()),
            share_user[1],
            share_user[2],
            share_user[3],
            share_user[4])
    print(sql)
    return sql

def create_table():
    db2 = pymysql.connect(db_host, db_user, db_pass, db_name, db_port)
    cursor2 = db2.cursor()

    table_sql = '''CREATE TABLE %s (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
          `share_id` varchar(255) DEFAULT NULL COMMENT '股票代码',
          `share_name` varchar(255) DEFAULT NULL COMMENT '股票名称',
          `have_number` varchar(255) DEFAULT NULL COMMENT '持仓量',
          `have_time` varchar(255) DEFAULT NULL COMMENT '建仓时间',
          `profit_loss_cost` varchar(255) DEFAULT NULL COMMENT '盈亏成本',
          `present_price` varchar(255) DEFAULT NULL COMMENT '现价',
          `today_gains` varchar(255) DEFAULT NULL COMMENT '今日涨幅',
          `stock_market_capitalization` varchar(255) DEFAULT NULL COMMENT '股票市值',
          `profit_loss_ratio` varchar(255) DEFAULT NULL COMMENT '盈亏率',
          `floating_p_l` varchar(255) DEFAULT NULL COMMENT '浮动盈亏',
          `create_time` varchar(255) DEFAULT NULL COMMENT '创建时间',
          `warehouse_position` varchar(255) DEFAULT NULL COMMENT '仓位',
          `success` varchar(255) DEFAULT NULL COMMENT '成功率',
          `count_number` varchar(255) DEFAULT NULL COMMENT '操作次数',
          `user_add_time` varchar(255) DEFAULT NULL COMMENT '加入时间',
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=559 DEFAULT CHARSET=utf8;'''
    cursor2.execute(table_sql % db_table_name)
    db2.commit()
    db2.close()

if __name__ == '__main__':
    # 排行榜数据
    #url = "http://moni.10jqka.com.cn/paihang.shtml"
    # 成功
    #url = "http://moni.10jqka.com.cn/xgcg.shtml"
    # 一个月排行榜
    url = "http://moni.10jqka.com.cn/yyl.shtml"
    #
    #url = "http://moni.10jqka.com.cn/zyl.shtml"
    # 段位
    #url = "http://moni.10jqka.com.cn/dw.shtml"
    main(url)